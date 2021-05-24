# 获取链接后 6 位
import datetime
ISOTIMEFORMAT = '%y%m%d'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime)
# 链接 https://store.lizhi.io/site/products/id/31?cid=53qvofdc&mtm_campaign=wechat&mtm_kwd=p210413
url = "https://store.lizhi.io/site/products/id/31?cid=53qvofdc&mtm_campaign=wechat&mtm_kwd=p"
print(url+theTime)
newurl = url + theTime
from PIL import Image, ImageDraw, ImageFont
import qrcode
img = qrcode.make(data=newurl)
with open('test.png', 'wb') as f:
    img.save(f)

