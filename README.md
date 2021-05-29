在工作中要经常用做图软件去替换模版图片的二维码非常麻烦，重复性的工作非常浪费时间。因此决定尝试用 Python 做一个半自动化程序。

# 需求

- [x] 获取当前日期，截取数字，生成链接并替换二维码
- [x] 模板图片生成后以日期命名
- [x] 移除多余的原图片
- [ ] 生成可替换文字、图标、二维码链接的卡片
- [x] 多个商品 ID 获取卡片
- [x] 在原文件名前添加时间作为最终文件名
- [x] 尽量优化减少用到的第三方库

# 用法

1. 使用 Python3 运行程序，输入商品 ID

```shell
python3 app.py
```

2. 自动下载原图片，生成二维码并替换好二维码，以 `date_文件名.png` 保存
3. 最后将自动删除原图片

# 说明

- 本程序会读取系统时间，所以请在当天使用才能生成正确的链接及二维码；

- 需要用到的库 `Pillow` `qrcode` `requests`，使用 `pip install Pillow qrcode requests` 命令安装即可。

  

