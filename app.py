# 获取链接后 6 位
import datetime
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
with open('test.png', 'wb') as f:
    img.save(f)

