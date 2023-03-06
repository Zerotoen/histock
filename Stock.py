from selenium import webdriver
from selenium.webdriver.common.by import By
from mainwindow import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore

#self.scroll_value = self.listWidget.verticalScrollBar.value()
#self.listWidget.verticalScrollBar().setValue(self.scrollbar_value)

class MainWindow_controller(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.histock=Histock()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listwidget = self.ui.listWidget
        self.ui.Global_Button.clicked.connect(self.Global_on_click)
        self.ui.Asia_Button.clicked.connect(self.Asia_on_click)
        self.ui.America_Button.clicked.connect(self.America_on_click)
        self.ui.Europe_Button.clicked.connect(self.Europe_on_click)
        self.ui.National_debt_Button.clicked.connect(self.National_debt_on_click)
        self.ui.Virtual_currency_Button.clicked.connect(self.Virtual_currency_on_click)
        self.ui.Taiwan_Button.clicked.connect(self.Taiwan_on_click)
        self.current_active = None
        self.line='-'*106
        self.additem1='{:^20}{:^20}{:^20}{:^20}{:^20}'.format('名稱','價格','漲跌','比例','時間')
        
    def Global_on_click(self):
        stocklist = self.histock.Global_stock()#將要顯示的容器回傳，要加工在表格的函式處理
        self.listwidget.clear()
        itemtext1 = QtWidgets.QListWidgetItem(self.additem1)
        itemtext1.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listwidget.addItem(itemtext1)
        for items in stocklist:
            for item in items:
                name, price, change, percent, time = item.split(' ')
                stockitem ="{:^18}|{:^18}|{:^18}|{:^18}|{:^18}".format(name, price, change, percent, time)
                itemtext2 = QtWidgets.QListWidgetItem(stockitem)
                itemtext2.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext2)
                itemtext3 = QtWidgets.QListWidgetItem(self.line)
                itemtext3.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext3)
                QtWidgets.QApplication.processEvents()
                
    def Asia_on_click(self):
        stocklist = self.histock.Asia_stock()
        self.listwidget.clear()
        itemtext1 = QtWidgets.QListWidgetItem(self.additem1)
        itemtext1.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listwidget.addItem(itemtext1)
        for items in stocklist:
            for item in items:
                name, price, change, percent, time = item.split(' ')
                stockitem ="{:^18}|{:^18}|{:^18}|{:^18}|{:^18}".format(name, price, change, percent, time)
                itemtext2 = QtWidgets.QListWidgetItem(stockitem)
                itemtext2.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext2)
                itemtext3 = QtWidgets.QListWidgetItem(self.line)
                itemtext3.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext3)
                QtWidgets.QApplication.processEvents()
                
    def America_on_click(self):
        stocklist = self.histock.America_stock()
        self.listwidget.clear()
        itemtext1 = QtWidgets.QListWidgetItem(self.additem1)
        itemtext1.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listwidget.addItem(itemtext1)
        for items in stocklist:
            for item in items:
                name, price, change, percent, time = item.split(' ')
                stockitem ="{:^18}|{:^18}|{:^18}|{:^18}|{:^18}".format(name, price, change, percent, time)
                itemtext2 = QtWidgets.QListWidgetItem(stockitem)
                itemtext2.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext2)
                itemtext3 = QtWidgets.QListWidgetItem(self.line)
                itemtext3.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext3)
                QtWidgets.QApplication.processEvents()
                
    def Europe_on_click(self):
        stocklist = self.histock.Europe_stock()
        self.listwidget.clear()
        itemtext1 = QtWidgets.QListWidgetItem(self.additem1)
        itemtext1.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listwidget.addItem(itemtext1)
        for items in stocklist:
            for item in items:
                name, price, change, percent, time = item.split(' ')
                stockitem ="{:^18}|{:^18}|{:^18}|{:^18}|{:^18}".format(name, price, change, percent, time)
                itemtext2 = QtWidgets.QListWidgetItem(stockitem)
                itemtext2.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext2)
                itemtext3 = QtWidgets.QListWidgetItem(self.line)
                itemtext3.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext3)
                QtWidgets.QApplication.processEvents()
                
    def National_debt_on_click(self):
        stocklist = self.histock.National_debt()
        self.listwidget.clear()
        itemtext1 = QtWidgets.QListWidgetItem(self.additem1)
        itemtext1.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listwidget.addItem(itemtext1)
        for items in stocklist:
            for item in items:
                name, price, change, percent, time = item.split(' ')
                stockitem ="{:^18}|{:^18}|{:^18}|{:^18}|{:^18}".format(name, price, change, percent, time)
                itemtext2 = QtWidgets.QListWidgetItem(stockitem)
                itemtext2.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext2)
                itemtext3 = QtWidgets.QListWidgetItem(self.line)
                itemtext3.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext3)
                QtWidgets.QApplication.processEvents()
                
    def Virtual_currency_on_click(self):
        stocklist = self.histock.Virtual_currency()
        self.listwidget.clear()
        itemtext1 = QtWidgets.QListWidgetItem(self.additem1)
        itemtext1.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listwidget.addItem(itemtext1)
        for items in stocklist:
            for item in items:
                name, price, change, percent, time = item.split(' ')
                stockitem="{:^18}|{:^18}|{:^18}|{:^18}|{:^18}".format(name, price, change, percent, time)
                itemtext2 = QtWidgets.QListWidgetItem(stockitem)
                itemtext2.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext2)
                itemtext3 = QtWidgets.QListWidgetItem(self.line)
                itemtext3.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.listwidget.addItem(itemtext3)
                QtWidgets.QApplication.processEvents()
                
    def Taiwan_on_click(self):
        stocklist = self.histock.Taiwan_stock()
        self.listwidget.clear()
        self.additem1='{:^20}{:^20}{:^20}{:^20}{:^20}'.format('名稱','價格','漲跌','比例','振幅')
        itemtext1 = QtWidgets.QListWidgetItem(self.additem1)
        itemtext1.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.listwidget.addItem(itemtext1)
        for item in stocklist:
            name, price, change, percent, time = item.split(' ')
            stockitem="{:^18}|{:^18}|{:^18}|{:^18}|{:^18}".format(name, price, change, percent, time)
            itemtext2 = QtWidgets.QListWidgetItem(stockitem)
            itemtext2.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            self.listwidget.addItem(itemtext2)
            itemtext3 = QtWidgets.QListWidgetItem(self.line)
            itemtext3.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            self.listwidget.addItem(itemtext3)
            QtWidgets.QApplication.processEvents()
                
