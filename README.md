# <p align="center"><strong>DouYinDownload</strong></p>
<h3 align="center">🔥抖音无水印视频图片下载🔥</h3>
<div align="center">
  <a href = "https://github.com/sakuraIsNow/DouYinDownload/edit/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"></a>
  <img src="https://img.shields.io/github/repo-size/sakuraIsNow/DouYinDownload?style=for-the-badge&color=8A2BE2">
  <img src="https://img.shields.io/github/languages/top/sakuraIsNow/DouYinDownload?style=for-the-badge&color=32CD32">
  <img src="https://img.shields.io/badge/PYTHON-V3.11.1-FFD700?style=for-the-badge">
</div>
<div align="center">
<img src="https://github.com/sakuraIsNow/DouYinDownload/blob/main/bg/search.png" width=100% height=100%>
</div>

## 🖥️Python环境配置
<div>建议使用python3.11.1版本或者更高版本，<a href = "https://www.python.org/">可在Python官网下载</a></div>
<div>其他版本运行可能报错</div>
安装python后，使用pip安装所需要的依赖库：

```bash
 pip install -r requirements.txt
```

## 🖱️初步使用
<div>
需要将你的cookie和服务下载路径进行配置，在/downloader/douYin/config.py文件中进行配置

```bash
cookie = r'your cookie here' # 你的cookie 最好使用登陆的cookie 游客cookie不稳定
pathDir = r'your path here' # 服务源文件下载文件夹路径,保证文件夹存在
```
cookie最好使用DouYin登陆的cookie，游客状态下的cookie不稳定  
cookie只保存在本地，不会上传以及用于非法用途等
</div>

<div>
可以在/douyinDownloadServer/setting.py中添加访问ip

```bash
ALLOWED_HOSTS = []
```
不添加默认为127.0.0.1
</div>
<div>
配置完后运行manage.py文件

```bash
python manage.py runserver
```
如果在ALLOWED_HOSTS中添加了ip，在上述运行命令中需要添加ip，默认为127.0.0.1:8000
</div>
<div>
  启动django服务后，在浏览器访问页面的搜索框中输入DouYin视频或图文链接点击搜索
</div>
<div>
  搜索完成后点击页面视频或者图片完成客户端的下载
</div>

## 💾功能
- DouYin视频或图文下载
- find.py可获取页面访问cookie(提前关闭浏览器)

## 📰版权声明
<div>MIT License</div>

<div>Copyright (c) 2021 JohnserfSeed</div>

<div>此项目的源代码在 MIT 许可证下授权，有关详细信息，请参阅 <a href = "https://github.com/sakuraIsNow/DouYinDownload/edit/main/LICENSE">LICENSE</a> 文件。</div>

## ❤️‍🔥感谢
<div><a href = "https://www.python.org/">Python</a></div>  
<div><a href = "https://github.com/Johnserf-Seed/TikTokDownload">f2</a></div>
<div><a href = "https://github.com/django/django">Django</a></div>
<div><a href = "https://github.com/globocom/m3u8">m3u8</a></div>
