# 引入date、os库
import datetime
import os
# 引入请求库
import requests
# 引入 images 库
from PIL import Image
# 引入qrcode
import qrcode
# 引入pyperclip
import pyperclip
# 引入shutil
import shutil


# 判断当前目录下是否有临时缓存文件夹
if not os.path.exists('./tmp'):
    os.mkdir('./tmp')
# 判断当前目录下是否有img文件夹
if not os.path.exists('./img'):
    os.mkdir('./img')
# 输入法切换为英文状态
os.system('setxkbmap -layout us')
# 输入商品ID
goods_id = input("请输入商品ID (多个产品以,隔开):")
# 判断输入是否包含中文逗号，如果有转换为英文逗号
if '，' in goods_id:
    goods_id = goods_id.replace('，', ',')
# 如果商品ID为空，则输出错误信息
if goods_id == "":
    print("商品 ID 不能为空")
    exit()

# 输入日期(yyMMDD)
date = input("请输入日期(yyMMDD):")
# 如果日期输入为空
if date == "":
    # 输入提示“将默认使用当前系统日期”
    print("已默认使用当前系统日期")
    # 则设置为当前日期，格式为yyMMDD
    date = datetime.datetime.now().strftime("%y%m%d")

# 将输入的商品ID以“,”分割
goods_id = goods_id.split(",")

# 将商品ID循环执行
for i in goods_id:
    # 定义图像链接为：https://union.lizhi.io/partner/product/[商品ID]/poster
    url = "https://union.lizhi.io/partner/product/" + i + "/poster?cid=53qvofdc"
    # 请求图像链接
    response = requests.get(url)
    # 如果请求成功
    if response.status_code == 200:
        # 从返回头获取图像文件名
        filename = response.headers['Content-Disposition'].split('=')[1]
        # 按“”分割，取第二段文件名
        filename = filename.split('"')[1]
        # 按.分割，去掉后缀
        filename = filename.split('.')[0]
        # 将文件名使用 raw_uncode_escape 转义
        filename = filename.encode('raw_unicode_escape').decode('utf-8')
        # 将图像以 日期_filename 保存到临时文件夹
        with open('./tmp/' + date + "_" + filename, 'wb') as f:
            f.write(response.content)
            # 打印下载进度
            print("处理进度：" + str(goods_id.index(i) + 1) + "/" + str(len(goods_id)))
        # 将图片转换为PIL格式
        img = Image.open('./tmp/' + date + "_" + filename)
        # 生成180*180px的二维码，容错率为L
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # 定义二维码链接为 https://store.lizhi.io/site/products/id/[商品ID]?cid=53qvofdc&hmsr=wechat&hmpl=p[日期]
        qr_url = "https://store.lizhi.io/site/products/id/" + i + "?cid=53qvofdc&hmsr=wechat&hmpl=p" + date
        # 将二维码内容设置为：
        qr.add_data(qr_url)
        # 生成二维码，并更改图像大小为180*180px
        qr.make_image()
        # 图像尺寸设置为180*180px
        code_img = qr.make_image(fill_color="black", back_color="white").resize((180, 180))
        # 将code_img贴到图片上760,172位置
        img.paste(code_img, (760, 172))
        # 图片以png格式保存到 img 文件夹
        img.save('./img/' + date + "_" + filename + '.png', 'PNG')
        
        # 如果商品ID只有1个，则输出：原文链接：qr_url
        if len(goods_id) == 1:
            print("原文链接：" + qr_url)
            # 将qr_url复制到剪切板
            pyperclip.copy(qr_url)
            # 禁止跳出
            input("已将原文链接复制到剪切板，按回车键退出")

    # 如果请求失败，则输出错误信息：图像源文件请求失败，请商品是否存在及商品ID是否正确
    else:
        print("图像源文件请求失败，请商品是否存在及商品ID是否正确")

# 删除整个临时文件夹
shutil.rmtree('./tmp')
# 如果商品ID数量大于1，则输出：原文链接：https://store.lizhi.io?cid=53qvofdc&hmsr=wechat&hmpl=p[日期]
if len(goods_id) > 1:
    print("原文链接：https://store.lizhi.io?cid=53qvofdc&hmsr=wechat&hmpl=p" + date)
    # 将https://store.lizhi.io?cid=53qvofdc&hmsr=wechat&hmpl=p[日期]复制到剪切板
    pyperclip.copy("https://store.lizhi.io?cid=53qvofdc&hmsr=wechat&hmpl=p" + date)
    # 禁止跳出
    input("已将原文链接复制到剪切板，按回车键退出")