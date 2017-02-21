# -*- coding: utf-8 -*-
__author__ = 'Jerry'

"""
iperf test, iperf_64
"""
import os
import re
import datetime
import time
import global_argu
from report_s import *
from log_s import *
import configparser


class iperf(object):

	def __init__(self, ip2, ip5,  parallel, time, interval):
		self.ip2 = ip2
		self.ip5 = ip5
		self.parallel = parallel
		self.time = time
		self.interval = interval

	def iperf_test_2g(self, j):
		directory = os.path.exists('D:\Python_project\Pro\TP_8\iperf3_64')
		if directory is True:
			os.chdir('D:\Python_project\Pro\TP_8\iperf3_64')
			file = os.path.isfile('D:\Python_project\Pro\TP_8\iperf3_64\iperf3.exe')
			if file is True:
				LogMsg(log.logger.info, 'Iperf: Running 2.4G_Tx')
				os.system('iperf3.exe -c %s -P %s -t %s -i %s >D:\Python_project\Pro\TP_8\iperflog\iperflog2_Tx[%s].txt' % (self.ip2, self.parallel, self.time, self.interval, j))
				time.sleep(1)
				LogMsg(log.logger.info, 'Iperf: Running 2.4G_Rx')
				os.chdir('D:\Python_project\Pro\TP_8\iperf3_64')
				os.system('iperf3.exe -c %s -P %s -t %s -i %s -R >D:\Python_project\Pro\TP_8\iperflog\iperflog2_Rx[%s].txt' % (self.ip2, self.parallel, self.time, self.interval, j))
				# Log to Gui
				LogMsg(log.logger.info, 'Iperf Running OK!')
				LogMsg(log.logger.info, 'Change iperf_flag to 1')
				conf =configparser.ConfigParser()
				conf.read('D:\Python_project\Pro\TP_8\config.ini')
				conf.set('other_config', 'iperf_flag', '1')
				conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))

			else:
				LogMsg(log.logger.error, 'iperf_test_2g: NO File!')
		else:
			LogMsg(log.logger.error, 'iperf_test_2g: NO Directory')

	def iperf_test_5g(self, j):
		directory = os.path.exists('D:\Python_project\Pro\TP_8\iperf3_64')
		if directory is True:
			os.chdir('D:\Python_project\Pro\TP_8\iperf3_64')
			file = os.path.isfile('D:\Python_project\Pro\TP_8\iperf3_64\iperf3.exe')
			if file is True:
				LogMsg(log.logger.info, 'Iperf: Running 5G_TX')
				os.system('iperf3.exe -c %s -P %s -t %s -i %s >D:\Python_project\Pro\TP_8\iperflog\iperflog5_Tx[%s].txt' % (self.ip5, self.parallel, self.time, self.interval, j))
				time.sleep(1)
				LogMsg(log.logger.info, 'Iperf: Running 5G_RX')
				os.chdir('D:\Python_project\Pro\TP_8\iperf3_64')
				os.system('iperf3.exe -c %s -P %s -t %s -i %s -R >D:\Python_project\Pro\TP_8\iperflog\iperflog5_Rx[%s].txt' % (self.ip5, self.parallel, self.time, self.interval, j))
				# Log to Gui
				LogMsg(log.logger.info, 'Iperf Running OK')
				LogMsg(log.logger.info, 'Change iperf_flag to 1')
				conf =configparser.ConfigParser()
				conf.read('D:\Python_project\Pro\TP_8\config.ini')
				conf.set('other_config', 'iperf_flag', '1')
				conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))

			else:
				LogMsg(log.logger.error, 'iperf_test_5g: NO File!')
		else:
			LogMsg(log.logger.error, 'iperf_test_5g: NO Directory')

	def iperf_state_2g(self, j):
		while True:
			conf =configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			ipef_flag = conf.get('other_config', 'iperf_flag')
			if ipef_flag == '1':
				break
			time.sleep(1)
		f = open('D:\Python_project\Pro\TP_8\iperflog\iperflog2_Tx[%s].txt' %j)
		ret = f.read()
		sum = len(re.findall(r'\[SUM\]', ret))
		# tx = re.findall(r'\[SUM\]\s+\d.+', ret)[(sum//2)-1].split()[-2:]
		tx = re.findall(r'\[SUM\]\s+\d.+', ret)[sum-1].split()[-3:-2]
		# TX = " ".join(tx)
		LogMsg(log.logger.info, tx[0])
		f_2 = open('D:\Python_project\Pro\TP_8\iperflog\iperflog2_Rx[%s].txt' %j)
		ret = f_2.read()
		sum = len(re.findall(r'\[SUM\]', ret))
		rx = re.findall(r'\[SUM\]\s+\d.+', ret)[sum-1].split()[-3:-2]
		# RX = " ".join(rx)
		LogMsg(log.logger.info, rx[0])
		if global_argu.degree == '8' or global_argu.degree == '4':
			result_2g = report(global_argu.Report_distance, tx[0], rx[0], None, None, None, None, global_argu.dot11_2dg, None)
			result_2g.degree_report(int(j))
			f.close()
			f_2.close()
		else:
			LogMsg(log.logger.error, 'iperf_state_2g: Degree ERROR')
			f.close()
			f_2.close()
		# when finish ,flag == 0
		conf =configparser.ConfigParser()
		conf.read('D:\Python_project\Pro\TP_8\config.ini')
		conf.set('other_config', 'iperf_flag', '0')
		conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		LogMsg(log.logger.info, 'Change iperf_flag to 0')

	def iperf_state_5g(self, j):
		while True:
			conf =configparser.ConfigParser()
			conf.read('D:\Python_project\Pro\TP_8\config.ini')
			ipef_flag = conf.get('other_config', 'iperf_flag')
			if ipef_flag == '1':
				break
			time.sleep(1)
		f = open('D:\Python_project\Pro\TP_8\iperflog\iperflog5_Tx[%s].txt' %j)
		ret = f.read()
		sum = len(re.findall(r'\[SUM\]', ret))
		# tx = re.findall(r'\[SUM\]\s+\d.+', ret)[(sum//2)-1].split()[-2:]
		tx = re.findall(r'\[SUM\]\s+\d.+', ret)[sum-1].split()[-3:-2]
		# TX = " ".join(tx)
		LogMsg(log.logger.info, tx[0])
		f_5 = open('D:\Python_project\Pro\TP_8\iperflog\iperflog5_Rx[%s].txt' %j)
		ret = f_5.read()
		sum = len(re.findall(r'\[SUM\]', ret))
		rx = re.findall(r'\[SUM\]\s+\d.+', ret)[sum-1].split()[-3:-2]
		# RX = " ".join(rx)
		LogMsg(log.logger.info, rx[0])
		if global_argu.degree == '8' or global_argu.degree == '4':
			result_5g = report(global_argu.Report_distance, tx[0], rx[0], None, None, None, None, None, global_argu.dot11_5dg)
			result_5g.degree_report(int(j))
			f.close()
			f_5.close()
		else:
			LogMsg(log.logger.error, 'iperf_state_5g: Degree ERROR')
			f.close()
			f_5.close()
		# when finish ,flag == 0
		conf =configparser.ConfigParser()
		conf.read('D:\Python_project\Pro\TP_8\config.ini')
		conf.set('other_config', 'iperf_flag', '0')
		conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
		LogMsg(log.logger.info, 'Change iperf_flag to 0')


if __name__ == '__main__':
	ips2 = '192.168.188.20'
	ips5 = '127.0.0.1'
	times = 15
	parallels = 8
	intervals = 15
	p = iperf(ips2, ips5,  parallels, times, intervals)
	#p.iperf_test_2g(1)
	p.iperf_state_2g(0)
	#p.iperf_state_5g(2)
