# -*- coding: utf-8 -*-
__author__ = 'Jerry'
from log_s import *
from socket_c import *
from Ap import *
from report_s import *
import sys
sys.coinit_flags = 0
import pythoncom
import os
import re
import configparser
import win32com.client


class Chariot(object):
	def __init__(self):
		pass

	def run_2g(self, j):
		# check tclsh86
		pythoncom.CoInitialize()
		WMI = win32com.client.GetObject('winmgmts:')
		processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="tclsh86.exe"')
		if len(processCodeCov) > 0:
			LogMsg(log.logger.info, 'process tclsh86.exe is exit!!!')
			os.system('TASKKILL /F /IM tclsh86.exe')
		else:
			pass
		pythoncom.CoUninitialize()
		# threading: get sta rssi
		if global_argu.AP_Type == 'CIG':
			ap = Ap(global_argu.AP_host, global_argu.AP_User, global_argu.AP_Passwd)
			ap.get_bssid_2g()
			sock_2 = socket_c(global_argu.Chariot_ip2)
			sock_2.socket_2g(j)
		else:
			pass
		# run chariot
		directory = os.path.exists('D:\\testtools\IxChariot')
		if directory is True:
			os.chdir('D:\\testtools\IxChariot')
			file = os.path.isfile('D:\\testtools\IxChariot\\throughput_2.tcl')
			if file is True:
				LogMsg(log.logger.info, 'Start Running IxChariot Now!')
				os.system('tclsh86 throughput_2.tcl')
				time.sleep(2)
				os.chdir('D:\Python_project\Pro\TP_8\iperflog\MyResults')
				os.rename('2g_Tx.tst', 'Throughput_2g_Tx_[{0}].tst'.format(j))
				os.rename('2g_Rx.tst', 'Throughput_2g_Rx_[{0}].tst'.format(j))
				os.rename('2g_Tx.txt', 'Throughput_2g_Tx_[{0}].txt'.format(j))
				os.rename('2g_Rx.txt', 'Throughput_2g_Rx_[{0}].txt'.format(j))
				LogMsg(log.logger.info, 'IxChariot Running OK!')
				LogMsg(log.logger.info, 'Change chariot_flag to 1')
				conf = configparser.ConfigParser()
				conf.read('D:\Python_project\Pro\TP_8\config.ini')
				conf.set('other_config', 'chariot_flag', '1')
				conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))

	def run_5g(self, j):
		# check tclsh86
		pythoncom.CoInitialize()
		WMI = win32com.client.GetObject('winmgmts:')
		processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="tclsh86.exe"')
		if len(processCodeCov) > 0:
			LogMsg(log.logger.info, 'process tclsh86.exe is exit!!!')
			os.system('TASKKILL /F /IM tclsh86.exe')
		else:
			pass
		pythoncom.CoUninitialize()
		# threading: get sta rssi
		if global_argu.AP_Type == 'CIG':
			ap = Ap(global_argu.AP_host, global_argu.AP_User, global_argu.AP_Passwd)
			ap.get_bssid_5g()
			sock_5 = socket_c(global_argu.Chariot_ip5)
			sock_5.socket_5g(j)
		else:
			pass
		# run chariot
		directory = os.path.exists('D:\\testtools\IxChariot')
		if directory is True:
			os.chdir('D:\\testtools\IxChariot')
			file = os.path.isfile('D:\\testtools\IxChariot\\throughput_5.tcl')
			if file is True:
				LogMsg(log.logger.info, 'Start Running IxChariot Now!')
				os.system('tclsh86 throughput_5.tcl')
				time.sleep(2)
				os.chdir('D:\Python_project\Pro\TP_8\iperflog\MyResults')
				os.rename('5g_Tx.tst', 'Throughput_5g_Tx_[{0}].tst'.format(j))
				os.rename('5g_Rx.tst', 'Throughput_5g_Rx_[{0}].tst'.format(j))
				os.rename('5g_Tx.txt', 'Throughput_5g_Tx_[{0}].txt'.format(j))
				os.rename('5g_Rx.txt', 'Throughput_5g_Rx_[{0}].txt'.format(j))
				LogMsg(log.logger.info, 'IxChariot Running OK!')
				LogMsg(log.logger.info, 'Change chariot_flag to 1')
				conf = configparser.ConfigParser()
				conf.read('D:\Python_project\Pro\TP_8\config.ini')
				conf.set('other_config', 'chariot_flag', '1')
				conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))

	def get_data_2g(self, j):
		while True:
			pythoncom.CoInitialize()
			WMI = win32com.client.GetObject('winmgmts:')
			processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="WerFault.exe"')
			if len(processCodeCov) > 0:
				LogMsg(log.logger.info, 'process WerFault is exit!!!')
				os.system('TASKKILL /F /IM WerFault.exe')
				pythoncom.CoUninitialize()
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			chariot_flag = conf.get('other_config', 'chariot_flag')
			if chariot_flag == '1':
				break
			time.sleep(1)
		f = open('D:\Python_project\Pro\TP_8\iperflog\MyResults\Throughput_2g_Tx_[{0}].txt'.format(j))
		ret = f.read()
		Tx = re.findall(r'Totals:\s+\d.+', ret)[0].split()[1]
		LogMsg(log.logger.info, "Tx is: %s" % Tx)
		f2 = open('D:\Python_project\Pro\TP_8\iperflog\MyResults\Throughput_2g_Rx_[{0}].txt'.format(j))
		ret2 = f2.read()
		Rx = re.findall(r'Totals:\s+\d.+', ret2)[0].split()[1]
		LogMsg(log.logger.info, "Rx is: %s" % Rx)
		# Get Tx Rx set flag 0
		conf = configparser.ConfigParser()
		conf.read('D:\Python_project\Pro\TP_8\config.ini')
		conf.set('other_config', 'chariot_flag', '0')
		conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		LogMsg(log.logger.info, 'Change chariot_flag to 0')
		# write to excel
		if global_argu.degree == '8' or global_argu.degree == '4':
			result_2g = report(global_argu.Report_distance, Tx, Rx, None, None, None, None, global_argu.dot11_2dg, None)
			result_2g.degree_report(int(j))
			f.close()
			f2.close()
		else:
			LogMsg(log.logger.error, 'Chariot_2g: Degree ERROR')
			f.close()
			f2.close()

	def get_data_5g(self, j):
		while True:
			pythoncom.CoInitialize()
			WMI = win32com.client.GetObject('winmgmts:')
			processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="WerFault.exe"')
			if len(processCodeCov) > 0:
				LogMsg(log.logger.info, 'process is exit!!!')
				os.system('TASKKILL /F /IM WerFault.exe')
			pythoncom.CoUninitialize()
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			chariot_flag = conf.get('other_config', 'chariot_flag')
			if chariot_flag == '1':
				break
			time.sleep(1)
		f = open('D:\Python_project\Pro\TP_8\iperflog\MyResults\Throughput_5g_Tx_[{0}].txt'.format(j))
		ret = f.read()
		Tx = re.findall(r'Totals:\s+\d.+', ret)[0].split()[1]
		LogMsg(log.logger.info, "Tx is: %s" % Tx)
		f2 = open('D:\Python_project\Pro\TP_8\iperflog\MyResults\Throughput_5g_Rx_[{0}].txt'.format(j))
		ret2 = f2.read()
		Rx = re.findall(r'Totals:\s+\d.+', ret2)[0].split()[1]
		LogMsg(log.logger.info, "Rx is: %s" % Rx)
		conf = configparser.ConfigParser()
		conf.read('D:\Python_project\Pro\TP_8\config.ini')
		conf.set('other_config', 'chariot_flag', '0')
		conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		LogMsg(log.logger.info, 'Change chariot_flag to 0')
		if global_argu.degree == '8' or global_argu.degree == '4':
			result_2g = report(global_argu.Report_distance, Tx, Rx, None, None, None, None, None, global_argu.dot11_5dg)
			result_2g.degree_report(int(j))
			f.close()
			f2.close()
		else:
			LogMsg(log.logger.error, 'Chariot_5g: Degree ERROR')
			f.close()
			f2.close()




