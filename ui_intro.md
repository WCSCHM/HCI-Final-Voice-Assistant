# UI介绍文档

### 概述
这是一个基于PyQt5构建的语音助手应用程序。用户可以选择语言并点击按钮开始语音识别。应用程序通过调用process_command函数处理语音指令，并根据识别结果执行相应操作。

### UI组件和布局
#### ‘VoiceAssistant’类
- 初始化UI (initUI)：设置窗口标题、大小、以及整体布局。窗口固定大小为660x1200。

- 背景GIF (bg_label)：用于显示动态GIF。背景GIF默认不播放，只有在录音时才会播放。

- 主界面控件：
    - main_widget：包含主要功能的控件，设置背景颜色。
    - label：显示可识别的语音命令提示信息。
    - language_label和language_combobox：用于选择识别语音的语言。
    - button：用于启动语音识别的按钮。
    - status_label：显示当前状态信息。
    - copyright_label：显示版权信息。
#### RecognizeThread 类
- 线程类：继承自QThread，用于处理语音识别的后台任务，避免阻塞主线程。
- 信号机制：使用pyqtSignal传递识别完成后的结果

### 主要流程
1. 启动应用：用户启动应用，主窗口显示并初始化UI。
2. 选择语言：用户从下拉菜单中选择语音识别的语言（中文或英文）。
3. 开始识别：
    - 用户点击“开始识别 (Start Recognition)”按钮。
    - 应用程序更新状态为“正在录音... (Recording...)”。
    - 动态背景GIF开始播放，定时5秒后停止。
    - 创建并启动RecognizeThread线程，进行语音识别。
4. 识别完成：
    - RecognizeThread线程完成识别后，发出信号recognition_complete，传递识别结果。
    - 主界面显示识别文本和执行结果，并通过对话框提示用户。
    - 状态更新为“等待命令... (Waiting for command...)”。
### 样式设置
应用程序通过设置QSS样式表来美化UI组件，包括按钮、下拉菜单和标签。

#### 主要样式
- QMainWindow：设置背景颜色为深蓝色。
- QPushButton：设置字体大小、背景颜色、文字颜色、边距和圆角效果。鼠标悬停时背景颜色变深。
- QComboBox：设置字体大小、边距、最小高度和宽度。

### 如何运行
1. 确保已经安装PyQt5依赖库。
2. 将所有代码和资源文件（例如background.gif）放在同一目录下。
3. 运行gui.py