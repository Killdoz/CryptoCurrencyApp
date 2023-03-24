


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 541, 681))
        self.frame.setStyleSheet("background-color: #2BA4FB;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 30, 361, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 100, 71, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images\eth.png"))
        self.label_3.setObjectName("label_3")
        self.amount_of_money = QtWidgets.QLineEdit(self.frame)
        self.amount_of_money.setGeometry(QtCore.QRect(30, 230, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.amount_of_money.setFont(font)
        self.amount_of_money.setStyleSheet("border-color: white;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.amount_of_money.setText("")
        self.amount_of_money.setAlignment(QtCore.Qt.AlignCenter)
        self.amount_of_money.setObjectName("amount_of_money")
        self.cur = QtWidgets.QLineEdit(self.frame)
        self.cur.setGeometry(QtCore.QRect(30, 290, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cur.setFont(font)
        self.cur.setStyleSheet("border-color: white;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.cur.setText("")
        self.cur.setAlignment(QtCore.Qt.AlignCenter)
        self.cur.setObjectName("cur")
        self.result = QtWidgets.QLineEdit(self.frame)
        self.result.setGeometry(QtCore.QRect(30, 410, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("border-color: white;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.cryptocur = QtWidgets.QLineEdit(self.frame)
        self.cryptocur.setGeometry(QtCore.QRect(30, 350, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cryptocur.setFont(font)
        self.cryptocur.setStyleSheet("border-color: white;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.cryptocur.setText("")
        self.cryptocur.setAlignment(QtCore.Qt.AlignCenter)
        self.cryptocur.setObjectName("cryptocur")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 470, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: white;\n"
"\n"
"QPushButton::pressed{\n"
"color: #72C2FB;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(480, 320, 55, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images\strilky.png"))
        self.label_2.setObjectName("label_2")
        self.pominyaty = QtWidgets.QPushButton(self.frame)
        self.pominyaty.setGeometry(QtCore.QRect(480, 330, 61, 51))
        self.pominyaty.setStyleSheet("color: rgba(255, 255, 255,0);\n"
"background-color: rgba(255, 255, 255,0);")
        self.pominyaty.setObjectName("pominyaty")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(390, 350, 81, 51))
        self.listWidget.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"color: white;")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(390, 290, 81, 51))
        self.listWidget_2.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"color: white;")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CryptoConverter"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))
        self.pominyaty.setText(_translate("MainWindow", "PushButton"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "BTC"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "ETH"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "LTC"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "XRP"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "QNT"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "SOL"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "DOGE"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "USD"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "EUR"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "GBP"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "UAH"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "RUB"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
