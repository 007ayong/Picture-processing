# 获取链接后 6 位
import datetime
from os import name
ISOTIMEFORMAT = '%y%m%d'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
# 链接 https://store.lizhi.io/site/products/id/31?cid=53qvofdc&mtm_campaign=wechat&mtm_kwd=p210413
Product_url = "https://store.lizhi.io/site/products/id/"
id = input("请输入商品 ID：")
url = Product_url + id + "?cid=53qvofdc&mtm_campaign=wechat&mtm_kwd=p" + theTime
print("商品链接："+ url)
# 引入处理图片的模块
from PIL import Image
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    border=4,
)
qr.add_data(url)
img = qr.make_image()
# 如果需要保存二维码图片，取消注释
#img.save(id + "二维码.png")
img_180_180 = img.resize((180,180),Image.ANTIALIAS)
# 模板图片下载链接 https://union.lizhi.io/partner/product/349/poster?cid=53qvofdc
import wget
dl_url = "https://union.lizhi.io/partner/product/" + id + "/poster?cid=53qvofdc"
wget.download(dl_url,id + ".jpg")
file_name = id + ".jpg"
print("模板图：" + file_name)
bgimg = Image.open(file_name)
bgimg.paste(img_180_180,box=(760,172))
bgimg.save(theTime + "_" + id + ".png")
print("恭喜🎉，新的图片创建成功！")
print("文件名："+ theTime + "_" + id + ".png")
import os
os.remove(file_name)
