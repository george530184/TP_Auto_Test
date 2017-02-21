# -*- coding: utf-8 -*-
__author__ = 'Jerry'
from report_s import *
from log_s import *
import socket
import sys
import configparser
import global_argu


class socket_c(object):

	def __init__(self, HOST):
		self.HOST = HOST

	def socket_2g(self, a):
		BUF_SIZE = 1024
		BSSID = ''.encode(encoding='utf-8')
		if global_argu.AP_Type == 'CIG':
			config = configparser.ConfigParser()
			config.read('D:\Python_project\Pro\TP_8\config.ini')
			bssid = [config.get('other_config', 'bssid')]
			BSSID = bssid[0].encode(encoding='utf-8')
		elif global_argu.AP_Type == 'NOKIA_1931':
			BSSID = '2'.encode(encoding='utf-8')
			print(BSSID)
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			LogMsg(log.logger.error, 'Create Socket ERROR')
			sys.exit()
		try:
			s.connect((self.HOST, 5252))
		except socket.error:
			LogMsg(log.logger.error, 'Connect Remote Host ERROR!')
			sys.exit()
		try:
			s.sendall(BSSID)
		except socket.error:
			LogMsg(log.logger.error, 'Send Message ERROR!')
			sys.exit()
		print("s is {0}".format(s))
		data = s.recv(BUF_SIZE).decode()
		LogMsg(log.logger.info, "Sta_Rssi is: %s" % data)
		# write to excel
		if global_argu.degree == '8' or global_argu.degree == '4':
			result_Rssi = report(global_argu.Report_distance, None, None, None, None, data, global_argu.Chariot_time, global_argu.dot11_2dg, None)
			result_Rssi.degree_report(int(a))
		else:
			LogMsg(log.logger.error, 'Socket_2g: Degree ERROR!')
		s.close()

	def socket_5g(self, a):
		BUF_SIZE = 1024
		BSSID = ''.encode(encoding='utf-8')
		if global_argu.AP_Type == 'CIG':
			config = configparser.ConfigParser()
			config.read('D:\Python_project\Pro\TP_8\config.ini')
			bssid = [config.get('other_config', 'bssid')]
			BSSID = bssid[0].encode(encoding='utf-8')
		elif global_argu.AP_Type == 'NOKIA_1931':
			BSSID = '5'.encode(encoding='utf-8')
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			LogMsg(log.logger.error, 'Create Socket ERROR')
			sys.exit()
		try:
			s.connect((self.HOST, 5252))
		except socket.error:
			LogMsg(log.logger.error, 'Connect Remote Host ERROR!')
			sys.exit()
		try:
			s.send(BSSID)
		except socket.error:
			LogMsg(log.logger.error, 'Send Message ERROR!')
			sys.exit()
		data = s.recv(BUF_SIZE).decode()
		LogMsg(log.logger.info, "STA_Rssi is: %s" % data)
		# write to excel
		if global_argu.degree == '8' or global_argu.degree == '4':
			result_Rssi = report(global_argu.Report_distance, None, None, None, None, data, global_argu.Chariot_time5, None, global_argu.dot11_5dg)
			result_Rssi.degree_report(int(a))
		else:
			LogMsg(log.logger.error, 'Socket_5g: Degree ERROR!')
		s.close()

if __name__ == '__main__':
	HOST = '127.0.0.1'
	sk = socket_c(HOST)
	sk.socket_2g(1)