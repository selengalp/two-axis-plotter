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
camcapture = cv.CaptureFromCAM(0)       
cv.SetCaptureProperty(camcapture,cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cv.SetCaptureProperty(camcapture,cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

UDP_IP = "127.0.0.1"
UDP_PORT = 8081



while True:

    frame = cv.QueryFrame(camcapture)
    image = QtGui.QImage(frame.tostring(), frame.width, frame.height, QtGui.QImage.Format_RGB888).rgbSwapped()
    ba = QtCore.QByteArray()
    buff = QtCore.QBuffer(ba)
    buff.open(QtCore.QIODevice.WriteOnly)
    image.save(buff, "PNG")
    # pixmap = QtGui.QPixmap.fromImage(image)
    # form.ui.label.setPixmap(pixmap.scaled(form.ui.label.size(),
    #     QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
    print len(ba)
    selector = 0 
    for i in range(2):
        if selector is 0:
            socket.sendto(ba[:60000],(UDP_IP, UDP_PORT))
            selector = 1
        if selector is 1:
            socket.sendto(ba[60000:],(UDP_IP, UDP_PORT))
            selector = 0

    cv.WaitKey(5)


app.exec_()        