class Histock():
    
    def __init__(self):
        super().__init__()
        self.url='https://histock.tw/index'
        self.oP=webdriver.ChromeOptions()
        self.oP.add_argument("headless")
        self.web=webdriver.Chrome(options=self.oP)
        self.web.implicitly_wait(10)
        self.web.get(self.url)
        self.stocks=[]
    def Global_stock(self):
        self.web.find_element(By.XPATH,'//*[@id="headTabGlobal"]/a').click()
        main = self.web.find_element(By.CLASS_NAME,'main')
        items=main.find_element(By.ID,'id1')
        self.stocks.clear()
        
        for item in items.find_elements(By.CLASS_NAME,'index-list'):
            stock = item.text.replace('名稱 價格 漲跌 比例 時間', '').strip()
            self.stocks.append(stock.split('\n'))
            
        return self.stocks
            
    def Asia_stock(self):
        self.web.find_element(By.XPATH,'//*[@id="headTabGlobal"]/a').click()
        main=self.web.find_element(By.CLASS_NAME,'main')
        items=main.find_element(By.XPATH,'//*[@id="id4"]/div/table')
        stock = items.text.replace('名稱 價格 漲跌 比例 時間', '').strip()
        self.stocks.clear()
        self.stocks.append(stock.split('\n'))
        
        return self.stocks
    
    def America_stock(self):
        self.web.find_element(By.XPATH,'//*[@id="headTabGlobal"]/a').click()
        main=self.web.find_element(By.CLASS_NAME,'main')
        items=main.find_element(By.XPATH,'//*[@id="id2"]/div[1]/div/table')
        stock = items.text.replace('名稱 價格 漲跌 比例 時間', '').strip()
        self.stocks.clear()
        self.stocks.append(stock.split('\n'))
        
        return self.stocks
        
    def Europe_stock(self):
        self.web.find_element(By.XPATH,'//*[@id="headTabGlobal"]/a').click()
        main=self.web.find_element(By.CLASS_NAME,'main')
        items=main.find_element(By.XPATH,'//*[@id="id3"]/div/table')
        stock = items.text.replace('名稱 價格 漲跌 比例 時間', '').strip()
        self.stocks.clear()
        self.stocks.append(stock.split('\n'))
        
        return self.stocks
        
    def National_debt(self):
        self.web.find_element(By.XPATH,'//*[@id="headTabGlobal"]/a').click()
        main=self.web.find_element(By.CLASS_NAME,'main')
        items=main.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[2]/div[6]')
        self.stocks.clear()
        for item in items.find_elements(By.CLASS_NAME,'index-list'):
            stock = item.text.replace('名稱 價格 漲跌 比例 時間', '').strip()
            self.stocks.append(stock.split('\n'))
            
        return self.stocks
    
    def Virtual_currency(self):
        self.web.find_element(By.XPATH,'//*[@id="headTabGlobal"]/a').click()
        main=self.web.find_element(By.CLASS_NAME,'main')
        items=main.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[2]/div[8]/div[2]/div[1]')
        stock = items.text.replace('名稱 價格 漲跌 比例 時間', '').strip()
        self.stocks.clear()
        self.stocks.append(stock.split('\n'))
        
        return self.stocks
        
    def Taiwan_stock(self):
        self.web.find_element(By.XPATH,'//*[@id="headTabStock"]/a').click()
        self.web.find_element(By.PARTIAL_LINK_TEXT,'排行').click()
        
        main=self.web.find_element(By.CLASS_NAME,'grid')
        items=main.find_element(By.CLASS_NAME,'gvTB')
        self.stocks=[]
        for item in items.find_elements(By.CLASS_NAME,'alt-row'):
            item=item.text.split(' ')
            item=item[1]+' '+item[2]+' '+item[3]+' '+item[4]+' '+item[6]
            self.stocks.append(item)
            
        return self.stocks       
    
    def Close(self):
        self.web.close()
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec())    
    
    
    
    
    
    