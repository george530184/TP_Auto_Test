# -*- coding: utf-8 -*-
__author__ = 'Jerry'

"""
auto config cig wifi sw
"""
from report_s import *
from log_s import *
from socket_c import *
import telnetlib
import time
import re
import datetime
import configparser
import global_argu


class Ap(object):
	# The default AP : CIG

	def __init__(self, host, username, password):
		self.host = host
		self.username = username
		self.password = password

	def config(self):
		LogMsg(log.logger.info, 'Config AP Now!')
		try:
			tn = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			tn.set_debuglevel(2)
			tn.read_until('Login as:'.encode('utf-8'))  # !str
			tn.write(self.username.encode('ascii')+b'\n')   # str
			tn.read_until('Password:'.encode('utf-8'))
			tn.write(self.password.encode('ascii')+b'\n')
			tn.read_until('AP>'.encode('utf-8'))
			tn.write('enable \n'.encode('ascii'))
			tn.read_until('#AP>'.encode('utf-8'))
			tn.write("system/wifi \n".encode('ascii'))
			tn.read_until('#AP/system/wifi>'.encode('utf-8'))
			# 2.4G
			tn.write(("basic 0 1 %s 1 %s 0 \n" % (global_argu.AP_channel_2, global_argu.AP_bandwidth_2[0])).encode('ascii'))
			tn.read_until('#AP/system/wifi>'.encode('utf-8'))
			tn.write(("ssid 0 0 1 %s \n" % global_argu.AP_ssid_2).encode('ascii'))
			tn.read_until('#AP/system/wifi>'.encode('utf-8'))
			tn.write("sec 0 0 3 0 0 \n".encode('ascii'))
			time.sleep(1)
			# 5G
			tn.read_until('#AP/system/wifi>'.encode('utf-8'))
			tn.write(('basic 1 1 %s 8 %s 0 \n' % (global_argu.AP_channel_5 , global_argu.AP_bandwidth_5[0])).encode('ascii'))
			tn.read_until('#AP/system/wifi>'.encode('utf-8'))
			tn.write(('ssid 1 0 1 %s \n' % global_argu.AP_ssid_5).encode('ascii'))
			tn.read_until('#AP/system/wifi>'.encode('utf-8'))
			tn.write('sec 1 0 3 0 0 \n'.encode('ascii'))
			# Close Telnet
			tn.read_until('#AP/system/wifi>'.encode('utf-8'))
			tn.write('x \n'.encode('ascii'))
			tn.read_until('#AP/system>'.encode('utf-8'))
			tn.write('x \n'.encode('ascii'))
			tn.read_until('#AP>'.encode('utf-8'))
			tn.close()
			# Log to GUI
			LogMsg(log.logger.info, 'Config AP Successfully!')

		except Exception as e:
			LogMsg(log.logger.error, 'Config AP: Telnet ERROR!')

	def state_2g(self, a):
		try:
			time.sleep(int(global_argu.Chariot_time)/2)
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('Login as:'.encode('utf-8'))  # !str
			t.write(self.username.encode('ascii')+b'\n')   # str
			t.read_until('Password:'.encode('utf-8'))
			t.write(self.password.encode('ascii')+b'\n')
			t.read_until('AP>'.encode('utf-8'))
			t.write('enable \n'.encode('ascii'))
			t.read_until('#AP>'.encode('utf-8'))
			t.write('system/shell \n'.encode('ascii'))
			t.read_until('#AP/system/shell>'.encode('utf-8'))
			# 2.4G TxRate RxRate Rssi
			t.write('wlanconfig ath0 list \n'.encode('ascii'))
			ret = t.read_until('#AP/system/shell>'.encode('utf-8'))
			print(ret)
			# re
			TxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[0].decode('utf-8')[:-1]
			RxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[1].decode('utf-8')[:-1]
			Rssi = re.findall(r'\s(\d+)\s'.encode('utf-8'), ret)[2].decode('utf-8')
			print(TxRate)
			LogMsg(log.logger.info, "TxRate is: %s" % TxRate)
			LogMsg(log.logger.info, "Rssi is: %s" % Rssi)
			if global_argu.degree == '8' or global_argu.degree == '4':
				result_2g = report(global_argu.Report_distance, None, None, Rssi, TxRate, None, None, global_argu.dot11_2dg, None)
				result_2g.degree_report(int(a))
			else:
				LogMsg(log.logger.error, 'state_2g: degree ERROR!')
			# close
			t.write('x \n'.encode('ascii'))
			t.read_until('#AP/system>'.encode('utf-8'))
			t.write('x \n'.encode('ascii'))
			t.read_until('#AP>'.encode('utf-8'))
			t.close()
		except Exception as e:
			LogMsg(log.logger.error, 'state_2g: Telnet ERROR!')

	def state_5g(self, a):
		try:
			time.sleep(int(global_argu.Chariot_time5)/2)
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('Login as:'.encode('utf-8'))  # !str
			t.write(self.username.encode('ascii')+b'\n')   # str
			t.read_until('Password:'.encode('utf-8'))
			t.write(self.password.encode('ascii')+b'\n')
			t.read_until('AP>'.encode('utf-8'))
			t.write('enable \n'.encode('ascii'))
			t.read_until('#AP>'.encode('utf-8'))
			t.write('system/shell \n'.encode('ascii'))
			t.read_until('#AP/system/shell>'.encode('utf-8'))
			# 5G TxRate RxRate Rssi
			t.write('wlanconfig ath16 list \n'.encode('ascii'))
			ret = t.read_until('#AP/system/shell>'.encode('utf-8'))
			print(ret)
			# re
			TxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[0].decode('utf-8')[:-1]
			RxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[1].decode('utf-8')[:-1]
			Rssi = re.findall(r'\s(\d+)\s'.encode('utf-8'), ret)[2].decode('utf-8')
			print(TxRate)
			LogMsg(log.logger.info, "TxRate is: %s" % TxRate)
			LogMsg(log.logger.info, "Rssi is: %s" % Rssi)
			if global_argu.degree == '8' or global_argu.degree == '4':
				result_5g = report(global_argu.Report_distance, None, None, Rssi, TxRate, None, None, None, global_argu.dot11_5dg)
				result_5g.degree_report(int(a))
			else:
				LogMsg(log.logger.error, 'state_5g: degree ERROR!')
			# close
			t.write('x \n'.encode('ascii'))
			t.read_until('#AP/system>'.encode('utf-8'))
			t.write('x \n'.encode('ascii'))
			t.read_until('#AP>'.encode('utf-8'))
			t.close()
		except Exception as e:
			LogMsg(log.logger.error, 'state_5g: Telnet ERROR!')

	def get_bssid_2g(self):
		try:
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('Login as:'.encode('utf-8'))  # !str
			t.write(self.username.encode('ascii')+b'\n')   # str
			t.read_until('Password:'.encode('utf-8'))
			t.write(self.password.encode('ascii')+b'\n')
			t.read_until('AP>'.encode('utf-8'))
			t.write('enable \n'.encode('ascii'))
			t.read_until('#AP>'.encode('utf-8'))
			t.write('system/shell \n'.encode('ascii'))
			t.read_until('#AP/system/shell>'.encode('utf-8'))
			t.write('iwconfig ath0 \n'.encode('ascii'))
			ret = t.read_until('#AP/system/shell>'.encode('utf-8'))
			print(ret)
			bssid = re.findall(r'[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}'.encode('utf-8'), ret)[0].decode('utf-8')
			LogMsg(log.logger.info, bssid)
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			conf.set('other_config', 'bssid', bssid)
			conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		except Exception as e:
			LogMsg(log.logger.error, 'get_bssid_2g: Telnet ERROR!')

	def get_bssid_5g(self):
		try:
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('Login as:'.encode('utf-8'))  # !str
			t.write(self.username.encode('ascii')+b'\n')   # str
			t.read_until('Password:'.encode('utf-8'))
			t.write(self.password.encode('ascii')+b'\n')
			t.read_until('AP>'.encode('utf-8'))
			t.write('enable \n'.encode('ascii'))
			t.read_until('#AP>'.encode('utf-8'))
			t.write('system/shell \n'.encode('ascii'))
			t.read_until('#AP/system/shell>'.encode('utf-8'))
			t.write('iwconfig ath16 \n'.encode('ascii'))
			ret = t.read_until('#AP/system/shell>'.encode('utf-8'))
			print(ret)
			bssid = re.findall(r'[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}'.encode('utf-8'), ret)[0].decode('utf-8')
			LogMsg(log.logger.info, bssid)
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			conf.set('other_config', 'bssid', bssid)
			conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		except Exception as e:
			LogMsg(log.logger.error, 'get_bssid_5g: Telnet ERROR!')


