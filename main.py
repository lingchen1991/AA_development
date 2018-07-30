from PyQt5 import QtWidgets
from demo import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from DataLoading import *

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def loadSingle(self):
        print("Loading dicoms")
        folder_name = QFileDialog.getExistingDirectory(self, '读取')
        if folder_name:
            self.images = readSingle(folder_name)
            print("DICOM reading is completed")

    def loadAll(self):
        print("Loading dicoms")
        folder_name = QFileDialog.getExistingDirectory(self, '读取')
        if folder_name:
            self.images = readAll(folder_name)
            print("DICOM reading is completed")

    def loadROI(self):
        folder_name = QFileDialog.getExistingDirectory(self, '读取')
        if folder_name:
            self.labels = readROI(folder_name)
            print("ROI reading is completed")

    def loadCSV(self):
        file_name, ok = QFileDialog.getOpenFileName(self, '读取', './')

    def save(self):
        write(self.df)
        #file_name, ok = QFileDialog.getSaveFileName(self, '读取', '/home')
        #if ok:
            #_f = open(file_name, 'w')
            #_f.write(str(self.plainTextEdit.toPlainText()))

    def segment(self):
        return 0

    def calculate(self):
        self.df = extract(self.images, self.labels)
        print("Features extraction is completed")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())