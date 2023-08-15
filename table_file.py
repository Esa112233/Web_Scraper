# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabel_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import webscraper as scrape
import sqlstuff as sql
from threading import *
import convert_to_excel_file as excl


class table_win(object):
    def setupUi(self, MainWindow, sql_username):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 896)
        MainWindow.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border-top-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_search_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search_enter.setGeometry(QtCore.QRect(200, 50, 250, 31))
        self.lineEdit_search_enter.setObjectName("lineEdit_search_enter")
        self.lineEdit_Or = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Or.setGeometry(QtCore.QRect(460, 50, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineEdit_Or.setFont(font)
        self.lineEdit_Or.setReadOnly(False)
        self.lineEdit_Or.setObjectName("lineEdit_Or")
        self.lineEdit_Or.setReadOnly(True)
        self.textEdit_search_icon = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_search_icon.setGeometry(QtCore.QRect(20, 50, 160, 31))
        self.textEdit_search_icon.setObjectName("textEdit_search_icon")
        self.textEdit_search_icon.setReadOnly(True)
        self.lineEdit_2_url_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2_url_enter.setGeometry(QtCore.QRect(590, 50, 521, 31))
        self.lineEdit_2_url_enter.setText("")
        self.lineEdit_2_url_enter.setObjectName("lineEdit_2_url_enter")
        self.textEdit_URL_text = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_URL_text.setGeometry(QtCore.QRect(510, 50, 61, 31))
        self.textEdit_URL_text.setObjectName("textEdit_URL_text")
        self.textEdit_URL_text.setReadOnly(True)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 160, 1091, 631))
        self.tableWidget.setMinimumSize(QtCore.QSize(1091, 631))
        self.tableWidget.setMaximumSize(QtCore.QSize(1091, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        # self.checkBox_email = QtWidgets.QCheckBox(self.centralwidget)
        # self.checkBox_email.setGeometry(QtCore.QRect(50, 820, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        # self.checkBox_email.setFont(font)
        # self.checkBox_email.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.checkBox_email.setObjectName("checkBox_email")
        # self.checkBox_URL = QtWidgets.QCheckBox(self.centralwidget)
        # self.checkBox_URL.setGeometry(QtCore.QRect(140, 820, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        # self.checkBox_URL.setFont(font)
        # self.checkBox_URL.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.checkBox_URL.setObjectName("checkBox_URL")
        self.pushButton_convert_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_convert_file.setGeometry(QtCore.QRect(230, 810, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_convert_file.setFont(font)
        self.pushButton_convert_file.setObjectName("pushButton_convert_file")
        self.pushButton_convert_file.clicked.connect(self.convert_to_excel)
        self.pushButton_Find = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Find.setGeometry(QtCore.QRect(420, 90, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Find.setFont(font)
        self.pushButton_Find.setObjectName("pushButton_Find")
        self.pushButton_Find.clicked.connect(self.find_emails_thread)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sql_username = sql_username

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    

    def show_data(self, email_links):
        self.email_links = email_links
        self.row = 0
        self.tableWidget.setRowCount(len(email_links))
        for pair in email_links:
            self.tableWidget.setItem(self.row, 0, QtWidgets.QTableWidgetItem(pair[0]))
            self.tableWidget.setItem(self.row, 1, QtWidgets.QTableWidgetItem(pair[1]))
            self.row+=1
    
    
    def convert_to_excel(self):
        #print(self.email_links)
        # self.email_list_excel = list(self.email_links.keys())
        # self.links_links_excel = list(self.email_links.values())
        self.excel_file_name = self.lineEdit_search_enter.displayText()
        excl.convert(self.email_links, self.excel_file_name)

        


    def find_emails(self):
        self.entered_url = self.lineEdit_2_url_enter.displayText()
        self.email_dict = scrape.user_input_url(self.entered_url)
        print("here")
        self.new_emails = sql.check_result_data(self.email_dict, self.sql_username)
        self.show_data(self.new_emails)


    def find_emails_thread(self):
        t1 = Thread(target=self.find_emails)
        t1.start()

    







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_Or.setText(_translate("MainWindow", "And"))
        self.textEdit_search_icon.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">  Excel File Name:</span></p></body></html>"))
        self.textEdit_URL_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\"> URL:</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Link"))
        self.tableWidget.setColumnWidth(1, 700)
        self.tableWidget.setColumnWidth(0, 400)
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "Link"))
        # self.checkBox_email.setText(_translate("MainWindow", "Email"))
        # self.checkBox_URL.setText(_translate("MainWindow", "URL"))
        self.pushButton_convert_file.setText(_translate("MainWindow", "Convert to Excel File"))
        self.pushButton_Find.setText(_translate("MainWindow", "Find"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow_table = QtWidgets.QMainWindow()
#     ui = table_win()
#     ui.setupUi(MainWindow_table)
#     MainWindow_table.show()
#     sys.exit(app.exec_())

