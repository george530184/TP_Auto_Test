# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp_more_degree.ui'
#
# Created: Thu Mar 17 15:55:58 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 604)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AP_frame = QtWidgets.QFrame(self.centralwidget)
        self.AP_frame.setGeometry(QtCore.QRect(0, 0, 501, 241))
        self.AP_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.AP_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AP_frame.setObjectName("AP_frame")
        self.AP_Config_Title_Lable = QtWidgets.QLabel(self.AP_frame)
        self.AP_Config_Title_Lable.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.AP_Config_Title_Lable.setObjectName("AP_Config_Title_Lable")
        self.AP_TYPE_Lable = QtWidgets.QLabel(self.AP_frame)
        self.AP_TYPE_Lable.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.AP_TYPE_Lable.setObjectName("AP_TYPE_Lable")
        self.AP_Type_Choose = QtWidgets.QComboBox(self.AP_frame)
        self.AP_Type_Choose.setGeometry(QtCore.QRect(70, 30, 96, 20))
        self.AP_Type_Choose.setEditable(False)
        self.AP_Type_Choose.setObjectName("AP_Type_Choose")
        self.AP_Type_Choose.addItem("")
        self.AP_Type_Choose.addItem("")
        self.label_5g_ap = QtWidgets.QLabel(self.AP_frame)
        self.label_5g_ap.setGeometry(QtCore.QRect(280, 90, 51, 23))
        self.label_5g_ap.setObjectName("label_5g_ap")
        self.Channel_5_Lable = QtWidgets.QLabel(self.AP_frame)
        self.Channel_5_Lable.setGeometry(QtCore.QRect(290, 110, 51, 21))
        self.Channel_5_Lable.setObjectName("Channel_5_Lable")
        self.Channel_5 = QtWidgets.QLineEdit(self.AP_frame)
        self.Channel_5.setGeometry(QtCore.QRect(340, 110, 101, 20))
        self.Channel_5.setObjectName("Channel_5")
        self.Band_5_Lable = QtWidgets.QLabel(self.AP_frame)
        self.Band_5_Lable.setGeometry(QtCore.QRect(290, 130, 61, 21))
        self.Band_5_Lable.setObjectName("Band_5_Lable")
        self.HT_20_5g = QtWidgets.QRadioButton(self.AP_frame)
        self.HT_20_5g.setGeometry(QtCore.QRect(340, 130, 51, 16))
        self.HT_20_5g.setObjectName("HT_20_5g")
        self.HT40_up_5g = QtWidgets.QRadioButton(self.AP_frame)
        self.HT40_up_5g.setGeometry(QtCore.QRect(390, 130, 51, 16))
        self.HT40_up_5g.setObjectName("HT40_up_5g")
        self.HT40_down_5g = QtWidgets.QRadioButton(self.AP_frame)
        self.HT40_down_5g.setGeometry(QtCore.QRect(340, 150, 51, 16))
        self.HT40_down_5g.setObjectName("HT40_down_5g")
        self.HT40_5g = QtWidgets.QRadioButton(self.AP_frame)
        self.HT40_5g.setGeometry(QtCore.QRect(390, 150, 51, 16))
        self.HT40_5g.setObjectName("HT40_5g")
        self.HT80_5g = QtWidgets.QRadioButton(self.AP_frame)
        self.HT80_5g.setGeometry(QtCore.QRect(440, 150, 51, 16))
        self.HT80_5g.setObjectName("HT80_5g")
        self.SSID_5_Lable = QtWidgets.QLabel(self.AP_frame)
        self.SSID_5_Lable.setGeometry(QtCore.QRect(290, 170, 41, 21))
        self.SSID_5_Lable.setObjectName("SSID_5_Lable")
        self.SSID_5 = QtWidgets.QLineEdit(self.AP_frame)
        self.SSID_5.setGeometry(QtCore.QRect(340, 170, 113, 20))
        self.SSID_5.setObjectName("SSID_5")
        self.AP_IP_Lable = QtWidgets.QLabel(self.AP_frame)
        self.AP_IP_Lable.setGeometry(QtCore.QRect(10, 60, 31, 20))
        self.AP_IP_Lable.setObjectName("AP_IP_Lable")
        self.AP_IP = QtWidgets.QLineEdit(self.AP_frame)
        self.AP_IP.setGeometry(QtCore.QRect(70, 60, 101, 20))
        self.AP_IP.setObjectName("AP_IP")
        self.AP_User_Lable = QtWidgets.QLabel(self.AP_frame)
        self.AP_User_Lable.setGeometry(QtCore.QRect(180, 60, 31, 20))
        self.AP_User_Lable.setObjectName("AP_User_Lable")
        self.AP_User = QtWidgets.QLineEdit(self.AP_frame)
        self.AP_User.setGeometry(QtCore.QRect(210, 60, 71, 20))
        self.AP_User.setObjectName("AP_User")
        self.AP_Passd_Lable = QtWidgets.QLabel(self.AP_frame)
        self.AP_Passd_Lable.setGeometry(QtCore.QRect(290, 60, 51, 20))
        self.AP_Passd_Lable.setObjectName("AP_Passd_Lable")
        self.AP_Passwd = QtWidgets.QLineEdit(self.AP_frame)
        self.AP_Passwd.setGeometry(QtCore.QRect(360, 60, 81, 20))
        self.AP_Passwd.setObjectName("AP_Passwd")
        self.AP_Frame_2 = QtWidgets.QFrame(self.AP_frame)
        self.AP_Frame_2.setGeometry(QtCore.QRect(0, 90, 241, 141))
        self.AP_Frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AP_Frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AP_Frame_2.setObjectName("AP_Frame_2")
        self.Label_2g_ap = QtWidgets.QLabel(self.AP_Frame_2)
        self.Label_2g_ap.setGeometry(QtCore.QRect(10, 0, 51, 23))
        self.Label_2g_ap.setObjectName("Label_2g_ap")
        self.Channel_2_Lable = QtWidgets.QLabel(self.AP_Frame_2)
        self.Channel_2_Lable.setGeometry(QtCore.QRect(30, 20, 51, 21))
        self.Channel_2_Lable.setObjectName("Channel_2_Lable")
        self.Channel_2 = QtWidgets.QLineEdit(self.AP_Frame_2)
        self.Channel_2.setGeometry(QtCore.QRect(80, 20, 101, 20))
        self.Channel_2.setObjectName("Channel_2")
        self.HT40_2g = QtWidgets.QRadioButton(self.AP_Frame_2)
        self.HT40_2g.setGeometry(QtCore.QRect(130, 60, 51, 16))
        self.HT40_2g.setObjectName("HT40_2g")
        self.HT_40_up_2g = QtWidgets.QRadioButton(self.AP_Frame_2)
        self.HT_40_up_2g.setGeometry(QtCore.QRect(130, 40, 51, 16))
        self.HT_40_up_2g.setObjectName("HT_40_up_2g")
        self.HT_20_2g = QtWidgets.QRadioButton(self.AP_Frame_2)
        self.HT_20_2g.setGeometry(QtCore.QRect(80, 40, 51, 16))
        self.HT_20_2g.setObjectName("HT_20_2g")
        self.SSID_2 = QtWidgets.QLineEdit(self.AP_Frame_2)
        self.SSID_2.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.SSID_2.setObjectName("SSID_2")
        self.HT40_down_2g = QtWidgets.QRadioButton(self.AP_Frame_2)
        self.HT40_down_2g.setGeometry(QtCore.QRect(80, 60, 51, 16))
        self.HT40_down_2g.setObjectName("HT40_down_2g")
        self.SSID_2_Lable = QtWidgets.QLabel(self.AP_Frame_2)
        self.SSID_2_Lable.setGeometry(QtCore.QRect(30, 80, 41, 21))
        self.SSID_2_Lable.setObjectName("SSID_2_Lable")
        self.Band_2_Lable = QtWidgets.QLabel(self.AP_Frame_2)
        self.Band_2_Lable.setGeometry(QtCore.QRect(30, 40, 41, 21))
        self.Band_2_Lable.setObjectName("Band_2_Lable")
        self.config_ap = QtWidgets.QPushButton(self.AP_frame)
        self.config_ap.setGeometry(QtCore.QRect(410, 200, 75, 31))
        self.config_ap.setObjectName("config_ap")
        self.chariot_frame = QtWidgets.QFrame(self.centralwidget)
        self.chariot_frame.setGeometry(QtCore.QRect(0, 240, 501, 131))
        self.chariot_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.chariot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chariot_frame.setObjectName("chariot_frame")
        self.label_5g_chariot = QtWidgets.QLabel(self.chariot_frame)
        self.label_5g_chariot.setGeometry(QtCore.QRect(280, 20, 51, 23))
        self.label_5g_chariot.setObjectName("label_5g_chariot")
        self.chariot_pc_ip_5_label = QtWidgets.QLabel(self.chariot_frame)
        self.chariot_pc_ip_5_label.setGeometry(QtCore.QRect(270, 40, 41, 23))
        self.chariot_pc_ip_5_label.setObjectName("chariot_pc_ip_5_label")
        self.chariot_pc_IP_5g = QtWidgets.QLineEdit(self.chariot_frame)
        self.chariot_pc_IP_5g.setGeometry(QtCore.QRect(310, 40, 151, 20))
        self.chariot_pc_IP_5g.setObjectName("chariot_pc_IP_5g")
        self.chariot_5g_duration_label = QtWidgets.QLabel(self.chariot_frame)
        self.chariot_5g_duration_label.setGeometry(QtCore.QRect(270, 100, 51, 21))
        self.chariot_5g_duration_label.setObjectName("chariot_5g_duration_label")
        self.chariot_duration_5g = QtWidgets.QLineEdit(self.chariot_frame)
        self.chariot_duration_5g.setGeometry(QtCore.QRect(320, 100, 41, 20))
        self.chariot_duration_5g.setObjectName("chariot_duration_5g")
        self.chariot_5g_pair_label = QtWidgets.QLabel(self.chariot_frame)
        self.chariot_5g_pair_label.setGeometry(QtCore.QRect(370, 100, 41, 21))
        self.chariot_5g_pair_label.setObjectName("chariot_5g_pair_label")
        self.chariot_pair_5g = QtWidgets.QLineEdit(self.chariot_frame)
        self.chariot_pair_5g.setGeometry(QtCore.QRect(420, 100, 41, 20))
        self.chariot_pair_5g.setObjectName("chariot_pair_5g")
        self.chariot_frame_2 = QtWidgets.QFrame(self.chariot_frame)
        self.chariot_frame_2.setGeometry(QtCore.QRect(0, 0, 241, 131))
        self.chariot_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chariot_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chariot_frame_2.setObjectName("chariot_frame_2")
        self.Chariot_config_title_label = QtWidgets.QLabel(self.chariot_frame_2)
        self.Chariot_config_title_label.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.Chariot_config_title_label.setObjectName("Chariot_config_title_label")
        self.label_2g_chariot = QtWidgets.QLabel(self.chariot_frame_2)
        self.label_2g_chariot.setGeometry(QtCore.QRect(10, 20, 51, 23))
        self.label_2g_chariot.setObjectName("label_2g_chariot")
        self.chariot_pc_ip_2_label = QtWidgets.QLabel(self.chariot_frame_2)
        self.chariot_pc_ip_2_label.setGeometry(QtCore.QRect(10, 40, 31, 23))
        self.chariot_pc_ip_2_label.setObjectName("chariot_pc_ip_2_label")
        self.chariot_pc_IP_2g = QtWidgets.QLineEdit(self.chariot_frame_2)
        self.chariot_pc_IP_2g.setGeometry(QtCore.QRect(50, 40, 151, 20))
        self.chariot_pc_IP_2g.setObjectName("chariot_pc_IP_2g")
        self.chariot_2g_duration_label = QtWidgets.QLabel(self.chariot_frame_2)
        self.chariot_2g_duration_label.setGeometry(QtCore.QRect(10, 100, 51, 21))
        self.chariot_2g_duration_label.setObjectName("chariot_2g_duration_label")
        self.chariot_duration_2g = QtWidgets.QLineEdit(self.chariot_frame_2)
        self.chariot_duration_2g.setGeometry(QtCore.QRect(60, 100, 41, 20))
        self.chariot_duration_2g.setObjectName("chariot_duration_2g")
        self.chariot_2g_pair_label = QtWidgets.QLabel(self.chariot_frame_2)
        self.chariot_2g_pair_label.setGeometry(QtCore.QRect(110, 100, 41, 21))
        self.chariot_2g_pair_label.setObjectName("chariot_2g_pair_label")
        self.chariot_pair_2g = QtWidgets.QLineEdit(self.chariot_frame_2)
        self.chariot_pair_2g.setGeometry(QtCore.QRect(160, 100, 41, 20))
        self.chariot_pair_2g.setObjectName("chariot_pair_2g")
        self.chariot_sta_IP_2g = QtWidgets.QLineEdit(self.chariot_frame_2)
        self.chariot_sta_IP_2g.setGeometry(QtCore.QRect(50, 70, 151, 20))
        self.chariot_sta_IP_2g.setObjectName("chariot_sta_IP_2g")
        self.chariot_sta_ip_2_label = QtWidgets.QLabel(self.chariot_frame_2)
        self.chariot_sta_ip_2_label.setGeometry(QtCore.QRect(10, 70, 41, 20))
        self.chariot_sta_ip_2_label.setObjectName("chariot_sta_ip_2_label")
        self.chariot_sta_IP_5g = QtWidgets.QLineEdit(self.chariot_frame)
        self.chariot_sta_IP_5g.setGeometry(QtCore.QRect(310, 70, 151, 20))
        self.chariot_sta_IP_5g.setObjectName("chariot_sta_IP_5g")
        self.chariot_sta_ip_5_label = QtWidgets.QLabel(self.chariot_frame)
        self.chariot_sta_ip_5_label.setGeometry(QtCore.QRect(270, 70, 41, 20))
        self.chariot_sta_ip_5_label.setObjectName("chariot_sta_ip_5_label")
        self.Config_frame = QtWidgets.QFrame(self.centralwidget)
        self.Config_frame.setGeometry(QtCore.QRect(0, 370, 501, 131))
        self.Config_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Config_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Config_frame.setObjectName("Config_frame")
        self.Degree_config_label = QtWidgets.QLabel(self.Config_frame)
        self.Degree_config_label.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.Degree_config_label.setObjectName("Degree_config_label")
        self.Degree_8 = QtWidgets.QRadioButton(self.Config_frame)
        self.Degree_8.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.Degree_8.setObjectName("Degree_8")
        self.Degree_4 = QtWidgets.QRadioButton(self.Config_frame)
        self.Degree_4.setGeometry(QtCore.QRect(290, 30, 244, 16))
        self.Degree_4.setAutoExclusive(True)
        self.Degree_4.setAutoRepeatDelay(300)
        self.Degree_4.setObjectName("Degree_4")
        self.Distance_config_label = QtWidgets.QLabel(self.Config_frame)
        self.Distance_config_label.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.Distance_config_label.setObjectName("Distance_config_label")
        self.D_10m_4 = QtWidgets.QCheckBox(self.Config_frame)
        self.D_10m_4.setGeometry(QtCore.QRect(300, 70, 51, 16))
        self.D_10m_4.setObjectName("D_10m_4")
        self.D_50m_4 = QtWidgets.QCheckBox(self.Config_frame)
        self.D_50m_4.setGeometry(QtCore.QRect(370, 70, 51, 16))
        self.D_50m_4.setObjectName("D_50m_4")
        self.Band_config_label = QtWidgets.QLabel(self.Config_frame)
        self.Band_config_label.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.Band_config_label.setObjectName("Band_config_label")
        self.D_2g_4 = QtWidgets.QCheckBox(self.Config_frame)
        self.D_2g_4.setGeometry(QtCore.QRect(300, 110, 51, 16))
        self.D_2g_4.setObjectName("D_2g_4")
        self.D_5g_4 = QtWidgets.QCheckBox(self.Config_frame)
        self.D_5g_4.setGeometry(QtCore.QRect(370, 110, 51, 16))
        self.D_5g_4.setObjectName("D_5g_4")
        self.Config_frame_2 = QtWidgets.QFrame(self.Config_frame)
        self.Config_frame_2.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.Config_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Config_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Config_frame_2.setObjectName("Config_frame_2")
        self.D_10m_8 = QtWidgets.QCheckBox(self.Config_frame_2)
        self.D_10m_8.setGeometry(QtCore.QRect(20, 10, 51, 16))
        self.D_10m_8.setObjectName("D_10m_8")
        self.D_50m_8 = QtWidgets.QCheckBox(self.Config_frame_2)
        self.D_50m_8.setGeometry(QtCore.QRect(90, 10, 41, 21))
        self.D_50m_8.setObjectName("D_50m_8")
        self.Config_frame_3 = QtWidgets.QFrame(self.Config_frame)
        self.Config_frame_3.setGeometry(QtCore.QRect(10, 100, 120, 31))
        self.Config_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Config_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Config_frame_3.setObjectName("Config_frame_3")
        self.D_2g_8 = QtWidgets.QCheckBox(self.Config_frame_3)
        self.D_2g_8.setGeometry(QtCore.QRect(20, 10, 51, 16))
        self.D_2g_8.setObjectName("D_2g_8")
        self.D_5g_8 = QtWidgets.QCheckBox(self.Config_frame_3)
        self.D_5g_8.setGeometry(QtCore.QRect(90, 10, 51, 16))
        self.D_5g_8.setObjectName("D_5g_8")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(270, 510, 91, 41))
        self.start.setObjectName("start")
        self.report = QtWidgets.QPushButton(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(400, 510, 91, 41))
        self.report.setObjectName("report")
        self.log_mess = QtWidgets.QTabWidget(self.centralwidget)
        self.log_mess.setGeometry(QtCore.QRect(510, 0, 431, 501))
        self.log_mess.setObjectName("log_mess")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.log_text = QtWidgets.QTextBrowser(self.widget)
        self.log_text.setGeometry(QtCore.QRect(0, 0, 431, 481))
        self.log_text.setObjectName("log_text")
        self.log_mess.addTab(self.widget, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Cai_Dang_Lang = QtWidgets.QMenuBar(MainWindow)
        self.Cai_Dang_Lang.setGeometry(QtCore.QRect(0, 0, 947, 23))
        self.Cai_Dang_Lang.setAccessibleName("")
        self.Cai_Dang_Lang.setObjectName("Cai_Dang_Lang")
        self.log = QtWidgets.QMenu(self.Cai_Dang_Lang)
        self.log.setObjectName("log")
        self.about = QtWidgets.QMenu(self.Cai_Dang_Lang)
        self.about.setObjectName("about")
        MainWindow.setMenuBar(self.Cai_Dang_Lang)
        self.Zhuang_Tai_Lang = QtWidgets.QStatusBar(MainWindow)
        self.Zhuang_Tai_Lang.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Zhuang_Tai_Lang.setObjectName("Zhuang_Tai_Lang")
        MainWindow.setStatusBar(self.Zhuang_Tai_Lang)
        self.running_log = QtWidgets.QAction(MainWindow)
        self.running_log.setObjectName("running_log")
        self.about_ver = QtWidgets.QAction(MainWindow)
        self.about_ver.setObjectName("about_ver")
        self.log.addAction(self.running_log)
        self.about.addAction(self.about_ver)
        self.Cai_Dang_Lang.addAction(self.log.menuAction())
        self.Cai_Dang_Lang.addAction(self.about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CIG TP多角度测试系统_V1.3"))
        self.AP_Config_Title_Lable.setText(_translate("MainWindow", "AP配置选项"))
        self.AP_TYPE_Lable.setText(_translate("MainWindow", "AP类型："))
        self.AP_Type_Choose.setItemText(0, _translate("MainWindow", "CIG "))
        self.AP_Type_Choose.setItemText(1, _translate("MainWindow", "NOKIA_1931"))
        self.label_5g_ap.setText(_translate("MainWindow", "5G"))
        self.Channel_5_Lable.setText(_translate("MainWindow", "Channel"))
        self.Band_5_Lable.setText(_translate("MainWindow", "Band"))
        self.HT_20_5g.setText(_translate("MainWindow", "HT20"))
        self.HT40_up_5g.setText(_translate("MainWindow", "HT40+"))
        self.HT40_down_5g.setText(_translate("MainWindow", "HT40-"))
        self.HT40_5g.setText(_translate("MainWindow", "HT40"))
        self.HT80_5g.setText(_translate("MainWindow", "HT80"))
        self.SSID_5_Lable.setText(_translate("MainWindow", "SSID"))
        self.AP_IP_Lable.setText(_translate("MainWindow", "AP IP"))
        self.AP_User_Lable.setText(_translate("MainWindow", "User"))
        self.AP_Passd_Lable.setText(_translate("MainWindow", "Password"))
        self.Label_2g_ap.setText(_translate("MainWindow", "2.4G"))
        self.Channel_2_Lable.setText(_translate("MainWindow", "Channel"))
        self.HT40_2g.setText(_translate("MainWindow", "HT40"))
        self.HT_40_up_2g.setText(_translate("MainWindow", "HT40+"))
        self.HT_20_2g.setText(_translate("MainWindow", "HT20"))
        self.HT40_down_2g.setText(_translate("MainWindow", "HT40-"))
        self.SSID_2_Lable.setText(_translate("MainWindow", "SSID"))
        self.Band_2_Lable.setText(_translate("MainWindow", "Band"))
        self.config_ap.setText(_translate("MainWindow", "配置AP"))
        self.label_5g_chariot.setText(_translate("MainWindow", "5G"))
        self.chariot_pc_ip_5_label.setText(_translate("MainWindow", "PC_IP"))
        self.chariot_5g_duration_label.setText(_translate("MainWindow", "Duration"))
        self.chariot_5g_pair_label.setText(_translate("MainWindow", "PairNum"))
        self.Chariot_config_title_label.setText(_translate("MainWindow", "Chariot配置选项"))
        self.label_2g_chariot.setText(_translate("MainWindow", "2.4G"))
        self.chariot_pc_ip_2_label.setText(_translate("MainWindow", "PC_IP"))
        self.chariot_2g_duration_label.setText(_translate("MainWindow", "Duration"))
        self.chariot_2g_pair_label.setText(_translate("MainWindow", "PairNum"))
        self.chariot_sta_ip_2_label.setText(_translate("MainWindow", "STA_IP"))
        self.chariot_sta_ip_5_label.setText(_translate("MainWindow", "STA_IP"))
        self.Degree_config_label.setText(_translate("MainWindow", "测试角度配置"))
        self.Degree_8.setText(_translate("MainWindow", "8角度测试"))
        self.Degree_4.setText(_translate("MainWindow", "4角度测试"))
        self.Distance_config_label.setText(_translate("MainWindow", "测试距离配置"))
        self.D_10m_4.setText(_translate("MainWindow", "10m"))
        self.D_50m_4.setText(_translate("MainWindow", "50m"))
        self.Band_config_label.setText(_translate("MainWindow", "测试频段配置"))
        self.D_2g_4.setText(_translate("MainWindow", "2.4G"))
        self.D_5g_4.setText(_translate("MainWindow", "5G"))
        self.D_10m_8.setText(_translate("MainWindow", "10m"))
        self.D_50m_8.setText(_translate("MainWindow", "50m"))
        self.D_2g_8.setText(_translate("MainWindow", "2.4G"))
        self.D_5g_8.setText(_translate("MainWindow", "5G"))
        self.start.setText(_translate("MainWindow", "START"))
        self.report.setText(_translate("MainWindow", "Report"))
        self.log_mess.setTabText(self.log_mess.indexOf(self.widget), _translate("MainWindow", "消息控制台"))
        self.log.setTitle(_translate("MainWindow", "日志"))
        self.about.setTitle(_translate("MainWindow", "关于"))
        self.running_log.setText(_translate("MainWindow", "运行日志"))
        self.about_ver.setText(_translate("MainWindow", "版本信息"))

