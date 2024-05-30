import sys  
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QStatusBar, QDialog, QPushButton, QMessageBox
from PyQt5.uic.properties import QtGui

import design  
import subprocess
import os
import matplotlib.pyplot as plt


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.pushButton.clicked.connect(self.launch_scdm)
        self.pushButtonWB.clicked.connect(self.launch_wb)
        self.pushButton_2.clicked.connect(self.browse)
        self.pushButton_4.clicked.connect(self.graph)

    def launch_wb(self):
        program = r'C:\Program Files\ANSYS Inc\v194\Framework\bin\Win64\runwb2.exe'
        subprocess.Popen(program)

    def launch_scdm(self):
        program = r'C:\Program Files\ANSYS Inc\v194\SCDM\SpaceClaim.exe'
        subprocess.Popen(program)

    def browse(self):
        self.listWidget.clear()  
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose a folder")

        if directory:  
            for file_name in os.listdir(directory):  
                if file_name.endswith(".txt"):
                    self.listWidget.addItem(file_name)  

    def buttonClicked1(self):
        self.pushButton.setText('Run 1!')

    def buttonClicked2(self):
        self.pushButtonWB.setText('Run 2!')


    def graph(self):
        x = [1, 2, 3, 4]
        y = [2, 4, 12, 1]
        plt.plot(x, y, 'r^--')
        plt.title('Graph...', fontsize=18)
        plt.grid()
        plt.show()

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowIcon(QIcon('about.png'))
        msgBox.setText("OptiWidget\n "+"\N{COPYRIGHT SIGN}"+"\n2020")
        msgBox.setWindowTitle("About")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show()  
    app.exec_()  


if __name__ == '__main__':  
    main()  
