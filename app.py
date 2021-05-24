# 获取链接后 6 位
import datetime
from os import name
ISOTIMEFORMAT = '%y%m%d'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime)
# 链接 https://store.lizhi.io/site/products/id/31?cid=53qvofdc&mtm_campaign=wechat&mtm_kwd=p210413
Product_url = "https://store.lizhi.io/site/products/id/"
id = input("请输入商品 ID：")
url = Product_url + id + "?cid=53qvofdc&mtm_campaign=wechat&mtm_kwd=p" + theTime
print(url)
# 引入处理图片的模块
from PIL import Image, ImageDraw, ImageFont
import qrcode
img = qrcode.make(data=url)
img_180_180 = img.resize((180,180),Image.ANTIALIAS)
file_name = id + ".jpg"
print(file_name)
bgimg = Image.open(file_name)
#img = Image.open("qrcode.jpg")
bgimg.paste(img_180_180,box=(760,172))
#bgimg = bgimg.convert("RGB")
bgimg.save(theTime+"-"+id+".png")
