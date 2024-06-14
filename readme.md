
# 语音识别助手

## 项目构成

* pycache 项目生成的文本文件，无需改动
* vosk-model-small-cn-0.22 中文语音识别模型
* vosk-model-small-en-us-0.15 英文语音识别模型
* actions.py 项目各项操作的定义与执行文件
* app.py 输出控制台提示
* config.py 配置文件
* __gui.py 图形界面文件，前端部分在此处进行配置__
* main.py 主函数文件
* record.py 录音与保存音频
* speech_text.py 进行语音转换

## 项目依赖环境

* vosk(已包含)
* PyQt5(需安装)
* pyaudio（需安装）
* request

## 项目功能

* 支持中英双语（在图形界面进行选择）
* 打开摄像头 "open camera"
* 打开音乐播放器 "open music player"
* 打开记事本 "open notepad"
* 搜索xxx(默认为百度引擎，若只输入搜索则只打开搜索引擎) "search xxx"
* 输出语音识别结果并进行提示
