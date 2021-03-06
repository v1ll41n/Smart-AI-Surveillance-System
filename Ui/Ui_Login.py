from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from client import *

class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 526)
        MainWindow.setStyleSheet(open('mystyle.css','r').read())
        #MainWindow.showFullScreen()
        #MainWindow.showNormal()
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(250, 0, 250, -1)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.Titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel.setMaximumSize(QtCore.QSize(550, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.Titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel.setObjectName("Titlelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Titlelabel)
        self.Emaillabel = QtWidgets.QLabel(self.centralwidget)
        self.Emaillabel.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Emaillabel.setFont(font)
        self.Emaillabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.Emaillabel.setObjectName("Emaillabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Emaillabel)
        self.EmailEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailEdit.setMaximumSize(QtCore.QSize(550, 16777215))
        self.EmailEdit.setObjectName("EmailEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.EmailEdit)
        self.Passlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Passlabel.setFont(font)
        self.Passlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.Passlabel.setObjectName("Passlabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Passlabel)
        self.PassEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PassEdit.setMaximumSize(QtCore.QSize(550, 16777215))
        self.PassEdit.setObjectName("PassEdit")
        self.PassEdit.setEchoMode(QLineEdit.Password)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.PassEdit)
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setMaximumSize(QtCore.QSize(550, 16777215))
        self.LoginButton.setObjectName("LoginButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.LoginButton)
        self.RegButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegButton.setMaximumSize(QtCore.QSize(550, 16777215))
        self.RegButton.setObjectName("RegButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.RegButton)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.LoginButton.clicked.connect(self.LoginWrapper)  
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def LoginWrapper(self):
      self.client=client('http://18.213.123.42',3500)
      self.email=self.EmailEdit.text()
      self.password=self.PassEdit.text()
      #print("email :"+self.email+"\npassword :"+self.password)
      self.msg,self.status=self.client.login(self.email,self.password)
      print(self.status,self.msg)
      self.customResMsg(self.status,self.msg)
    #@override
    def customResMsg(self,status,msg):
        print("inside UI login",status,msg)
        if(status == 200) :
           QtWidgets.QMessageBox.information(self.centralwidget, "Logged in!", msg)
           print(self.client.token)
        elif(status == 400) :
          QtWidgets.QMessageBox.warning(self.centralwidget, "Missing parameter", msg)
        elif(status == 408) :
          QtWidgets.QMessageBox.critical(self.centralwidget, "Connection Error", msg)
        elif(status == 500) :
          QtWidgets.QMessageBox.critical(self.centralwidget, "wrong email/password", msg)
          
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titlelabel.setText(_translate("MainWindow", "Login"))
        self.Emaillabel.setText(_translate("MainWindow", "Email"))
        self.Passlabel.setText(_translate("MainWindow", "Password"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))
        self.RegButton.setText(_translate("MainWindow", "Register"))