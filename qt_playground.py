from map_drawer import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import QFile, pyqtSlot


# from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton
        self.ui.pushButton.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.ui.lineEdit.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.ui.lineEdit_2.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

# from PyQt5 import QtWidgets # import PyQt5 widgets
# import sys
#
# # Create the application object
# app = QtWidgets.QApplication(sys.argv)
#
# # Create the form object
# first_window = QtWidgets.QWidget()
#
# # Set window size
# first_window.resize(400, 300)
#
# # Set the form title
# first_window.setWindowTitle("The first pyqt program")
#
# # Show form
# first_window.show()
#
# # Run the program
# sys.exit(app.exec())
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPalette
# from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox
#
# # app = QApplication([])
#
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#
#
# class App(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 textbox - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 400
#         self.height = 140
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         # Create textbox
#         self.textbox = QLineEdit(self)
#         self.textbox.move(20, 20)
#         self.textbox.resize(280, 40)
#
#         # Create a button in the window
#         self.button = QPushButton('Show text', self)
#         self.button.move(20, 80)
#
#         # connect button to function on_click
#         self.button.clicked.connect(self.on_click)
#         self.show()
#
#     @pyqtSlot()
#     def on_click(self):
#         textboxValue = self.textbox.text()
#         QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
#                              QMessageBox.Ok)
#         self.textbox.setText("")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
#
# # app.setStyle('Fusion')
# # palette = QPalette()
# # palette.setColor(QPalette.ButtonText, Qt.blue)
# # app.setPalette(palette)
# # button = QPushButton('Click')
# #
# #
# # def on_button_clicked():
# #     alert = QMessageBox()
# #     alert.setText('Button Click was clicked')
# #     alert.exec_()
# #
# #
# # button.clicked.connect(on_button_clicked)
# # button.show()
# # app.exec_()
# #
