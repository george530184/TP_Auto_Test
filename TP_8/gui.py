# -*- coding: utf-8 -*-
__author__ = 'Jerry'

'''
GUI argument get from global_argu.py
'''

from PyQt5 import QtWidgets, QtCore
from gui_design import Ui_MainWindow
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from log_s import *
from main_run import Run
import sys,os
import configparser
import time
import global_argu


class gui_data(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None):
		super(gui_data, self).__init__(parent)
		self.setupUi(self)
		# 状态栏
		self.Zhuang_Tai_Lang.showMessage('Copyright © 2016-2017 CIG. All rights reserved.')
		# config.ini
		dir_tp = os.path.isdir('D:\Python_project\Pro\TP_8')
		if dir_tp is True:
			pass
		else:
			os.makedirs(r'D:\Python_project\Pro\TP_8')
		os.chdir('D:\Python_project\Pro\TP_8')
		file_data = os.path.isfile('D:\Python_project\Pro\TP_8\config.ini')
		if file_data is True:
			pass
		else:
			f = open('config.ini', 'w')
			f.close()
		config =configparser.ConfigParser()
		config['ap_config'] = {'ap_ip_config': '',
							   'ap_user_config': '',
							   'ap_passwd_config': '',
							   'channel_2_config': '',
							   'channel_5_config': '',
							   'ssid_2_config': '',
							   'ssid_5_config': '',
							   'choose_ap': ''
		}
		config['chariot_config'] = {'chariot_2g_pc_ip_config': '',
									'chariot_2g_sta_ip_config': '',
									'chariot_5g_pc_ip_config': '',
									'chariot_5g_sta_ip_config': '',
									'chariot_2g_duration_config': '',
									'chariot_2g_pair_config': '',
									'chariot_5g_duration_config': '',
									'chariot_5g_pair_config': ''

		}
		config['radiobutton_config'] = {'radio_button_2g_config': '',
										'radio_button_5g_config': ''
		}
		config['other_config'] = {'degree_config': '',
								  'distance_config': '',
								  'distance_config_2': '',
								  'band_config': '',
								  'band_config_2': '',
								  'start_s': '',
								  'ap_config_button': '',
								  'Game_Over': '0',   # flag 标志位 0：Running 1：Over
								  'stop_distance_flag': '0', # flag 标志位 0：Running 2：Over
								  'dis_flag': '0',  # flag 标志位 0：Default 1：dis[0] 2:dis[1]
								  'bssid': '' ,     # bssid for get sta rssi
								  'chariot_flag': '0' # flag标志位 0:Default 1:ok

		}
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
		# init logfile
		file_data = os.path.isfile('D:\Python_project\Pro\TP_8\log\Running.txt')
		if file_data is True:
			os.remove('D:\Python_project\Pro\TP_8\log\Running.txt')
		else:
			pass
		# init /log/tmp logfile
		os.chdir('D:\Python_project\Pro\TP_8\log\\tmp')
		file_data = os.path.isfile('D:\Python_project\Pro\TP_8\log\\tmp\RunX.txt')
		if file_data is True:
			os.remove('RunX.txt')
			f = open('RunX.txt', 'w')
			f.close()
		else:
			f = open('RunX.txt', 'w')
			f.close()
		file_data2 = os.path.isfile('D:\Python_project\Pro\TP_8\log\\tmp\Running.txt')
		if file_data2 is True:
			os.remove('D:\Python_project\Pro\TP_8\log\\tmp\Running.txt')
		else:
			pass
		# Single and Slot
		self.config_ap.clicked.connect(self.ap_config)
		self.start.clicked.connect(self.config_set)
		self.start.clicked.connect(self.log_show_messages)
		self.report.clicked.connect(self.report_show)
		if len(global_argu.Report_distance) == 2:
			self.start.clicked.connect(self.show_message)
		else:
			pass

	def ap_config(self):
		# AP config
		if self.AP_Type_Choose.currentText().strip() == 'CIG':
			ap_ip = self.AP_IP.text()
			ap_user = self.AP_User.text()
			ap_passwd = self.AP_Passwd.text()
			channel_2 = self.Channel_2.text()
			channel_5 = self.Channel_5.text()
			ssid_2 = self.SSID_2.text()
			ssid_5 = self.SSID_5.text()
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			# AP config
			conf.set('ap_config', 'ap_ip_config', ap_ip)
			conf.set('ap_config', 'ap_user_config', ap_user)
			conf.set('ap_config', 'ap_passwd_config', ap_passwd)
			conf.set('ap_config', 'channel_2_config', channel_2)
			conf.set('ap_config', 'channel_5_config', channel_5)
			conf.set('ap_config', 'ssid_2_config', ssid_2)
			conf.set('ap_config', 'ssid_5_config', ssid_5)
			conf.set('other_config', 'ap_config_button', '1')
			conf.set('other_config', 'start_s', '2')
			# radio_button
			# 2.4G
			if self.HT_20_2g.isChecked():
				conf.set('radiobutton_config', 'radio_button_2g_config', '0')
			elif self.HT40_down_2g.isChecked():
				conf.set('radiobutton_config', 'radio_button_2g_config', '1')
			elif self.HT_40_up_2g.isChecked():
				conf.set('radiobutton_config', 'radio_button_2g_config', '2')
			elif self.HT40_2g.isChecked():
				conf.set('radiobutton_config', 'radio_button_2g_config', '3')
			else:
				LogMsg(log.logger.error, 'No 2g HT_Button!!')
			# 5G
			if self.HT_20_5g.isChecked():
				conf.set('radiobutton_config', 'radio_button_5g_config', '0')
			elif self.HT40_down_5g.isChecked():
				conf.set('radiobutton_config', 'radio_button_5g_config', '1')
			elif self.HT40_up_5g.isChecked():
				conf.set('radiobutton_config', 'radio_button_5g_config', '2')
			elif self.HT40_5g.isChecked():
				conf.set('radiobutton_config', 'radio_button_5g_config', '3')
			elif self.HT80_5g.isChecked():
				conf.set('radiobutton_config', 'radio_button_5g_config', '4')
			else:
				LogMsg(log.logger.error, 'No 5g HT_Button!!')
			conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
			os.chdir('D:\Python_project\Pro\TP_8')
			from imp import reload
			import global_argu
			reload(global_argu)
			Run()
		else:
			LogMsg(log.logger.info, 'Not Supported Non CIG series AP Auto Config!')

	def report_show(self):
		os.system('start D:\iperf\iperf_result')

	def config_set(self):
		config =configparser.ConfigParser()
		config['ap_config'] = {'ap_ip_config': '',
							   'ap_user_config': '',
							   'ap_passwd_config': '',
							   'channel_2_config': '',
							   'channel_5_config': '',
							   'ssid_2_config': '',
							   'ssid_5_config': '',
							   'choose_ap': ''
		}
		config['chariot_config'] = {'chariot_2g_pc_ip_config': '',
									'chariot_2g_sta_ip_config': '',
									'chariot_5g_pc_ip_config': '',
									'chariot_5g_sta_ip_config': '',
									'chariot_2g_duration_config': '',
									'chariot_2g_pair_config': '',
									'chariot_5g_duration_config': '',
									'chariot_5g_pair_config': ''
		}
		config['radiobutton_config'] = {'radio_button_2g_config': '',
										'radio_button_5g_config': ''
		}
		config['other_config'] = {'degree_config': '',
								  'distance_config': '',
								  'distance_config_2': '',
								  'band_config': '',
								  'band_config_2': '',
								  'start_s': '',
								  'ap_config_button': '',
								  'Game_Over': '0',
								  'stop_distance_flag': '0',
								  'dis_flag': '0',
								  'bssid': '',
								  'chariot_flag': '0'

		}
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
		# AP config
		ap_ip = self.AP_IP.text()
		ap_user = self.AP_User.text()
		ap_passwd = self.AP_Passwd.text()
		channel_2 = self.Channel_2.text()
		channel_5 = self.Channel_5.text()
		ssid_2 = self.SSID_2.text()
		ssid_5 = self.SSID_5.text()
		# chariot config
		chariot_2g_pc_ip = self.chariot_pc_IP_2g.text()
		chariot_2g_sta_ip = self.chariot_sta_IP_2g.text()
		chariot_5g_pc_ip = self.chariot_pc_IP_5g.text()
		chariot_5g_sta_ip = self.chariot_sta_IP_5g.text()
		chariot_2g_duration = self.chariot_duration_2g.text()
		chariot_2g_pair = self.chariot_pair_2g.text()
		chariot_5g_duration = self.chariot_duration_5g.text()
		chariot_5g_pair = self.chariot_pair_5g.text()
		conf = configparser.ConfigParser()
		conf.read('D:\Python_project\Pro\TP_8\config.ini')
		conf.set('other_config', 'ap_config_button', '2')
		# AP config
		conf.set('ap_config', 'choose_ap', self.AP_Type_Choose.currentText().strip())
		conf.set('ap_config', 'ap_ip_config', ap_ip)
		conf.set('ap_config', 'ap_user_config', ap_user)
		conf.set('ap_config', 'ap_passwd_config', ap_passwd)
		conf.set('ap_config', 'channel_2_config', channel_2)
		conf.set('ap_config', 'channel_5_config', channel_5)
		conf.set('ap_config', 'ssid_2_config', ssid_2)
		conf.set('ap_config', 'ssid_5_config', ssid_5)
		# chariot config
		conf.set('chariot_config', 'chariot_2g_pc_ip_config', chariot_2g_pc_ip)
		conf.set('chariot_config', 'chariot_2g_sta_ip_config', chariot_2g_sta_ip)
		conf.set('chariot_config', 'chariot_5g_pc_ip_config', chariot_5g_pc_ip)
		conf.set('chariot_config', 'chariot_5g_sta_ip_config', chariot_5g_sta_ip)
		conf.set('chariot_config', 'chariot_2g_duration_config', chariot_2g_duration)
		conf.set('chariot_config', 'chariot_2g_pair_config', chariot_2g_pair)
		conf.set('chariot_config', 'chariot_5g_duration_config', chariot_5g_duration)
		conf.set('chariot_config', 'chariot_5g_pair_config', chariot_5g_pair)
		# radio_button
		# 2.4G
		if self.HT_20_2g.isChecked():
			conf.set('radiobutton_config', 'radio_button_2g_config', '0')
		elif self.HT40_down_2g.isChecked():
			conf.set('radiobutton_config', 'radio_button_2g_config', '1')
		elif self.HT_40_up_2g.isChecked():
			conf.set('radiobutton_config', 'radio_button_2g_config', '2')
		elif self.HT40_2g.isChecked():
			conf.set('radiobutton_config', 'radio_button_2g_config', '3')
		else:
			LogMsg(log.logger.error, 'No 2g HT_Button!!')
		# 5G
		if self.HT_20_5g.isChecked():
			conf.set('radiobutton_config', 'radio_button_5g_config', '0')
		elif self.HT40_down_5g.isChecked():
			conf.set('radiobutton_config', 'radio_button_5g_config', '1')
		elif self.HT40_up_5g.isChecked():
			conf.set('radiobutton_config', 'radio_button_5g_config', '2')
		elif self.HT40_5g.isChecked():
			conf.set('radiobutton_config', 'radio_button_5g_config', '3')
		elif self.HT80_5g.isChecked():
			conf.set('radiobutton_config', 'radio_button_5g_config', '4')
		else:
			LogMsg(log.logger.error, 'No 5g HT_Button!!')
		# degree
		if self.Degree_8.isChecked():
			conf.set('other_config', 'degree_config', '8')
		elif self.Degree_4.isChecked():
			conf.set('other_config', 'degree_config', '4')
		else:
			LogMsg(log.logger.error, 'NO Degree isChecked!')
		# other config
		# distance
		if self.D_10m_8.isChecked() or self.D_10m_4.isChecked():
			conf.set('other_config', 'distance_config', '10')
		else:
			conf.set('other_config', 'distance_config', '')
		if self.D_50m_8.isChecked() or self.D_50m_4.isChecked():
			conf.set('other_config', 'distance_config_2', '50')
		else:
			conf.set('other_config', 'distance_config_2', '')
		# Band
		if self.D_2g_8.isChecked() or self.D_2g_4.isChecked():
			conf.set('other_config', 'band_config', '2.4G')
		else:
			conf.set('other_config', 'band_config', '')
		if self.D_5g_8.isChecked() or self.D_5g_4.isChecked():
			conf.set('other_config', 'band_config_2', '5G')
		else:
			conf.set('other_config', 'band_config_2', '')
		conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		conf_singal = configparser.ConfigParser()
		conf_singal.read('D:\Python_project\Pro\TP_8\config.ini')
		conf_singal.set('other_config', 'start_s', '1')
		conf_singal.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		self.thread_conf = MyThread()
		self.thread_conf.start()

	def log_show_messages(self):
		self.thread2 = MyThread2()
		self.thread2.single_2.connect(self.log_show_2)
		self.thread2.start()

	def log_show_2(self):
		handler_show = FileEventHandler()
		handler_show.on_modified(self.log_text)

	def show_message(self):
		self.thread3 =MyThread3()
		self.thread3.single_3.connect(self.show_next_dis_message)
		self.thread3.start()

	def show_next_dis_message(self):
		rusult = QMessageBox.information(self, "Note", " Next Distance!！START???", QMessageBox.Ok)
		if rusult == QMessageBox.Ok:
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			conf.set('other_config', 'stop_distance_flag', '0')
			conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
			LogMsg(log.logger.info, 'OKOK')
		else:
			LogMsg(log.logger.info, 'SLEEP!!!!')


class MyThread(QThread):

	def __init__(self, parent=None):
		super(MyThread, self).__init__(parent)

	def run(self):
		from imp import reload
		import global_argu
		reload(global_argu)
		Run()


class MyThread2(QThread):
	single_2 = QtCore.pyqtSignal()

	def __init__(self):
		super(MyThread2, self).__init__()

	def run(self):
		LogMsg(log.logger.info, 'Start Running !')
		while True:
			time.sleep(1.5)
			self.single_2.emit()


class MyThread3(QThread):
	single_3 = QtCore.pyqtSignal()

	def __init__(self):
		super(MyThread3, self).__init__()

	def run(self):
		while True:
			time.sleep(1)
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			stop_dis = conf.get('other_config', 'stop_distance_flag')
			if stop_dis == '2':
				self.single_3.emit()
				break


if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	myshow =gui_data()
	myshow.show()
	sys.exit(app.exec_())














