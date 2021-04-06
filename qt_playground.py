import os
from pathlib import Path

from PyQt5.QtGui import QPixmap

from map_drawer import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QGraphicsPixmapItem, QGraphicsScene, \
    QFileDialog
from PyQt5.QtCore import QFile, pyqtSlot

# from ui_mainwindow import Ui_MainWindow
from rectangle_area import get_image


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_click)
        self.ui.pushButtonSetPath.clicked.connect(self.on_click_set_path)
        self.show()

    def set_filename(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Image", str(Path.home()), "Image Files (*.png *.jpg *.bmp)")

    def draw_image(self, image_path):
        pix = QPixmap(image_path)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        self.ui.graphicsViewMapCanvas.setScene(scene)

    @pyqtSlot()
    def on_click(self):
        textbox_value_lon_left = float(self.ui.lineEdit.text())
        textbox_value_lon_right = float(self.ui.lineEdit_2.text())
        textbox_value_lat_up = float(self.ui.lineEdit_3.text())
        textbox_value_lat_down = float(self.ui.lineEdit_4.text())
        get_image(textbox_value_lat_down, textbox_value_lon_left, textbox_value_lat_up, textbox_value_lon_right)
        self.draw_image('rectangle_area_map.png')
        # get_image(49.4750, 15.8611, 49.5005, 15.9178)
        QMessageBox.question(self, 'File save', 'The file was saved',
                             QMessageBox.Ok,
                             QMessageBox.Ok)

    @pyqtSlot()
    def on_click_set_path(self):
        self.set_filename()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
