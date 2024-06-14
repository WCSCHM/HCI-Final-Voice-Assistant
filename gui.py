import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QGridLayout, QWidget, QComboBox, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QMovie, QPalette, QColor
from app import process_command

class RecognizeThread(QThread):
    recognition_complete = pyqtSignal(str, dict)

    def __init__(self, duration, language):
        super().__init__()
        self.duration = duration
        self.language = language

    def run(self):
        text, result = process_command(duration=self.duration, language=self.language)
        self.recognition_complete.emit(text, result)

class VoiceAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle('语音助手 (Voice Assistant)')
        self.setFixedSize(660, 1200)  # 固定窗口大小

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        gif_path = os.path.join(cur_dir, "background.gif")

        # 创建用于显示 GIF 动画的 QLabel
        self.bg_label = QLabel(self)
        self.bg_label.setFixedSize(660, 387)
        self.bg_label.setAlignment(Qt.AlignCenter)
        self.bg_label.setScaledContents(True)  # 确保 GIF 动画缩放以填满整个窗口

        self.background = QMovie(gif_path)
        self.bg_label.setMovie(self.background)
        self.background.start()
        self.background.stop()  # 默认不播放动画

        # 创建主界面控件
        main_widget = QWidget(self)
        main_widget.setFixedSize(660, 813)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor("#00007c"))
        main_widget.setAutoFillBackground(True)
        main_widget.setPalette(palette)

        main_layout = QGridLayout(main_widget)

        self.label = QLabel('你可以说(You can say):\n    打开摄像头(open camera)\n    打开音乐播放器(open music player)\n    打开记事本(open notepad)\n    搜索xxx(search xxx)', self)
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setFont(QFont('Simsun', 14))
        self.label.setStyleSheet("font-weight: bold; color: white;")
        main_layout.addWidget(self.label, 0, 0, 1, 2)
        
        self.language_label = QLabel('选择语言 (Select Language):', self)
        self.language_label.setFont(QFont('Simsun', 15))
        self.language_label.setStyleSheet("font-weight: bold; color: white;")
        main_layout.addWidget(self.language_label, 1, 0)

        self.language_combobox = QComboBox(self)
        self.language_combobox.addItems(['zh', 'en'])
        main_layout.addWidget(self.language_combobox, 1, 1)

        self.button = QPushButton('开始识别 (Start Recognition)', self)
        self.button.clicked.connect(self.start_recognition)
        self.button.setStyleSheet("font-weight:bold;")
        main_layout.setAlignment(self.button, Qt.AlignHCenter)
        main_layout.addWidget(self.button, 2, 0, 1, 2, alignment=Qt.AlignCenter)

        self.status_label = QLabel('等待命令... (Waiting for command...)', self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont('Simsun', 13))
        self.status_label.setStyleSheet("font-weight:bold; color: white;")
        main_layout.addWidget(self.status_label, 3, 0, 1, 2)

        self.copyright_label = QLabel('同济大学软件学院 2253333王沫涵 2250695奥泉瑞 2251931王紫东', self)
        self.copyright_label.setAlignment(Qt.AlignCenter)
        self.copyright_label.setFont(QFont('KaiTi', 10))
        self.copyright_label.setStyleSheet("color: white;")
        main_layout.addWidget(self.copyright_label, 4, 0, 1, 2)

        layout.addWidget(self.bg_label)
        layout.addWidget(main_widget)

        self.setStyleSheet("""
            QMainWindow {
                 background-color: #00007c          
            }
            QPushButton {
                font-size: 25px;
                background-color: #007bff;
                color: white;
                padding: 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QComboBox {
                font-size: 23px;
                padding: 3px;
                min-height: 40px;
                min-width: 150px;
            }
        """)

    def start_recognition(self):
        duration = 5
        language = self.language_combobox.currentText()
        self.update_status("正在录音... (Recording...)")
        self.background.start()
        QTimer.singleShot(5000, self.background.stop)
        self.recognize_thread = RecognizeThread(duration, language)
        self.recognize_thread.recognition_complete.connect(self.show_result)
        self.recognize_thread.start()

    def show_result(self, text, result):
        result_text = f"识别文本: {text} (Recognized text: {text})\n执行结果: {result['status']} (Execution result: {result['status']})"
        QMessageBox.information(self, "语音助手 (Voice Assistant)", result_text)
        self.update_status("等待命令... (Waiting for command...)")

    def update_status(self, message):
        self.status_label.setText(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VoiceAssistant()
    ex.show()
    sys.exit(app.exec_())