class ActonTech(object):
	def __init__(self, host, username, password):
		self.host = host
		self.username = username
		self.password = password

	def state_2g(self, a):
		pass

	def state_5g(self, a):
		pass

	def get_bssid_2g(self):
		pass

	def get_bssid_5g(self):
		pass


class Nokia_1931(object):
	# Nokia_1931 only need host to telnet

	def __init__(self, host, username, password):
		self.host = host
		self.username = username
		self.password = password

	def state_2g(self, a):
		try:
			time.sleep(int(global_argu.Chariot_time)/2)
			sock_2 = socket_c(global_argu.Chariot_ip2)
			sock_2.socket_2g(a)
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
			t.write('wlanconfig ath1 list \n'.encode('ascii'))  # str
			ret = t.read_until('root@OpenWrt:/#'.encode('utf-8'))
			print(ret)
			# re
			TxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[0].decode('utf-8')[:-1]
			RxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[1].decode('utf-8')[:-1]
			Rssi = re.findall(r'\s(\d+)\s'.encode('utf-8'), ret)[2].decode('utf-8')
			print(TxRate)
			LogMsg(log.logger.info, "TxRate is: %s" % TxRate)
			LogMsg(log.logger.info, "Rssi is: %s" % Rssi)
			if global_argu.degree == '8' or global_argu.degree == '4':
				result_5g = report(global_argu.Report_distance, None, None, Rssi, TxRate, None, None, global_argu.dot11_2dg, None)
				result_5g.degree_report(int(a))
			else:
				LogMsg(log.logger.error, 'state_2g: degree ERROR!')
			# close
			t.write('exit \n'.encode('ascii'))
			t.close()
		except Exception as e:
			LogMsg(log.logger.error, 'state_2g: Telnet ERROR!')

	def state_5g(self, a):
		try:
			time.sleep(int(global_argu.Chariot_time5)/2)
			sock_5 = socket_c(global_argu.Chariot_ip5)
			sock_5.socket_5g(a)
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
			t.write('wlanconfig ath0 list \n'.encode('ascii'))  # str
			ret = t.read_until('root@OpenWrt:/#'.encode('utf-8'))
			print(ret)
			# re
			TxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[0].decode('utf-8')[:-1]
			RxRate = re.findall(r'\s(\d+M)\s'.encode('utf-8'), ret)[1].decode('utf-8')[:-1]
			Rssi = re.findall(r'\s(\d+)\s'.encode('utf-8'), ret)[2].decode('utf-8')
			print(TxRate)
			LogMsg(log.logger.info, "TxRate is: %s" % TxRate)
			LogMsg(log.logger.info, "Rssi is: %s" % Rssi)
			if global_argu.degree == '8' or global_argu.degree == '4':
				result_5g = report(global_argu.Report_distance, None, None, Rssi, TxRate, None, None, None, global_argu.dot11_5dg)
				result_5g.degree_report(int(a))
			else:
				LogMsg(log.logger.error, 'state_5g: degree ERROR!')
			# close
			t.write('exit \n'.encode('ascii'))
			t.close()
		except Exception as e:
			LogMsg(log.logger.error, 'state_5g: Telnet ERROR!')

	def get_bssid_2g(self):
		try:
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
			t.write('iwconfig ath1 \n'.encode('ascii'))
			ret = t.read_until('root@OpenWrt:/#'.encode('utf-8'))
			print(ret)
			bssid = re.findall(r'[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}'.encode('utf-8'), ret)[0].decode('utf-8')
			LogMsg(log.logger.info, bssid)
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			conf.set('other_config', 'bssid', bssid)
			conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		except Exception as e:
			LogMsg(log.logger.error, 'get_bssid_2g: Telnet ERROR!')

	def get_bssid_5g(self):
		try:
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
			t.write('iwconfig ath0 \n'.encode('ascii'))
			ret = t.read_until('root@OpenWrt:/#'.encode('utf-8'))
			print(ret)
			bssid = re.findall(r'[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}'.encode('utf-8'), ret)[0].decode('utf-8')
			LogMsg(log.logger.info, bssid)
			conf = configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			conf.set('other_config', 'bssid', bssid)
			conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		except Exception as e:
			LogMsg(log.logger.error, 'get_bssid_5g: Telnet ERROR!')

if __name__ == '__main__':
	hostd = '192.168.1.1'
	usrd = 'admin'
	passd = 'password'
	p = Nokia_1931(hostd, usrd, passd)
	q = '1'
	# p.state_2g(q) # Get 2.4G TxRate Rssi
	# p.state_5g(q) # Get 5G   TxRate Rssi
	p.get_bssid_5g()





