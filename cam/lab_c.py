#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab.ui'
#
# Created: Mon May 12 19:04:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cv, cv2, sys
import socket

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 120, 320, 240))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "TextLabel", None))

class Lab(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

app = QtGui.QApplication([])
form = Lab()

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


form.show()
UDP_IP = ""
UDP_PORT = 8081
socket.bind((UDP_IP,UDP_PORT))

cam = QtCore.QByteArray()

while True:
    for i in range(2):
        data,addr = socket.recvfrom(60000)
        cam.append(data)
    print len(cam)
    
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(cam,None,QtCore.Qt.AutoColor)
    form.ui.label.setPixmap(pixmap.scaled(form.ui.label.size(),
    QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))        
    cv.WaitKey(5)
    cam.clear()
app.exec_()        

#QPixmap image = new QPixmap();
#image->loadFromData(arr.data());
#label->setPixmap(*image);
