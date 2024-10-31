import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import whatsapp_msg_sender

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.button1 = QPushButton("Whatsapp", self)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.button1)

        self.setLayout(self.layout)
        self.show()

        self.button1.clicked.connect(self.on_button1)

    @pyqtSlot()
    def on_button1(self):
        print("Starting...")
        whatsapp_msg_sender.Tool().Start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())