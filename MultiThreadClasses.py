#coding: utf-8

import socket
from threading import Thread
from time import sleep
import numpy as np 
import cv, cv2
from PyQt4 import QtGui,QtCore

class TCPListener(Thread):

    def __init__(self,socket,address):
        Thread.__init__(self)
        self.address = address
        self.socket = socket 
        print "[+] New thread started for ",address


    def run(self):    
        print "Connection from : ",self.address

        self.socket.send("\nWelcome to the server\n\n")

        data = "blablabla"

        while len(data):
            data = self.socket.recv(30)
            print "Client sent : "+data
        print "Client disconnected..."


class UDPSender(Thread):
    
    def __init__(self,socket,address,capture):
        Thread.__init__(self)
        self.address = address
        self.socket = socket
        self.capture = capture
        print "[+] New thread started for ",address
    
    def run(self):
        gray = bytes("1")

        while len(gray):
            frame = cv.QueryFrame(self.capture)
            image = QtGui.QImage(frame.tostring(), frame.width, frame.height, 
                                        QtGui.QImage.Format_RGB888).rgbSwapped()
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly)
            image.save(buff, "PNG") 
            selector = 0 
            for i in range(2):
                if selector is 0:
                    self.socket.sendto(ba[:60000],self.address)
                    selector = 1
                if selector is 1:
                    self.socket.sendto(ba[60000:],self.address)
                    selector = 0
            print self.address,"------",len(ba)             
            cv.WaitKey(5)

class UDPReciever(Thread):
    def __init__(self,socket,address,cam):
        Thread.__init__(self)
        self.address = address
        self.socket = socket
        self.cam = cam
        print "[+] New thread started for ",address

    def run(self):

        while True:
            for i in range(2):
                data, addr = self.socket.recvfrom(60000)
                self.cam.append(data)
            print self.address    
            print len(self.cam)       
            cv.WaitKey(5)
            self.cam.clear()    
            

class TCPSender(Thread):
    def __init__(self,socket,address,data):
        Thread.__init__(self)
        self.address = address
        self.socket = socket
        self.data = data 
        print "[+] New thread started for ",address

    def run(self):
        self.socket.connect(self.address)
        last_data = ["0","0","0","0"]  

        while True:
            print "yessssss"
            print self.address, "buuuuuuuuuu"
            print self.data,"yukarı"

            if self.data  != last_data:
                self.socket.send(bytes(self.data))
                print self.data,"gönderdikten sonra"
                last_data = self.data
                print self.data,"aşağpı"
            else:
                print "something"
                cv.WaitKey(5)   
                print self.data       