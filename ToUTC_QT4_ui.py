# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToUTC_0.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from datetime_test import ParseDatesToUTC

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ConvertToUTC(QtGui.QWidget): #class Ui_Form(object):
    # added manually
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, ConvertToUTC):
        ConvertToUTC.setObjectName(_fromUtf8("ConvertToUTC"))
        ConvertToUTC.resize(524, 304)
        self.setWindowIcon(QtGui.QIcon('ToUTC.png'))
        
        self.gridLayout = QtGui.QGridLayout(ConvertToUTC)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalWidget = QtGui.QWidget(ConvertToUTC)
        self.verticalWidget.setEnabled(True)
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.verticalWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.FilePath = QtGui.QLineEdit(self.verticalWidget)
        self.FilePath.setObjectName(_fromUtf8("FilePath"))
        self.horizontalLayout.addWidget(self.FilePath)
        self.toolButton = QtGui.QToolButton(self.verticalWidget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.verticalWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ColumnNumber = QtGui.QLineEdit(self.verticalWidget)
        self.ColumnNumber.setEnabled(True)
        self.ColumnNumber.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ColumnNumber.setText(_fromUtf8(""))
        self.ColumnNumber.setObjectName(_fromUtf8("ColumnNumber"))
        self.horizontalLayout_2.addWidget(self.ColumnNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.verticalWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.ColSeparator = QtGui.QLineEdit(self.verticalWidget)
        self.ColSeparator.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ColSeparator.setText(_fromUtf8(""))
        self.ColSeparator.setObjectName(_fromUtf8("ColSeparator"))
        self.horizontalLayout_5.addWidget(self.ColSeparator)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.verticalWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.DateTimeFormat = QtGui.QLineEdit(self.verticalWidget)
        self.DateTimeFormat.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DateTimeFormat.setText(_fromUtf8(""))
        self.DateTimeFormat.setObjectName(_fromUtf8("DateTimeFormat"))
        self.horizontalLayout_3.addWidget(self.DateTimeFormat)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.verticalWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.TimeZone = QtGui.QLineEdit(self.verticalWidget)
        self.TimeZone.setMaximumSize(QtCore.QSize(50, 16777215))
        self.TimeZone.setText(_fromUtf8(""))
        self.TimeZone.setObjectName(_fromUtf8("TimeZone"))
        self.horizontalLayout_4.addWidget(self.TimeZone)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton = QtGui.QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.verticalWidget, 0, 0, 1, 1)
         #dafault values
        self.DateTimeFormat.setText("%Y/%m/%d %H:%M")
        self.TimeZone.setText("CET") 
        self.ColumnNumber.setText("1") 
        self.ColSeparator.setText("")
        self.FilePath.setText("...")
        
        self.retranslateUi(ConvertToUTC)
        QtCore.QMetaObject.connectSlotsByName(ConvertToUTC)
        
      

    def retranslateUi(self, ConvertToUTC):
        ConvertToUTC.setWindowTitle(_translate("ConvertToUTC", "Convert To UTC", None))
        self.label_2.setText(_translate("ConvertToUTC", "   Converting file with DateTime column form a specific Time Zone to UTC", None))
        self.label.setText(_translate("ConvertToUTC", " File Path ", None))
        self.toolButton.setText(_translate("ConvertToUTC", "...", None))
        self.label_3.setText(_translate("ConvertToUTC", " DateTime column number                   ", None))
        self.label_6.setText(_translate("ConvertToUTC", " Column separator (. ; , ..etc leave empty for Tab) ", None))
        self.label_4.setText(_translate("ConvertToUTC", " Python DateTime Format (i.e. %Y/%m/%d %H:%M)", None))
        self.label_5.setText(_translate("ConvertToUTC", " Original TimeZone (i.e. CET)              ", None))
        self.pushButton.setText(_translate("ConvertToUTC", "Convert To UTC", None))
        self.toolButton.clicked.connect(self.selectFile)
        self.pushButton.clicked.connect(self.run)
        
    def printHam(self):
        print("Hammam!!")
        
    def selectFile(self):
       # lineEdit.setText(QFileDialog.getOpenFileName())
        self.FilePath.setText(QtGui.QFileDialog.getOpenFileName())
    
    def run(self):
       # lineEdit.setText(QFileDialog.getOpenFileName())
       # self.FilePath.setText(QtGui.QFileDialog.getOpenFileName())
        #path = self.FilePath.textChanged
        timeformat =self.DateTimeFormat.text()
        in_timezone = self.TimeZone.text() # CET
       # filepath = r"C:\Users\matteo_2\.spyder2-py3\n\Kareham_clean_all_turbines_30minut-Exported_2.txt"
        column = int(self.ColumnNumber.text())
        separator = '\t' if self.ColSeparator.text() == "" else self.ColSeparator.text()
        filepath = self.FilePath.text() 
        
        ParseDatesToUTC(filepath,column, separator,timeformat,in_timezone)
        
    
        #ParseDatesToUTC(path,self.ColumnNumber.textChanged,self.ColSeparator.textChanged,self.DateTimeFormat.textChanged,self.TimeZone.textChanged)
     #   ParseDatesToUTC(filepath,column,separator,timeformat,in_timezone,out_timezone='UTC')

#pushButton.clicked.connect(selectFile)        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_ConvertToUTC()
    ex.show()
    sys.exit(app.exec_())

    
