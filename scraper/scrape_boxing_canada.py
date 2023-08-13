# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlstuff as sql
from tabel_file import table_win
import sys



class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.papa_sports_img = QtWidgets.QLabel(self.centralwidget)
        self.papa_sports_img.setGeometry(QtCore.QRect(260, 70, 201, 211))
        self.papa_sports_img.setText("")
        self.papa_sports_img.setPixmap(QtGui.QPixmap("../../Pictures/Screenshots/Screenshot 2023-08-06 220801.png"))
        self.papa_sports_img.setObjectName("papa_sports_img")
        self.Line_edit_username_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_edit_username_enter.setGeometry(QtCore.QRect(270, 280, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Line_edit_username_enter.setFont(font)
        self.Line_edit_username_enter.setObjectName("Line_edit_username_enter")
        self.textEdit_usernameLBL = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_usernameLBL.setGeometry(QtCore.QRect(160, 280, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_usernameLBL.setFont(font)
        self.textEdit_usernameLBL.setObjectName("textEdit_usernameLBL")
        self.textEdit_usernameLBL.setReadOnly(True)
        self.textEdit_2_passwordLBL = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2_passwordLBL.setGeometry(QtCore.QRect(160, 320, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2_passwordLBL.setFont(font)
        self.textEdit_2_passwordLBL.setObjectName("textEdit_2_passwordLBL")
        self.textEdit_2_passwordLBL.setReadOnly(True)
        self.line_edit_password_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_password_enter.setGeometry(QtCore.QRect(270, 320, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line_edit_password_enter.setFont(font)
        self.line_edit_password_enter.setObjectName("line_edit_password_enter")
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(160, 360, 101, 41))
        self.button_login.setObjectName("button_login")
        self.button_login.clicked.connect(lambda: self.call_table(MainWindow))
        self.button_register = QtWidgets.QPushButton(self.centralwidget)
        self.button_register.setGeometry(QtCore.QRect(260, 360, 101, 41))
        self.button_register.setObjectName("button_register")
        self.button_register.clicked.connect(self.register_clicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 21))
        self.menubar.setObjectName("menubar")
        self.menumenue = QtWidgets.QMenu(self.menubar)
        self.menumenue.setObjectName("menumenue")
        self.menuSave = QtWidgets.QMenu(self.menumenue)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menumenue.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menumenue.menuAction())

        self.stack1 = QtWidgets.QWidget()
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def login_clicked(self):
        usr = self.Line_edit_username_enter.displayText()
        passwrd = self.line_edit_password_enter.displayText()
        

    def already_reg_popup(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Already Registered")
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("User already Registered.")
        x = self.msg.exec_()


    def new_reg_popup(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Already Registered")
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("User successfully registered!")
        x = self.msg.exec_()


    def incorrect_login_popup(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Error")
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("Incorrect Username or Password")
        x = self.msg.exec_()


        
    def register_clicked(self):
        usr = self.Line_edit_username_enter.displayText()
        passwrd = self.line_edit_password_enter.displayText()
        reg_ststus = sql.register(usr, passwrd)
        if reg_ststus is True:
           self.already_reg_popup()
        else:
            self.new_reg_popup()


    def call_table(self, MainWindow):
        self.usr = self.Line_edit_username_enter.displayText()
        self.passwrd = self.line_edit_password_enter.displayText()
        self.check_login = sql.login(self.usr,self.passwrd)
        
        if self.check_login is True:
            MainWindow.close()
            self.MainWindow_table = QtWidgets.QMainWindow()
            self.ui_table = table_win()
            self.ui_table.setupUi(self.MainWindow_table, self.usr)
            self.MainWindow_table.show()
        else: 
            self.incorrect_login_popup()

        
           
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit_usernameLBL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Username:</span></p></body></html>"))
        self.textEdit_2_passwordLBL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Password:</span></p></body></html>"))
        self.button_login.setText(_translate("MainWindow", "Login"))
        self.button_register.setText(_translate("MainWindow", "Register"))
        self.menumenue.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))



class MY_app():
    def __init__(self):
    
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
    
    def run_app(self):
        self.main_window.show()
        sys.exit(self.app.exec_())





if __name__ == "__main__":
    
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)

    # MainWindow.show()
    
    # sys.exit(app.exec_())

    app_instance = MY_app()
    app_instance.run_app()
