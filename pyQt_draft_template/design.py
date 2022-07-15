# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QApplication, QStyle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Вспомогательный помощник GUI")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setWindowIcon(QtGui.QIcon('main.png'))

        # MainWindow.setWindowTitle('Вспомогательный помощник GUI')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 580, 350))
        # self.centralwidget.setStyleSheet("QWidget {  background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d8d0d0, stop: 1 #726d6d) }"
        #                                  "QWidget {border-radius: 10px}"
        #                                  "QWidget {border-color: beige}")   ##
        # self.tabWidget.setStyleSheet("QWidget {  background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #a5a0a0, stop: 1 #726d6d) }")   ##
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tab1.setFont(font)
        self.tab1.setObjectName("tab1")
        self.tabWidget.setStyleSheet("QTabBar::tab:hover {background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e1e814, stop: 1 #ecf409)}"
                                     "QTabBar::tab:hover {border: 2px solid black}"
                                     "QTabBar::tab:selected {background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88cae0, stop: 1 #4ec5ed)}")

        self.pushButton = QtWidgets.QPushButton(self.tab1)
        self.pushButton.setGeometry(QtCore.QRect(30, 260, 130, 50))

        self.pushButton.setStyleSheet("QPushButton { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f79e18, stop: 1 #f77118) }"
                                      "QPushButton {border-style: outset}"
                                      "QPushButton {border-width: 2px}"
                                      "QPushButton {border-radius: 10px}"
                                      "QPushButton {border-color: beige}"
                                      "QPushButton {font: bold 20px}"
                                      "QPushButton {min-width: 10em}"
                                      "QPushButton {padding: 6px}"
                                      "QPushButton:hover { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e1e814, stop: 1 #ecf409) }"
                                      "QPushButton:hover {border-color: black}"
                                      "QPushButton:pressed { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f7383c, stop: 1 #f4090d) }")
        self.pushButtonWB = QtWidgets.QPushButton(self.tab1)
        self.pushButtonWB.setGeometry(QtCore.QRect(300, 260, 130, 50))
        self.pushButtonWB.setStatusTip("Запустить Workbench 2019 R2")


        self.pushButtonWB.setStyleSheet(
            "QPushButton { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f79e18, stop: 1 #f77118) }"
            "QPushButton {border-style: outset}"
            "QPushButton {border-width: 2px}"
            "QPushButton {border-radius: 10px}"
            "QPushButton {border-color: beige}"
            "QPushButton {font: bold 20px}"
            "QPushButton {min-width: 10em}"
            "QPushButton {padding: 6px}"
            "QPushButton:hover { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e1e814, stop: 1 #ecf409) }"
            "QPushButton:hover {border-color: black}"
            "QPushButton:pressed { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f7383c, stop: 1 #f4090d) }")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStatusTip("Запустить SpaceClaim 2019 R2")
        self.label = QtWidgets.QLabel(self.tab1)

        self.label.setGeometry(QtCore.QRect(10, 10, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # self.label.setStyleSheet(
        #     "QLabel {  background: white }")  ##
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 260, 130, 50))
        self.pushButton_2.setStyleSheet(
            "QPushButton {background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f79e18, stop: 1 #f77118) }"
            "QPushButton {border-style: outset}"
            "QPushButton {border-width: 2px}"
            "QPushButton {border-radius: 10px}"
            "QPushButton {border-color: beige}"
            "QPushButton {font: bold 20px}"
            "QPushButton {min-width: 10em}"
            "QPushButton {padding: 6px}"
            "QPushButton:hover { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e1e814, stop: 1 #ecf409) }"
            "QPushButton:hover {border-color: black}"
            "QPushButton:pressed { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f7383c, stop: 1 #f4090d) }")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.tab2)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 550, 200))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab2)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 260, 130, 50))
        self.pushButton_3.setStyleSheet(
            "QPushButton { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f79e18, stop: 1 #f77118) }"
            "QPushButton {border-style: outset}"
            "QPushButton {border-width: 2px}"
            "QPushButton {border-radius: 10px}"
            "QPushButton {border-color: beige}"
            "QPushButton {font: bold 20px}"
            "QPushButton {min-width: 10em}"
            "QPushButton {padding: 6px}"
            "QPushButton:hover { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e1e814, stop: 1 #ecf409) }"
            "QPushButton:hover {border-color: black}"
            "QPushButton:pressed { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f7383c, stop: 1 #f4090d) }")
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI Semibold")
        # font.setPointSize(14)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.tab2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 471, 30))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")

        self.pushButton_4 = QtWidgets.QPushButton(self.tab3)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 260, 130, 50))
        self.pushButton_4.setStyleSheet(
            "QPushButton { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f79e18, stop: 1 #f77118) }"
            "QPushButton {border-style: outset}"
            "QPushButton {border-width: 2px}"
            "QPushButton {border-radius: 10px}"
            "QPushButton {border-color: beige}"
            "QPushButton {font: bold 20px}"
            "QPushButton {min-width: 10em}"
            "QPushButton {padding: 6px}"
            "QPushButton:hover { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e1e814, stop: 1 #ecf409) }"
            "QPushButton:hover {border-color: black}"
            "QPushButton:pressed { background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f7383c, stop: 1 #f4090d) }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.tab3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 381, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.tabWidget.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        style = QApplication.instance().style()
        icon_about = style.standardIcon(QStyle.SP_DialogHelpButton)
        icon_stop = style.standardIcon(QStyle.SP_BrowserStop)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        bar = self.menubar.addMenu('Меню')
        about = self.menubar.addMenu('Помощь')

        exitAction = QAction(icon_stop, 'Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выйти из приложения')
        exitAction.triggered.connect(self.close)
        bar.addAction(exitAction)

        aboutAction = QAction(icon_about, 'О программе', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.setStatusTip('Посмотреть информацию о программе')
        aboutAction.triggered.connect(self.showDialog)
        about.addAction(aboutAction)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        # self.statusBar.showMessage('ready')
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OptiWidget"))
        # MainWindow.setWindowIcon(QIcon('main.png'))
        self.pushButton.setText(_translate("MainWindow", "Запуск SCDM"))
        self.label.setText(_translate("MainWindow", "Запуск ANSYS Workbench"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Шаг 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать файлы"))
        self.pushButton_3.setText(_translate("MainWindow", "Преобразовать"))
        self.label_2.setText(_translate("MainWindow", "Переформатирование файлов к нужному порядку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Шаг 2"))
        self.pushButton_4.setText(_translate("MainWindow", "Завершить"))
        self.label_3.setText(_translate("MainWindow", "Формирование точек Чебышева"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Шаг 3"))
        self.pushButtonWB.setText(_translate("MainWindow", "Запуск WB"))

