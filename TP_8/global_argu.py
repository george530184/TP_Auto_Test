# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import configparser
import os
import sys

os.chdir('D:\Python_project\Pro\TP_8')
file_data = os.path.isfile('D:\Python_project\Pro\TP_8\config.ini')
if file_data is True:
	config = configparser.ConfigParser()
	config.read('D:\Python_project\Pro\TP_8\config.ini')
	# start
	sys_start = config.get('other_config', 'start_s')
	ap_configd = config.get('other_config', 'ap_config_button')
	Report_distanced = [config.get('other_config', 'distance_config')]
	Report_distanced.append(config.get('other_config', 'distance_config_2'))
	Report_distanced.sort()
	if Report_distanced[0] == '':
		Report_distanced.remove('')
	Report_distance = Report_distanced
	print(Report_distance)
	Report_band_d = [config.get('other_config', 'band_config')]
	Report_band_d.append(config.get('other_config', 'band_config_2'))
	Report_band_d.sort()
	if Report_band_d[0] == '':
		Report_band_d.remove('')
	Report_band = Report_band_d
	print(Report_band)
	dot11_2dg = '2.4G'
	dot11_5dg = '5G'
	degree = config.get('other_config', 'degree_config')
	check3 = '10'
	check4 = '50'
	# Chariot config
	Chariot_time = config.get('chariot_config', 'chariot_2g_duration_config')
	Chariot_time5 = config.get('chariot_config', 'chariot_5g_duration_config')
	Chariot_ip2 = config.get('chariot_config', 'chariot_2g_sta_ip_config')
	Chariot_ip5 = config.get('chariot_config', 'chariot_5g_sta_ip_config')
	# AP config
	AP_Type = config.get('ap_config', 'choose_ap')
	AP_host = config.get('ap_config', 'ap_ip_config')
	AP_User = config.get('ap_config', 'ap_user_config')
	AP_Passwd = config.get('ap_config', 'ap_passwd_config')
	AP_channel_2 = config.get('ap_config', 'channel_2_config')
	AP_channel_5 = config.get('ap_config', 'channel_5_config')

	'''
	ht20 is 0;ht40- is 1;ht40+ is 2;ht40 is 3;ht80 is 4
	only one argument
	'''
	AP_bandwidth_2 = [config.get('radiobutton_config', 'radio_button_2g_config')]
	if AP_bandwidth_2[0] == '0':
		AP_bd_2 = 'HT20'
	elif AP_bandwidth_2[0] == '1':
		AP_bd_2 = 'HT40-'
	elif AP_bandwidth_2[0] == '2':
		AP_bd_2 = 'HT40+'
	elif AP_bandwidth_2[0] == '3':
		AP_bd_2 = 'HT40'
	else:
		print('NO AP_bd_2')

	AP_bandwidth_5 = [config.get('radiobutton_config', 'radio_button_5g_config')]
	if AP_bandwidth_5[0] == '0':
		AP_bd_5 = 'HT20'
	elif AP_bandwidth_5[0] == '1':
		AP_bd_5 = 'HT40-'
	elif AP_bandwidth_5[0] == '2':
		AP_bd_5 = 'HT40+'
	elif AP_bandwidth_5[0] == '3':
		AP_bd_5 = 'HT40'
	elif AP_bandwidth_5[0] == '4':
		AP_bd_5 = 'HT80'
	else:
		print('NO AP_bd_5')
	AP_ssid_2 = config.get('ap_config', 'ssid_2_config')
	AP_ssid_5 = config.get('ap_config', 'ssid_5_config')
else:
	pass



