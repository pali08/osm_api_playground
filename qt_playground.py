from map_drawer import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import QFile, pyqtSlot

# from ui_mainwindow import Ui_MainWindow
from rectangle_area import get_image


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton
        self.ui.pushButton.clicked.connect(self.on_click)
        self.show()

    # @pyqtSlot()
    def on_click(self):
        textbox_value_lon_left = float(self.ui.lineEdit.text())
        textbox_value_lon_right = float(self.ui.lineEdit_2.text())
        textbox_value_lat_up = float(self.ui.lineEdit_3.text())
        textbox_value_lat_down = float(self.ui.lineEdit_4.text())
        print(textbox_value_lat_down)
        print(textbox_value_lat_up)
        print(textbox_value_lon_right)
        print(textbox_value_lon_left)
        get_image(textbox_value_lat_down, textbox_value_lon_left, textbox_value_lat_up, textbox_value_lon_right)
        # get_image(49.4750, 15.8611, 49.5005, 15.9178)
        QMessageBox.question(self, 'File save', 'The file was saved',
                             QMessageBox.Ok,
                             QMessageBox.Ok)
        # self.ui.lineEdit_2.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
