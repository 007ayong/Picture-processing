import os
import datetime
from PIL import Image
import qrcode
import requests
import sys
import time
def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("进行中: {}% ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.01)
datas = input("请输入商品 ID，以逗号隔开：")
ids = datas.split(',')
def change_qrcode(ids):
    for id in ids:
        ISOTIMEFORMAT = '%y%m%d'
        theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        # 旧链接 https://store.lizhi.io/site/products/id/31?cid=53qvofdc&mtm_campaign=wechat&mtm_kwd=p210413
        # 新链接 https://store.lizhi.io/site/products/id/31?cid=53qvofdc&hmsr=wechat&hmpl=p210903
        Product_url = "https://store.lizhi.io/site/products/id/"
        url = Product_url + id + "?cid=53qvofdc&hmsr=wechat&hmpl=p" + theTime
        print("商品链接："+ url)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            border=4,
        )
        qr.add_data(url)
        img = qr.make_image()
        img_180_180 = img.resize((180,180),Image.ANTIALIAS)
        # 模板图片下载链接 https://union.lizhi.io/partner/product/349/poster?cid=53qvofdc
        dl_url = "https://union.lizhi.io/partner/product/" + id + "/poster?cid=53qvofdc"
        if os.path.exists("img"):
            print ("图像文件夹已存在")
        else:
            os.mkdir("img")
            print ("已创建图像文件夹")
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        r = requests.get(url=dl_url, headers=headers, stream=True, allow_redirects=False, timeout=10)
        if r.status_code == 200:
                    # 获取content下载数据源
                    content = r.content
                    # 获取返回头携带的文件名		 
                    h = r.headers['Content-Disposition']    # 获取返回头，文件名字段
                    s1 = h.split('=')[1]     # 按=号切割，取第二段文件名
                    s2 = s1.split('"')[1]      #按双引号切割，去掉前后双引号
                    s3 = s2.split('.')[0]    #按.切割，去掉后缀
                    f = s3.encode('raw_unicode_escape')    # 使用'raw_unicode_escape'编码
                    mould_name = f.decode('utf-8')       # 再用utf-8 解码
                    #file_path = path + file_name)	# 文件名可自定义，如自定义上一步获取文件名不需要
                    # 打开文件写入
                    with open('./img/'+ mould_name + '.jpg', 'wb') as f:
                        f.write(content)
                    progress_bar()
        mould = "./img/" + mould_name + ".jpg"
        bgimg = Image.open(mould)
        bgimg.paste(img_180_180,box=(760,172))
        bgimg.save("./img/" + theTime + "_" + mould_name + ".png")
        print("\n恭喜，新的图片创建成功！")
        print("文件名："+ theTime + "_" + mould_name + ".png")
        os.remove(mould)
change_qrcode(ids)
os.system("pause")