import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from AndroidEdit import Ui_MainWindow
from Util.JsonUtils import JsonUtil


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, clip, parent=None):
        super(MainWindow, self).__init__(parent)
        self.clip = clip
        self.setupUi(self)
        self.code = -1
        self.initView()

    @pyqtSlot(bool)
    def on_btn_open_clicked(self, checked):
        self.filename = ".\Qtui\shared.jpg"
        if len(self.filename):
            self.image = QImage(self.filename)
            self.label.setPixmap(QPixmap.fromImage(self.image))
            self.label.setFixedWidth(self.image.width())
            self.label.setFixedHeight(self.image.height())

    def getEditContent(self):
        json = self.textEdit.toPlainText()
        code = self.jsonUtil.format(str=json)
        if (code == 1):
            self.label_2.setText("正确的json")
            self.label.setText("小鱼是个正确的小胖子")
            self.code = 1

        else:
            self.label_2.setText("错误的json")
            self.label.setText("小鱼是个错误的小胖子")
            self.code = -1
        self.textEdit.setText(self.jsonUtil.str)

    def getAndroidJson(self):
        self.getEditContent()
        if (self.code == -1):
            return
        jsonCode = self.textEdit.toPlainText()
        str = self.jsonUtil.formatAndroid(str=jsonCode)
        self.textEdit_2.setText(str)
        self.copyText(str)

    def copyText(self, text):
        try:
            self.clip.setText(text)
        except Exception as e:
            print(e)

    def clearString(self):
        self.textEdit_2.setText("")
        self.textEdit.setText("")

    def initView(self):
        self.filename = ".\img\shared.jpg"
        if len(self.filename):
            self.image = QImage(self.filename)
            self.label_3.setPixmap(QPixmap.fromImage(self.image))
            self.label_3.setFixedWidth(self.image.width())
            self.label_3.setFixedHeight(self.image.height())
        self.label.setText("小鱼是个小胖子")
        self.pushButton.clicked.connect(self.getEditContent)
        self.pushButton_android.clicked.connect(self.getAndroidJson)
        self.pushButton_clear.clicked.connect(self.clearString)
        self.jsonUtil = JsonUtil()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clipboard = app.clipboard()
    mainWndow = MainWindow(clip=clipboard)
    mainWndow.show()
    sys.exit(app.exec_())
