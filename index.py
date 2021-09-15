from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')






class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()

        self.Show_Author()
        self.Show_Category()
        self.Show_Publisher()
        
        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()


        self.Show_All_Books()

    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)
        self.pushButton_7.clicked.connect(self.Add_New_Book)

        self.pushButton_14.clicked.connect(self.Add_Category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)
        self.pushButton_7.clicked.connect(self.Add_New_Book)



    def Show_Themes(self):
        self.groupBox_4.show()

    def Hiding_Themes(self):
        self.groupBox_4.hide()

# ==============================================================
# ======================= Opening Tabs =============================

    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)
    
    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)


# ==============================================================
# ======================= Save Books =============================
    def Show_All_Books(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)

        self.db.close()


    def Add_New_Book(self):

        self.db = MySQLdb.connect(host='localhost',user="root", password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.plainTextEdit.toPlainText()
        book_code = self.lineEdit_4.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_3.text()

        self.cur.execute('''
            INSERT INTO book (book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
            VALUES (%s , %s , %s , %s , %s , %s , %s)
        ''' ,(book_title , book_description , book_code , book_category , book_author , book_publisher , book_price))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_2.setText('')
        self.plainTextEdit.setPlainText('')
        self.lineEdit_4.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_3.setText('')
        self.Show_All_Books()




    def Search_Book(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass


# ==============================================================
# ======================= Users =============================

    def Add_New_User(self):
        pass

    def Login(self):
        pass

    def Edit_User(self):
        pass

# ==============================================================
# ======================= Category =============================

    def Add_Category(self):

        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_21.text()
        self.cur.execute('''
        INSERT INTO category (category_name)  VALUES (%s)
        ''' , (category_name,))
        
        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.lineEdit_21.setText('')
        self.Show_Category()
     

    def Show_Category(self):
        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category''')
        data = self.cur.fetchall()
        
        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)


    def Add_Author(self):

        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_22.text()
        self.cur.execute('''
        INSERT INTO authors (author_name)  VALUES (%s)
        ''' , (author_name,))
        
        self.db.commit()
        self.lineEdit_22.setText('')
        self.statusBar().showMessage('New Author Added')
        self.Show_Author()

    def Show_Author(self):
        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors''')
        data = self.cur.fetchall()
      
        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def Add_Publisher(self):
        
        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_23.text()
        self.cur.execute('''
        INSERT INTO publisher (publisher_name)  VALUES (%s)
        ''' , (publisher_name,))
        
        self.db.commit()
        self.lineEdit_23.setText('')
        self.statusBar().showMessage('New Publisher Added')
        self.Show_Publisher()
     
    def Show_Publisher(self):
        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()
      
        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


# ==============================================================
# ======================= Category =============================

    def Show_Category_Combobox(self):
        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()
       
        for category in data:
            self.comboBox_3.addItem(category[0])

    def Show_Author_Combobox(self):
        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors ''')
        data = self.cur.fetchall()
       
        for authors in data:
            self.comboBox_4.addItem(authors[0])

    def Show_Publisher_Combobox(self):
        self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()
       
        for publisher in data:
            self.comboBox_5.addItem(publisher[0])














def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
    