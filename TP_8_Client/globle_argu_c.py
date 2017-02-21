# -*- coding: utf-8 -*-
__author__ = 'Jerry'

import configparser
import os

os.chdir('D:\Python_project\Pro\TP_8_Client')
file_data = os.path.isfile('D:\Python_project\Pro\TP_8_Client\config.ini')
if file_data is True:
	config = configparser.ConfigParser()
	config.read('D:\Python_project\Pro\TP_8_Client\config.ini')
	STA_IP = config.get('basic', 'sta_ip')
	STA_TYPE = config.get('basic', 'sta_type')
else:
	pass