from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,res_rc
import MySQLdb
import sqlite3
from PyQt5.uic import loadUiType
import datetime
# from xlrd import *
# from xlsxwriter import *
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from shutil import copyfile
from xlwt import Workbook

con = sqlite3.connect("database/Library.db")
cur = con.cursor()

ui,_ = loadUiType('library2.ui')
login,_ = loadUiType('Login2.ui')
about,_ = loadUiType('AboutUs.ui')

class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        self.pushButton_3.clicked.connect(self.Exit)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
    def Handel_Login(self):
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[0] and password == row[2]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()




            else:
                self.label_9.setText('Make Sure You Enterd Your Username\n& Password Correctly')

    def Exit(self):
        warning = QMessageBox.warning(self , 'Exit' , "You want to exit?" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
         sys.exit(Login)


class AbouUs(QWidget,about):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
 
       
class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        
        self.initGui()
   

        self.Show_Author()
        self.Show_Category()
        self.Show_Publisher()
        
        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()

        self.Show_All_Clients()
        self.Show_All_Books()

        self.Show_All_Operations()

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
        self.pushButton_26.clicked.connect(self.Open_Category_Tab)
     
        self.pushButton_14.clicked.connect(self.Add_Category)
        self.pushButton_32.clicked.connect(self.Delete_Category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_33.clicked.connect(self.Delete_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)
        self.pushButton_34.clicked.connect(self.Delete_Publisher)

        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_13.clicked.connect(self.Login)
        self.pushButton_12.clicked.connect(self.Edit_User)
        self.pushButton_27.clicked.connect(self.DeleteUser)


        self.pushButton_17.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_18.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_19.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_20.clicked.connect(self.QDark_Theme)
     

        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_10.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)
        self.pushButton_9.clicked.connect(self.Delete_Books)
        self.pushButton_28.clicked.connect(self.clear)


        self.pushButton_22.clicked.connect(self.Add_New_Client)
        self.pushButton_24.clicked.connect(self.Search_Client)
        self.pushButton_23.clicked.connect(self.Edit_Client)
        self.pushButton_25.clicked.connect(self.Delete_Client)

        self.pushButton_6.clicked.connect(self.Handel_Day_Operations)

        self.pushButton_29.clicked.connect(self.Export_Day_Operations)
        self.pushButton_30.clicked.connect(self.Export_Books)
        self.pushButton_31.clicked.connect(self.Export_Clients)

    def Show_Themes(self):
        self.groupBox_4.show()

    def Hiding_Themes(self):
        self.groupBox_4.hide()



# ===================== Main Menu Bar ======================

    def initGui(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)

        file_bar = menuBar.addMenu("&File")
        edit_bar = menuBar.addMenu("&Edit")
        view_bar = menuBar.addMenu("&View")
        help_bar = menuBar.addMenu("&Help")

        # Sub menu items
        save_to_excel1 = QAction("Export Day Operation Sheet", self)
        file_bar.addAction(save_to_excel1)
        save_to_excel1.triggered.connect(self.Export_Day_Operations)

        save_to_excel2 = QAction("Export Books Sheet", self)
        file_bar.addAction(save_to_excel2)
        save_to_excel2.triggered.connect(self.Export_Books)

        save_to_excel3 = QAction("Export Clients Sheet", self)
        file_bar.addAction(save_to_excel3)
        save_to_excel3.triggered.connect(self.Export_Clients)
# ======================= File Bar End ==========================================

        exit_file = QAction("Exit", self)
        exit_file.triggered.connect(self.exit_programm_func)
        file_bar.addAction(exit_file)

        # Code Bar
        self.copy_action = QAction("Copy", self)
        self.copy_action.setShortcut("CTRL+C")
        edit_bar.addAction(self.copy_action)

        self.past_action = QAction("Past", self)
        self.past_action.setShortcut("CTRL+V")
        edit_bar.addAction(self.past_action)

        self.cut_action = QAction("Cut", self)
        self.cut_action.setShortcut("CTRL+X")
        edit_bar.addAction(self.cut_action)

        self.undo_action = QAction("Undo", self)
        self.undo_action.setShortcut("CTRL+Z")
        edit_bar.addAction(self.undo_action)

        # Help_bar
        about_prg = QAction("About", self)
        about_prg.triggered.connect(self.Handling_About)
        help_bar.addAction(about_prg)

        # View Bar
        self.full_screen = QAction("Fullscreen Mode", self)
        self.full_screen.setShortcut("F11")
        self.full_screen.triggered.connect(self.enter_full_screen_mode)
        view_bar.addAction(self.full_screen)

        self.exit_full_screen = QAction("Exit Fullscreen Mode", self)
        self.exit_full_screen.setShortcut("Esc")
        self.exit_full_screen.triggered.connect(self.exit_full_screen_mode)
        view_bar.addAction(self.exit_full_screen)



    def Handling_About(self):
        print('user match')
        self.window3 = AbouUs()
        self.window3.show()

 

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

    def Open_Category_Tab(self):
        self.tabWidget.setCurrentIndex(4)



    ########################################
    ######### Day Operations #################

    def Handel_Day_Operations(self):
        book_title = self.lineEdit.text()
        client_name = self.lineEdit_24.text()
        type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)

        print(today_date)
        print(to_date)

        # self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        my_data = (book_title,client_name,type,days_number,today_date,to_date)
        my_query = "INSERT INTO dayoperations VALUES (?,?,?,?,?,?)"
        self.cur.execute(my_query,my_data)


        # self.cur.execute('''
        #     INSERT INTO dayoperations (book_name, client, type , days , date , to_date )
        #     VALUES (%s , %s , %s, %s , %s , %s)
        # ''' , (book_title ,client_name, type , days_number , today_date  , to_date))

        self.db.commit()
        self.statusBar().showMessage('New Operation Added')
        self.Show_All_Operations()


    def Show_All_Operations(self):
        # self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT book_name , client , type , date , to_date FROM dayoperations
        ''')

        data = self.cur.fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

# =============================================================
# ======================= Save Books =============================

    def Show_All_Books(self):
        # self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close()

# ======================== Adding Books =========================
    def Add_New_Book(self):

        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.plainTextEdit.toPlainText()
        book_code = self.lineEdit_4.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_3.text()
        try:
            my_data = (book_title,book_description,book_code,book_category,book_author,book_publisher,book_price)
            my_query = "INSERT INTO book VALUES (?,?,?,?,?,?,?)"
            self.cur.execute(my_query,my_data)
        except:
            buttonReply = QMessageBox.information(self,"Alert!","This Book Name is already taken")

        # self.cur.execute('''
        #     INSERT INTO book (book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
        #     VALUES (%s , %s , %s , %s , %s , %s , %s)
        # ''' ,(book_title , book_description , book_code , book_category , book_author , book_publisher , book_price))

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

    def Search_Books(self):
        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_code = self.lineEdit_8.text()

        if book_title == "" and book_code =="":
            buttonReply = QMessageBox.information(self,"Empty","Please Enter The Book Title")
        else: 
            sql = ''' SELECT * FROM book WHERE book_name = ? or book_code = ?'''
            self.cur.execute(sql , [(book_title),(book_code)])

            data = self.cur.fetchone()

            try:   
                print(data)
                self.lineEdit_5.setText(data[0])
                self.plainTextEdit_2.setPlainText(data[1])
                self.lineEdit_6.setText(data[2])
                self.lineEdit_25.setText(data[3])
                self.lineEdit_26.setText(data[4])
                self.lineEdit_27.setText(data[5])
                self.lineEdit_7.setText(str(data[6]))
            except:
                buttonReply = QMessageBox.information(self,"Sorry","No such book in our Library please check book name")


    def Edit_Books(self):
        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_description = self.plainTextEdit_2.toPlainText()
        book_code = self.lineEdit_6.text()
        book_category = self.lineEdit_25.text()
        book_author = self.lineEdit_26.text()
        book_publisher = self.lineEdit_27.text()
        book_price = self.lineEdit_7.text()

        search_book_title = self.lineEdit_5.text()

        my_data = (book_title, book_description, book_code, book_category, book_author, book_publisher, book_price)
        my_query = "UPDATE book SET  book_name=?, book_description=?, book_code=?, book_category=?, book_author=?, book_publisher=? WHERE book_price=? "
        self.cur.execute(my_query,my_data)

        self.db.commit()
        self.statusBar().showMessage('book updated')
        self.Show_All_Books()


    def Delete_Books(self):
        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_code = self.lineEdit_8.text()

        warning = QMessageBox.warning(self , 'Delete Book' , "are you sure you want to delete this book" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :

            sql = ''' DELETE FROM book WHERE book_name = ? '''
            self.cur.execute(sql , [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')
            self.Show_All_Books()
            
    def clear(self):
            self.lineEdit_5.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_25.setText("")
            self.lineEdit_26.setText("")
            self.lineEdit_27.setText("")
            self.lineEdit_7.setText("")

  ########################################
    ######### Clients #################

    def Show_All_Clients(self):
        # self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT client_name , client_email ,client_nationalid FROM clients ''')
        data = self.cur.fetchall()

      
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

        self.db.close()

# ====================== client =====================
    def Add_New_Client(self):
        client_name = self.lineEdit_36.text()
        client_email = self.lineEdit_35.text()
        client_nationalid = self.lineEdit_37.text()

        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        try:
            my_data = (client_name,client_email,client_nationalid)
            my_query = "INSERT INTO clients VALUES (?,?,?)"
            self.cur.execute(my_query,my_data)
        except:
            buttonReply = QMessageBox.information(self,"Alert!","Email already exist, Try another Email ID")

        # self.cur.execute('''
        #     INSERT INTO clients(client_name , client_email , client_nationalid)
        #     VALUES (%s , %s , %s)
        # ''' , (client_name , client_email , client_nationalid))

        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('New CLient Added')
        self.Show_All_Clients()


    def Search_Client(self):
        client_national_id = self.lineEdit_40.text()
        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        sql = ''' SELECT * FROM clients WHERE client_nationalid = ? '''
        self.cur.execute(sql , [(client_national_id)])
        data = self.cur.fetchone()
    
        try:
            self.lineEdit_38.setText(data[0])
            self.lineEdit_39.setText(data[1])
            self.lineEdit_40.setText(data[2])
        except:
            buttonReply = QMessageBox.information(self,"Alert","Please Enter Your Vaild National Id")


    def Edit_Client(self):
        client_original_national_id = self.lineEdit_40.text()
        client_name = self.lineEdit_38.text()
        client_email = self.lineEdit_39.text()
      

        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        if client_name =="" or client_original_national_id =="" or  client_email  == "":
            buttonReply = QMessageBox.information(self,"Alert!","All fields are required")

        else:

            my_data = (client_name,client_email,client_original_national_id)
            my_query = "UPDATE clients SET  client_name = ?, client_email = ?  WHERE client_nationalid = ?"
            self.cur.execute(my_query,my_data)

            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('Client Data Updated ')
            buttonReply = QMessageBox.information(self,"Success!","Data Added")
            self.lineEdit_38.setText("") 
            self.lineEdit_39.setText("") 
            self.lineEdit_40.setText("") 
            self.Show_All_Clients()


    def Delete_Client(self):
        client_original_national_id = self.lineEdit_40.text()
        
        if client_original_national_id == "":
            buttonReply = QMessageBox.information(self,"Alert!","All fields are required")


        else:
            warning_message = QMessageBox.warning(self , "Delete CLient" , "are you sure you want to delete this client" , QMessageBox.Yes | QMessageBox.No)
            
            if warning_message == QMessageBox.Yes :
                # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
                self.db = sqlite3.connect('database\Library.db')
                self.cur = self.db.cursor()

                sql = ''' DELETE FROM clients WHERE client_nationalid = ? '''
                self.cur.execute(sql , [(client_original_national_id)])

                self.db.commit()
                self.db.close()
                self.statusBar().showMessage('CLient Deleted ')
                self.lineEdit_38.setText("") 
                self.lineEdit_39.setText("") 
                self.lineEdit_40.setText("") 
                self.Show_All_Clients()


# ==============================================================
# ======================= Users =============================

    def Add_New_User(self):
        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password2 = self.lineEdit_12.text()
        if username == "" or email == "" or password == "" or password2 == "":
            buttonReply = QMessageBox.information(self,"Alter!","All fields are required") 

        elif password == password2 :
            my_data = (username,email,password)
            my_query = "INSERT INTO users VALUES (?,?,?)"
            self.cur.execute(my_query,my_data)

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_44.setText('please add a valid password twice')



    def Login(self):
        # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        username = self.lineEdit_13.text()
        password = self.lineEdit_14.text()

        if username =="" or password == "":
            self.statusBar().showMessage('Username & Password Required')
        else:
            sql = ''' SELECT * FROM users'''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            for row in data  :
                if username == row[0] and password == row[2]:
                    print('user match')
                    self.statusBar().showMessage('You Are Successfull Login')
                    self.groupBox_5.setEnabled(True)
                    self.lineEdit_18.setText(row[0])
                    self.lineEdit_20.setText(row[1])
                    self.lineEdit_19.setText(row[2])
                else:
                    self.statusBar().showMessage('Invalid Username Or Password')


    def Edit_User(self):
        username = self.lineEdit_18.text()
        email = self.lineEdit_20.text()
        password = self.lineEdit_19.text()
        password2 = self.lineEdit_17.text()

        if username==""  or email=="" or password=="" or password2 == "":
            buttonReply = QMessageBox.information(self,"Alter!","All fields are required")

        elif password == password2 :
            # self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
            self.db = sqlite3.connect('database\Library.db')
            self.cur = self.db.cursor()

            
            my_data = (username,password,email)
            my_query = "UPDATE users SET  user_name = ?, user_password = ?  WHERE user_email = ?"
            self.cur.execute(my_query,my_data)

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            self.statusBar().showMessage('make sure you entered you password correctly')
           

    def DeleteUser(self):
        user_password = self.lineEdit_19.text()

        if self.lineEdit_18.text()=="" or self.lineEdit_20.text()=="" or self.lineEdit_19.text() == "":
            buttonReply = QMessageBox.information(self,"Alert!","All fields are required")


        else:
            warning_message = QMessageBox.warning(self , "Delete User" , "Are you sure! You want to Delete this User" , QMessageBox.Yes | QMessageBox.No)
            
            if warning_message == QMessageBox.Yes :
                # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
                self.db = sqlite3.connect('database\Library.db')
                self.cur = self.db.cursor()

                sql = ''' DELETE FROM users WHERE user_password = ? '''
                self.cur.execute(sql , [(user_password)])

                self.db.commit()
                self.db.close()
                self.statusBar().showMessage('User Deleted ')
                self.Show_All_Clients()


# ==============================================================
# ======================= Category =============================

    def Add_Category(self):

        # self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_21.text()
        if category_name == "":
            buttonReply = QMessageBox.information(self,"Alert!","Please enter category name")
        else:
            my_data = (category_name,)
            my_query = "INSERT INTO category (category_name) VALUES (?)"
            self.cur.execute(my_query,my_data)

        
        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.lineEdit_21.setText('')
        self.Show_Category()
        self.Show_Category_Combobox()
     

    def Show_Category(self):
        # self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category''')
        data = self.cur.fetchall()
        
        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(item))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def Delete_Category(self):  
        category_name = self.lineEdit_21.text()
        if self.lineEdit_21.text() == "":
            buttonReply = QMessageBox.information(self,"Alert!","Please enter category name")
        else:
            warning_message = QMessageBox.warning(self , "Delete User" , "Are you sure! You want to Delete this User" , QMessageBox.Yes | QMessageBox.No)
            if warning_message == QMessageBox.Yes :
                self.db = sqlite3.connect('database\Library.db')
                self.cur = self.db.cursor()
                sql = ''' DELETE FROM category WHERE category_name = ? '''
                self.cur.execute(sql , [(category_name)])
                self.db.commit()
                self.db.close()
                self.statusBar().showMessage('Category Deleted ')
                self.Show_Category()

    def Add_Author(self):
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()
        author_name = self.lineEdit_22.text()

        my_data = (author_name,)
        my_query = "INSERT INTO authors (author_name) VALUES (?)"
        self.cur.execute(my_query,my_data)
 
        self.db.commit()
        self.lineEdit_22.setText('')
        self.statusBar().showMessage('New Author Added')
        self.Show_Author()
        self.Show_Author_Combobox()

    def Show_Author(self):
        # self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
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


    def Delete_Author(self):   
        Author_name = self.lineEdit_22.text()
        if self.lineEdit_22.text() == "":
            buttonReply = QMessageBox.information(self,"Alert!","Please enter Author name")
        else:
            warning_message = QMessageBox.warning(self , "Delete User" , "Are you sure! You want to Delete this Author" , QMessageBox.Yes | QMessageBox.No)
            if warning_message == QMessageBox.Yes :
                # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
                self.db = sqlite3.connect('database\Library.db')
                self.cur = self.db.cursor()

                sql = ''' DELETE FROM authors WHERE author_name = ? '''
                self.cur.execute(sql , [(Author_name)])

                self.db.commit()
                self.db.close()
                self.statusBar().showMessage('Category Deleted ')
                self.Show_Author()


    def Add_Publisher(self):
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()
        publisher_name = self.lineEdit_23.text()

        my_data = (publisher_name,)
        my_query = "INSERT INTO publisher (publisher_name) VALUES (?)"
        self.cur.execute(my_query,my_data)

        self.db.commit()
        self.lineEdit_23.setText('')
        self.statusBar().showMessage('New Publisher Added')
        self.Show_Publisher()
        self.Show_Author_Combobox()
     
    def Show_Publisher(self):
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
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

    def Delete_Publisher(self):   
        Publisher_name = self.lineEdit_23.text()
      
        if self.lineEdit_23.text() == "":
            buttonReply = QMessageBox.information(self,"Alert!","Please enter Publisher name")

        else:
            warning_message = QMessageBox.warning(self , "Delete User" , "Are you sure! You want to Publisher this Author" , QMessageBox.Yes | QMessageBox.No)
            if warning_message == QMessageBox.Yes :
                # self.db = MySQLdb.connect(host='localhost' , user='root' , password ='Shubham@lohar952' , db='library')
                self.db = sqlite3.connect('database\Library.db')
                self.cur = self.db.cursor()

                sql = ''' DELETE FROM publisher WHERE publisher_name = ? '''
                self.cur.execute(sql , [(Publisher_name)])

                self.db.commit()
                self.db.close()
                self.statusBar().showMessage('Publisher Deleted ')
                self.Show_Publisher()
        
# ==============================================================
# ======================= Category =============================

    def Show_Category_Combobox(self):
        # self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()
       
        for category in data:
            self.comboBox_3.addItem(category[0])

    def Show_Author_Combobox(self):
        # self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors ''')
        data = self.cur.fetchall()
       
        for authors in data:
            self.comboBox_4.addItem(authors[0])

    def Show_Publisher_Combobox(self):
        # self.db = MySQLdb.connect(host='localhost',user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()
       
        for publisher in data:
            self.comboBox_5.addItem(publisher[0])


    def exit_programm_func(self):
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

    def enter_full_screen_mode(self):
        self.showFullScreen()
     
    def exit_full_screen_mode(self):
        self.showNormal()


    ########################################
    ######### Export Data #################
         
    def Export_Day_Operations(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT book_name, client, type, days , date, to_date FROM dayoperations ''')
        data = self.cur.fetchall()

        wb = Workbook()
        path, _ = QFileDialog.getSaveFileName(self, "Save File", QDir.homePath() + "/Day_Operations.xls", "XLS Files(*.xls *.txt)")

        if path:
            sheet1  = wb.add_sheet('Day_Operations')
            sheet1.write(0,0,'book title')
            sheet1.write(0,1,'cliant name')
            sheet1.write(0,2,'type')
            sheet1.write(0,3,'days')
            sheet1.write(0,4,'from - date')
            sheet1.write(0,5,'to - date')
            row_number = 1
            for row in data :
                column_number = 0
                for item in row :
                    sheet1.write(row_number , column_number , str(item))
                    column_number += 1
                row_number += 1
            self.statusBar().showMessage('Report Created Successfully')

        wb.save(path)



    def Export_Books(self):
        # self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        wb = Workbook()
        path, _ = QFileDialog.getSaveFileName(self, "Save File", QDir.homePath() + "/Books.xls", "XLS Files(*.xls *.txt)")
        if path:
            sheet1 = wb.add_sheet('Books')
            sheet1.write(0,0 , 'Book Code')
            sheet1.write(0,1 , 'Book Name')
            sheet1.write(0,2 , 'Book Description')
            sheet1.write(0,3 , 'Book Category')
            sheet1.write(0,4 , 'Book Author')
            sheet1.write(0,5 , 'Book publisher')
            sheet1.write(0,6 , 'Book Price')
            row_number = 1
            for row in data :
                column_number = 0
                for item in row :
                    sheet1.write(row_number , column_number , str(item))
                    column_number += 1
                row_number += 1
            self.statusBar().showMessage('Book Report Created Successfully')
        wb.save(path)


    def Export_Clients(self):
        # self.db = MySQLdb.connect(host='localhost', user='root', password='Shubham@lohar952', db='library')
        self.db = sqlite3.connect('database\Library.db')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT client_name , client_email ,client_nationalid FROM clients ''')
        data = self.cur.fetchall()

        wb = Workbook('Exported_Data\clients.xlsx')
        path, _ = QFileDialog.getSaveFileName(self, "Save File", QDir.homePath() + "/Clients.xls", "XLS Files(*.xls *.txt)")
        if path:
            sheet1 = wb.add_sheet('Clients')
            sheet1.write(0,0 , 'Client Name')
            sheet1.write(0,1 , 'CLient Email')
            sheet1.write(0,2 , 'CLient NationalID')
            row_number = 1
            for row in data :
                column_number = 0
                for item in row :
                    sheet1.write(row_number , column_number , str(item))
                    column_number += 1
                row_number += 1
            self.statusBar().showMessage('Clients Report Created Successfully')
        wb.save(path)

 ########################################
 #########  UI Themes #################

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

def main():
    app = QApplication(sys.argv)
    window = Login()
    # window = MainApp()
    window.show()
    sys.exit(app.exec_())
    # app.exec_()


if __name__ == '__main__':
    main()
    