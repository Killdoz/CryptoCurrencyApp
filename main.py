import requests
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from uix import Ui_MainWindow

class CryptoConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CryptoConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('CryptoConverter') 
        self.setWindowIcon(QIcon('images\icon.png'))
        self.ui.amount_of_money.setPlaceholderText('Amount of money')
        self.ui.cryptocur.setPlaceholderText('Set crypto')
        self.ui.cur.setPlaceholderText('Set currency')
        self.ui.result.setPlaceholderText('Result')
        self.ui.result.setReadOnly(True)
        self.ui.listWidget.move(390,350)
        self.ui.listWidget_2.move(390, 290)
        self.ui.listWidget.disconnect()
        self.ui.listWidget_2.disconnect()
        self.ui.pushButton.clicked.connect(self.converter)
        self.ui.pominyaty.clicked.connect(self.zmina)
        self.ui.listWidget_2.clicked.connect(self.listy2)
        self.ui.listWidget.clicked.connect(self.listy)

    def converter(self):
        cryptc = self.ui.cur.text()
        cur = self.ui.cryptocur.text()
        cryptc = cryptc.upper()
        cur = cur.upper()
        url = f'https://min-api.cryptocompare.com/data/price?fsym={cryptc}&tsyms={cur}&RelaxedValidation=True'
        page = requests.get(url)
        data = page.json()
        numcur = data[cur]
        am = int(self.ui.amount_of_money.text())
        res = am * numcur
        self.ui.result.setText(str(res))

    def zmina(self):
        self.ui.listWidget.disconnect()
        self.ui.listWidget_2.disconnect()
        self.ui.cryptocur.setPlaceholderText('Set currency')
        self.ui.cur.setPlaceholderText('Set crypto')
        self.ui.listWidget.move(390,290)
        self.ui.listWidget_2.move(390, 350)
        self.ui.listWidget.clicked.connect(self.listy4)
        self.ui.listWidget_2.clicked.connect(self.listy3)
        self.ui.pominyaty.clicked.connect(self.init_UI)
        
    def listy2(self):
        item_cur = str(self.ui.listWidget_2.currentItem().text())

        self.ui.cur.setText(item_cur)
        
    def listy(self):
        item_cr = str(self.ui.listWidget.currentItem().text())

        self.ui.cryptocur.setText(item_cr)
      
    def listy3(self):
        item_cur = str(self.ui.listWidget_2.currentItem().text())

        self.ui.cryptocur.setText(item_cur)

    def listy4(self):
        item_cr = str(self.ui.listWidget.currentItem().text())

        self.ui.cur.setText(item_cr)
app = QtWidgets.QApplication([])
application = CryptoConv()
application.show()

sys.exit(app.exec())