# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'con-widget.ui'
#
# Created: Sat May 10 13:12:56 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_conWindow(object):
    def setupUi(self, conWindow):
        conWindow.setObjectName(_fromUtf8("conWindow"))
        conWindow.resize(286, 119)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(conWindow.sizePolicy().hasHeightForWidth())
        conWindow.setSizePolicy(sizePolicy)
        conWindow.setMinimumSize(QtCore.QSize(286, 119))
        conWindow.setMaximumSize(QtCore.QSize(286, 119))
        conWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridLayout = QtGui.QGridLayout(conWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelIP = QtGui.QLabel(conWindow)
        self.labelIP.setObjectName(_fromUtf8("labelIP"))
        self.horizontalLayout.addWidget(self.labelIP)
        self.lineIP = QtGui.QLineEdit(conWindow)
        self.lineIP.setObjectName(_fromUtf8("lineIP"))
        self.horizontalLayout.addWidget(self.lineIP)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonConnect = QtGui.QPushButton(conWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonConnect.sizePolicy().hasHeightForWidth())
        self.buttonConnect.setSizePolicy(sizePolicy)
        self.buttonConnect.setObjectName(_fromUtf8("buttonConnect"))
        self.verticalLayout_2.addWidget(self.buttonConnect)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelPort = QtGui.QLabel(conWindow)
        self.labelPort.setObjectName(_fromUtf8("labelPort"))
        self.horizontalLayout_2.addWidget(self.labelPort)
        self.linePort = QtGui.QLineEdit(conWindow)
        self.linePort.setObjectName(_fromUtf8("linePort"))
        self.horizontalLayout_2.addWidget(self.linePort)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonCancel = QtGui.QPushButton(conWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCancel.sizePolicy().hasHeightForWidth())
        self.buttonCancel.setSizePolicy(sizePolicy)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.verticalLayout.addWidget(self.buttonCancel)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(conWindow)
        QtCore.QMetaObject.connectSlotsByName(conWindow)

    def retranslateUi(self, conWindow):
        conWindow.setWindowTitle(_translate("conWindow", "Connection Window", None))
        self.labelIP.setText(_translate("conWindow", "IP", None))
        self.buttonConnect.setText(_translate("conWindow", "Connect", None))
        self.labelPort.setText(_translate("conWindow", "PORT", None))
        self.buttonCancel.setText(_translate("conWindow", "Cancel", None))

