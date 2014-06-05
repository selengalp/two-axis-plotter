#!/usr/bin/python
#coding: utf-8

import socket
from time import sleep
from MultiThreadClasses import *
import numpy as np 
import cv, cv2
from PyQt4 import QtGui,QtCore

address1 = ("127.0.0.1",8080)
address2 = ("127.0.0.1",8081)

udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

cap = cv.CaptureFromCAM(0)       
cv.SetCaptureProperty(cap,cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cv.SetCaptureProperty(cap,cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

tcpsock.bind(address1) 
tcpsock.listen(4)

print "\nListening for incoming connections..."
(clientsock, addr) = tcpsock.accept()

thread2 = TCPListener(clientsock,addr)
thread2.start()
thread1 = UDPSender(udpsock,address2,cap)
thread1.start()

while True:
    pass
    
    

