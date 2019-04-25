# YouTube Dmooji 弹幕文件转 Bilibili 弹幕文件 (Transfer YouTube Dmooji danmaku file to Bilibili danmaku file)
[YouTube Dmooji](https://chrome.google.com/webstore/detail/dmooji-live-comments-danm/dcacgbaadlgfnmcpjncoobionpjnbnih) 是一款chrome插件，可以实现在YouTube上观看弹幕的功能，但是其弹幕文件不被一些主流弹幕视频播放器支持。而b站弹幕可以被很多弹幕视频播放器支持，故本代码旨在将YouTube Dmooji的弹幕文件(`.json`)转换成Bilibili的弹幕文件(`.xml`)
## 配置要求(Requirement)
### Python
* python == 3.6.0
### python modules
* absl-py == 0.2.0
* requests == 2.12.4
## 使用方式(Usage)
下载 Y2B.py. 打开命令提示符，切换到`Y2B.py`所在路径。
```cmd
python Y2B.py --youtube_url https://www.youtube.com/watch?v=video_id --dir D:\YouDirectory --name YourFileName
```
示例
```cmd
python Y2B.py --youtube_url https://www.youtube.com/watch?v=mhIeiUbH2gg --dir H:\YoutubeToBilibili --name heheda
```
运行上述命令后，即可在目录`H:\YoutubeToBilibili`下看到名为`heheda.xml`的弹幕文件。之后可以使用诸如[弹弹play](http://dandanplay.com/)这样的弹幕播放器加载弹幕文件。另外还可使用一些将弹幕文件转字幕文件的工具，例如[bilibili ASS 弹幕在线转换](https://tiansh.github.io/us-danmaku/bilibili/)，将弹幕文件转为字幕文件。
## 参数(argument)
### 必要参数(required argument)
- `--youtube_url`：YouTube的视频网页链接，格式为`https://www.youtube.com/watch?v=video_id`例如`https://www.youtube.com/watch?v=mhIeiUbH2gg`**注意：不是YouTube弹幕文件的链接。**
### 非必须参数(optional argument)
- `--dir`：弹幕文件的输出目录，默认为`Y2B.py`所在目录
- `--name`：弹幕文件的名称，默认为`video_id.py`，video_id 为视频链接中的id
