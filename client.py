#!/usr/bin/python
# coding: utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mainWindow import Ui_mainWindow
from conWidget import Ui_conWindow
from threading import Thread
import sys, time, socket
from MultiThreadClasses import *

class MainWindow(QWidget):
	def __init__(self ):
		QWidget.__init__(self)
		self.ui = Ui_mainWindow()
		self.ui.setupUi(self)

class ConWindow(MainWindow):
	def __init__(self):
		QWidget.__init__(self)
		self.ui = Ui_conWindow()
		self.ui.setupUi(self)

app = QApplication([])
mainWidget = MainWindow()
connectionWidget = ConWindow()
messageBox = QMessageBox()

data = ["","","",""]

cam = QtCore.QByteArray()
pixmap = QtGui.QPixmap()

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
address1 = ("",)
address2 = ("",)

thread1 = TCPSender(tcpsock,address1,"connection complete")
thread2 = UDPReciever(udpsock,address2,cam)

def main():
	
	connectionWidget.show()
	connectionWidget.connect( connectionWidget.ui.buttonConnect,SIGNAL('pressed()'),clickCWConnectButton)
	connectionWidget.connect( connectionWidget.ui.buttonCancel,SIGNAL('pressed()'),clickCWCancelButton)
	mainWidget.connect(mainWidget.ui.buttonExit1,SIGNAL('pressed()'),clickCWCancelButton)
	mainWidget.connect(mainWidget.ui.buttonBack,SIGNAL('pressed()'),clickMWBackButton)
	mainWidget.connect(mainWidget.ui.buttonTakePicture,SIGNAL('pressed()'),clickMWTakePictureButton)
	mainWidget.connect(mainWidget.ui.buttonCircle,SIGNAL('pressed()'),clickMWCircleButton)
	mainWidget.connect(mainWidget.ui.buttonTriangle,SIGNAL('pressed()'),clickMWTriangleButton)
	mainWidget.connect(mainWidget.ui.buttonRectangle,SIGNAL('pressed()'),clickMWRectangleButton)
	mainWidget.connect(mainWidget.ui.buttonWriteToPlotter,SIGNAL('pressed()'),clickMWWriteToPlotterButton)
	mainWidget.connect(mainWidget.ui.line1,SIGNAL('editingFinished()'),editingFinishedMWLine1)
	mainWidget.connect(mainWidget.ui.line2,SIGNAL('editingFinished()'),editingFinishedMWLine2)
	mainWidget.connect(mainWidget.ui.line3,SIGNAL('editingFinished()'),editingFinishedMWLine3)
	# while True:
	# 	writeCamToLabel()
	# 	cv.WaitKey(5)
	app.exec_()

def clickCWConnectButton():
	address1 = (str(connectionWidget.ui.lineIP.text()),
						int(connectionWidget.ui.linePort.text()))
	address2 = ('',address1[1]+1)
	
	setattr(thread1,'address',address1)
	setattr(thread2,'address',address2)	
	
	udpsock.bind(address2)
	thread1.start()
	thread2.start()

	mainWidget.resize(380, 470)
	mainWidget.show()
	connectionWidget.hide()	
 	
def clickCWCancelButton():
	sys.exit()	

def clickMWTakePictureButton():
	print "buraya fotoğraf çekme fonksiyonu yazılacak"

def clickMWCircleButton():
	mainWidget.setMaximumSize(QSize(380, 668))
	mainWidget.resize(380, 668)
	mainWidget.ui.label1.setText('r')
	mainWidget.ui.label2.hide()
	mainWidget.ui.label3.hide()
	mainWidget.ui.line2.hide()
	mainWidget.ui.line3.hide()
	mainWidget.ui.buttonCircle.setDisabled(True)
	mainWidget.ui.buttonTriangle.setEnabled(True)
	mainWidget.ui.buttonRectangle.setEnabled(True)
	mainWidget.ui.line1.setText('')
	mainWidget.ui.line2.setText('')
	mainWidget.ui.line3.setText('')

def clickMWTriangleButton():
	mainWidget.setMaximumSize(QSize(380, 668))
	mainWidget.resize(380, 668)
	mainWidget.ui.label1.setText('a')
	mainWidget.ui.label2.setText('b')
	mainWidget.ui.label3.setText('c')
	mainWidget.ui.label1.show()
	mainWidget.ui.label2.show()
	mainWidget.ui.label3.show()
	mainWidget.ui.line1.show()
	mainWidget.ui.line2.show()
	mainWidget.ui.line3.show()
	mainWidget.ui.buttonCircle.setEnabled(True)
	mainWidget.ui.buttonTriangle.setDisabled(True)
	mainWidget.ui.buttonRectangle.setEnabled(True)
	mainWidget.ui.line1.setText('')
	mainWidget.ui.line2.setText('')
	mainWidget.ui.line3.setText('')
	

def clickMWRectangleButton():
	mainWidget.setMaximumSize(QSize(380, 668))
	mainWidget.resize(380, 668)
	mainWidget.ui.label1.setText('a')
	mainWidget.ui.label2.setText('b')
	mainWidget.ui.label1.show()
	mainWidget.ui.label2.show()
	mainWidget.ui.label3.hide()
	mainWidget.ui.line1.show()
	mainWidget.ui.line2.show()
	mainWidget.ui.line3.hide()
	mainWidget.ui.buttonCircle.setEnabled(True)
	mainWidget.ui.buttonTriangle.setEnabled(True)
	mainWidget.ui.buttonRectangle.setDisabled(True)
	mainWidget.ui.line1.setText('')
	mainWidget.ui.line2.setText('')
	mainWidget.ui.line3.setText('')
	

def clickMWWriteToPlotterButton():
	setattr(thread1,'data',data)
	print thread1.data	
	print thread1.isAlive(),thread2.isAlive()		

def clickMWBackButton():
	mainWidget.setMaximumSize(QSize(380, 470))
	mainWidget.resize(380,470)
	mainWidget.ui.buttonCircle.setEnabled(True)
	mainWidget.ui.buttonTriangle.setEnabled(True)
	mainWidget.ui.buttonRectangle.setEnabled(True)

def editingFinishedMWLine1():
	data[0] = str(mainWidget.ui.line1.text())
	

def editingFinishedMWLine2():
	data[1] = str(mainWidget.ui.line2.text())
	

def editingFinishedMWLine3():
	data[2] = str(mainWidget.ui.line3.text())
	

def writeCamToLabel():
	if len(cam):
		cam_data = getattr(thread2,'cam')
		pixmap.loadFromData(cam_data,None,QtCore.Qt.AutoColor)
		mainWidget.ui.labelCamera.setPixmap(pixmap.scaled(mainWidget.ui.labelCamera.size(),
				QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))	

if __name__ == '__main__':
	main()
