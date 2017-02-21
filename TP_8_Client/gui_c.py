# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_gui.ui'
#
# Created: Thu Mar 17 15:14:41 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(370, 547)
        self.start = QtWidgets.QPushButton(widget)
        self.start.setGeometry(QtCore.QRect(260, 10, 101, 51))
        self.start.setMaximumSize(QtCore.QSize(369, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.start.setFont(font)
        self.start.setCheckable(False)
        self.start.setAutoRepeat(False)
        self.start.setAutoExclusive(False)
        self.start.setAutoDefault(False)
        self.start.setDefault(False)
        self.start.setFlat(False)
        self.start.setObjectName("start")
        self.log_ctrl = QtWidgets.QTabWidget(widget)
        self.log_ctrl.setGeometry(QtCore.QRect(0, 90, 371, 461))
        self.log_ctrl.setObjectName("log_ctrl")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.log_show = QtWidgets.QTextBrowser(self.tab)
        self.log_show.setGeometry(QtCore.QRect(0, 0, 371, 451))
        self.log_show.setObjectName("log_show")
        self.log_ctrl.addTab(self.tab, "")
        self.sta_rssi_choose = QtWidgets.QComboBox(widget)
        self.sta_rssi_choose.setGeometry(QtCore.QRect(70, 20, 91, 22))
        self.sta_rssi_choose.setObjectName("sta_rssi_choose")
        self.sta_rssi_choose.addItem("")
        self.sta_rssi_choose.addItem("")
        self.sta_model = QtWidgets.QLabel(widget)
        self.sta_model.setGeometry(QtCore.QRect(10, 21, 54, 21))
        self.sta_model.setObjectName("sta_model")
        self.sta_ip_lable = QtWidgets.QLabel(widget)
        self.sta_ip_lable.setGeometry(QtCore.QRect(10, 50, 54, 21))
        self.sta_ip_lable.setObjectName("sta_ip_lable")
        self.sta_ip_host = QtWidgets.QLineEdit(widget)
        self.sta_ip_host.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.sta_ip_host.setObjectName("sta_ip_host")

        self.retranslateUi(widget)
        self.log_ctrl.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.start.setText(_translate("widget", "START"))
        self.log_ctrl.setTabText(self.log_ctrl.indexOf(self.tab), _translate("widget", "消息控制台"))
        self.sta_rssi_choose.setItemText(0, _translate("widget", "NIC网卡"))
        self.sta_rssi_choose.setItemText(1, _translate("widget", "WF1931_STA"))
        self.sta_model.setText(_translate("widget", "终端方式"))
        self.sta_ip_lable.setText(_translate("widget", "STA_IP:"))

