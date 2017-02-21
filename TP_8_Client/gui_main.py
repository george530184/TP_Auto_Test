# -*- coding: utf-8 -*-
__author__ = 'Jerry'
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from gui_c import Ui_widget
import sys
import os
import configparser
from log_c import *
from main_c import run


class Gui_Thread(QThread):

	def __init__(self):
		super(Gui_Thread, self).__init__()

	def run(self):
		from imp import reload
		import globle_argu_c
		reload(globle_argu_c)
		run()


class Gui_Thread_2(QThread):
	Single_ = pyqtSignal()

	def __init__(self):
		super(Gui_Thread_2, self).__init__()

	def run(self):
		while True:
			time.sleep(1)
			self.Single_.emit()


class Gui_Main(QtWidgets.QWidget, Ui_widget):
	def __init__(self, parent=None):
		super(Gui_Main, self).__init__(parent)
		self.setupUi(self)
		dir_tp = os.path.isdir('D:\Python_project\Pro\TP_8_Client')
		if dir_tp is True:
			pass
		else:
			os.makedirs(r'D:\Python_project\Pro\TP_8_Client')
		file_data = os.path.isfile('D:\Python_project\Pro\TP_8_Client\config.ini')
		if file_data is True:
			pass
		else:
			f = open('config.ini', 'w')
			f.close()
		config = configparser.ConfigParser()
		config['basic'] = {'sta_ip': '',
						   'sta_type':''

		}
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
		self.start.clicked.connect(self.start_pro)
		self.start.clicked.connect(self.log_show_message)

	def start_pro(self):
		config = configparser.ConfigParser()
		config.read('D:\Python_project\Pro\TP_8_Client\config.ini')
		sta_ip = self.sta_ip_host.text()
		config.set('basic', 'sta_ip', sta_ip)
		config.set('basic', 'sta_type', self.sta_rssi_choose.currentText().strip())
		config.write(open('D:\Python_project\Pro\TP_8_Client\config.ini', 'w'))
		self.threads = Gui_Thread()
		self.threads.start()

	def log_show_message(self):
		self.thread = Gui_Thread_2()
		self.thread.Single_.connect(self.log_show_2)
		self.thread.start()

	def log_show_2(self):
		handler_show = FileEventHandler()
		handler_show.on_modified(self.log_show)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myshow =Gui_Main()
	myshow.show()
	sys.exit(app.exec_())


