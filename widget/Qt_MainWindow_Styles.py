import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    # 自定义窗口类
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # 设置窗口标志（无边框）
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 为便于显示，设置窗口背景颜色
