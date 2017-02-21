# -*- coding: utf-8 -*-
__author__ = 'Jerry'

from Emachine import *
from PyQt5 import QtWidgets
from chariot import *
from Ap import *
from report_s import *
from shutil import copyfile
import os
import threading
import time
import telnetlib
import re
import shutil
import sys
import pythoncom
import win32com.client
import configparser
from log_s import *
import global_argu


def run_2(j):
	# Running 2.4G
	chariot_run_2 = Chariot()
	aps_2 = Ap(global_argu.AP_host, global_argu.AP_User, global_argu.AP_Passwd)
	aps_2_1931 =Nokia_1931(global_argu.AP_host, global_argu.AP_User, global_argu.AP_Passwd)
	threads = []
	t1 = threading.Thread(target=chariot_run_2.run_2g, args=(j,))
	threads.append(t1)
	# Choose AP
	if global_argu.AP_Type == 'CIG':
		t2 = threading.Thread(target=aps_2.state_2g, args=(j,))
	elif global_argu.AP_Type == 'NOKIA_1931':
		t2 = threading.Thread(target=aps_2_1931.state_2g, args=(j,))
	else:
		LogMsg(log.logger.info, 'NO AP_TYPE Choose!')
	threads.append(t2)
	t3 = threading.Thread(target=chariot_run_2.get_data_2g, args=(j,))
	threads.append(t3)
	for t in threads:
		t.start()
	t1.join()
	t2.join()
	t3.join()
	time.sleep(10)


def run_5(j):
	chariot_run_5 = Chariot()
	aps_5 = Ap(global_argu.AP_host, global_argu.AP_User, global_argu.AP_Passwd)
	aps_5_1931 = Nokia_1931(global_argu.AP_host, global_argu.AP_User, global_argu.AP_Passwd)
	# Running 5G
	threads_5 = []
	t1_5 = threading.Thread(target=chariot_run_5.run_5g, args=(j,))
	threads_5.append(t1_5)
	if global_argu.AP_Type == 'CIG':
		t2_5 = threading.Thread(target=aps_5.state_5g, args=(j,))
	elif global_argu.AP_Type == 'NOKIA_1931':
		t2_5 = threading.Thread(target=aps_5_1931.state_5g, args=(j,))
	threads_5.append(t2_5)
	t3_5 = threading.Thread(target=chariot_run_5.get_data_5g, args=(j,))
	threads_5.append(t3_5)
	for t_5 in threads_5:
		t_5.start()
	t1_5.join()
	t2_5.join()
	t3_5.join()
	time.sleep(10)


def close_2g():
	if global_argu.AP_Type == 'CIG':
		tn = telnetlib.Telnet(global_argu.AP_host, port=23, timeout=10)
		tn.set_debuglevel(2)
		tn.read_until('Login as:'.encode('utf-8'))  # !str
		tn.write(global_argu.AP_User.encode('ascii')+b'\n')   # str
		tn.read_until('Password:'.encode('utf-8'))
		tn.write(global_argu.AP_Passwd.encode('ascii')+b'\n')
		tn.read_until('AP>'.encode('utf-8'))
		tn.write('enable \n'.encode('ascii'))
		tn.read_until('#AP>'.encode('utf-8'))
		tn.write("system/wifi \n".encode('ascii'))
		tn.read_until('#AP/system/wifi>'.encode('utf-8'))
		# 2.4G
		tn.write(("basic 0 0 %s 1 %s 0 \n" % (global_argu.AP_channel_2, global_argu.AP_bandwidth_2[0])).encode('ascii'))
		tn.read_until('#AP/system/wifi>'.encode('utf-8'))
		tn.write(("ssid 0 0 0 %s \n" % global_argu.AP_ssid_2).encode('ascii'))
		tn.read_until('#AP/system/wifi>'.encode('utf-8'))
		tn.write("sec 0 0 3 0 0 \n".encode('ascii'))
		time.sleep(1)
		tn.read_until('#AP/system/wifi>'.encode('utf-8'))
		tn.write('x \n'.encode('ascii'))
		tn.read_until('#AP/system>'.encode('utf-8'))
		tn.write('x \n'.encode('ascii'))
		tn.read_until('#AP>'.encode('utf-8'))
		tn.close()
		# Log to GUI
		LogMsg(log.logger.info, 'Close 2.4G Successfully!')
	elif global_argu.AP_Type == 'NOKIA_1931':
		tn = telnetlib.Telnet(global_argu.AP_host, port=23, timeout=10)
		tn.set_debuglevel(2)
		tn.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
		tn.write("ifconfig ath1 down".encode('ascii'))
		# tn.read_until('root@OpenWrt:/#'.encode('utf-8'))
		tn.write('exit \n'.encode('ascii'))
		tn.close()
	else:
		LogMsg(log.logger.info, 'Close_2g Failed')


def start_2g():
	if global_argu.AP_Type == 'CIG':
		tn = telnetlib.Telnet(global_argu.AP_host, port=23, timeout=10)
		tn.set_debuglevel(2)
		tn.read_until('Login as:'.encode('utf-8'))  # !str
		tn.write(global_argu.AP_User.encode('ascii')+b'\n')   # str
		tn.read_until('Password:'.encode('utf-8'))
		tn.write(global_argu.AP_Passwd.encode('ascii')+b'\n')
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
		tn.read_until('#AP/system/wifi>'.encode('utf-8'))
		tn.write('x \n'.encode('ascii'))
		tn.read_until('#AP/system>'.encode('utf-8'))
		tn.write('x \n'.encode('ascii'))
		tn.read_until('#AP>'.encode('utf-8'))
		tn.close()
		# Log to GUI
		LogMsg(log.logger.info, 'Start 2.4G Successfully!')
	elif global_argu.AP_Type == 'NOKIA_1931':
		tn = telnetlib.Telnet(global_argu.AP_host, port=23, timeout=10)
		tn.set_debuglevel(2)
		tn.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
		tn.write("ifconfig ath1 up".encode('ascii'))
		# tn.read_until('root@OpenWrt:/#'.encode('utf-8'))
		tn.write('exit \n'.encode('ascii'))
		tn.close()
	else:
		LogMsg(log.logger.info, 'Start_2g Failed')


def ping_test():
	# Create ping.txt
	file_data = os.path.isfile('D:\Python_project\Pro\TP_8\ping.txt')
	if file_data is True:
		pass
	else:
		os.chdir('D:\Python_project\Pro\TP_8')
		f = open('ping.txt', 'w')
		f.close()
	while True:
		result = os.popen('ping %s -n 2' % global_argu.Chariot_ip5)
		os.chdir('D:\Python_project\Pro\TP_8')
		f = open('ping.txt', 'w')
		f.writelines(result)
		f.close()
		fd = open('D:\Python_project\Pro\TP_8\ping.txt', 'r')
		ret = fd.read()
		result_1 =re.findall(r'来自\s+\d.+'or r'Reply from\s+\d.+', ret)[0][3:18].strip()
		LogMsg(log.logger.info, result_1)
		result_2 =re.findall(r'\d.+%'or r'Lost\s+\d.+', ret)[0][18:19].strip()
		LogMsg(log.logger.info, result_2)
		if result_1 == global_argu.Chariot_ip5 and result_2 == '0':
			LogMsg(log.logger.info, 'YES Ping PASS')
			break
		LogMsg(log.logger.info, 'NO Ping FAIL')
		fd.close()


def ping_test_2():
	# Create ping.txt
	file_data = os.path.isfile('D:\Python_project\Pro\TP_8\ping.txt')
	if file_data is True:
		pass
	else:
		os.chdir('D:\Python_project\Pro\TP_8')
		f = open('ping.txt', 'w')
		f.close()
	while True:
		result = os.popen('ping %s -n 2' % global_argu.Chariot_ip2)
		os.chdir('D:\Python_project\Pro\TP_8')
		f = open('ping.txt', 'w')
		f.writelines(result)
		f.close()
		fd = open('D:\Python_project\Pro\TP_8\ping.txt', 'r')
		ret = fd.read()
		result_1 =re.findall(r'来自\s+\d.+'or r'Reply from\s+\d.+', ret)[0][3:18].strip()
		LogMsg(log.logger.info, result_1)
		result_2 =re.findall(r'\d.+%'or r'Lost\s+\d.+', ret)[0][18:19].strip()
		LogMsg(log.logger.info, result_2)
		if result_1 == global_argu.Chariot_ip2 and result_2 == '0':
			LogMsg(log.logger.info, 'YES Ping PASS')
			break
		LogMsg(log.logger.info, 'NO Ping FAIL')
		fd.close()


def stop_distance_check():
	while True:
		time.sleep(10)
		conf = configparser.ConfigParser()
		conf.read('D:\Python_project\Pro\TP_8\config.ini')
		dis = conf.get('other_config', 'stop_distance_flag')
		if dis == '0':
			break
		else:
			LogMsg(log.logger.info, 'Click OK after this message!')


def kill_process():
	pythoncom.CoInitialize()
	WMI = win32com.client.GetObject('winmgmts:')
	processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="EXCEL.EXE"')
	if len(processCodeCov) > 0:
		LogMsg(log.logger.info, 'process excel.exe is exit!!!')
		os.system('TASKKILL /F /IM EXCEL.EXE')
	else:
		pass
	pythoncom.CoUninitialize()


def move_10():
	move_10d = os.path.exists('D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_10m')
	if move_10d is True:
		pass
	else:
		os.makedirs('D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_10m')
	srcd = 'D:\Python_project\Pro\TP_8\iperflog\MyResults'
	dscd = 'D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_10m'
	for i in os.listdir(srcd):
		if i.endswith('.txt') or i.endswith('.tst'):
			shutil.move(srcd+os.sep+i, dscd+os.sep)


def move_50():
	move_50d = os.path.exists('D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_50m')
	if move_50d is True:
		pass
	else:
		os.makedirs('D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_50m')
	srcd = 'D:\Python_project\Pro\TP_8\iperflog\MyResults'
	dscd = 'D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_50m'
	for i in os.listdir(srcd):
		if i.endswith('.txt') or i.endswith('.tst'):
			shutil.move(srcd+os.sep+i, dscd+os.sep)


def Run():
	#######################################
	#
	# init system
	#
	#######################################

	"""
	running software
	when we start chariot ,the degree is 0°
	"""
	"""
	config ap
	"""
	chick =global_argu.ap_configd
	if chick == '1':
		ap = Ap(global_argu.AP_host, global_argu.AP_User, global_argu.AP_Passwd)
		ap.config()
	else:
		LogMsg(log.logger.info, 'Cant Config AP by itself!')
	directory = os.path.exists('D:\Python_project\Pro\TP_8\iperflog')
	if directory is True:
		pass
	else:
		os.makedirs('D:\Python_project\Pro\TP_8\iperflog')
	# remove MyResult *.File and makedir
	myresult = os.path.exists('D:\Python_project\Pro\TP_8\iperflog\MyResults')
	if myresult is True:
		shutil.rmtree('D:\Python_project\Pro\TP_8\iperflog\MyResults', True)
		os.makedirs('D:\Python_project\Pro\TP_8\iperflog\MyResults')
	else:
		os.makedirs('D:\Python_project\Pro\TP_8\iperflog\MyResults')
	chick2 = global_argu.sys_start
	conf = configparser.ConfigParser()
	conf.read('D:\Python_project\Pro\TP_8\config.ini')
	if chick2 == '1':
		kill_process()
		result = report(global_argu.Report_distance, None, None, None, None, None, global_argu.Chariot_time, global_argu.dot11_2dg, global_argu.dot11_5dg)
		result.create_report(9)
		machine = Emachine()
		directory = os.path.exists('D:\iperf\iperf_result')
		if directory is True:
			pass
		else:
			os.makedirs('D:\iperf\iperf_result')
		src = 'D:\Python_project\Pro\TP_8\iperflog\TP_Tmp_Report.xlsx'
		dsc = 'D:\iperf\iperf_result\TP_Result_%s.xlsx' % time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
		# remove data.txt
		os.chdir('D:\Python_project\Pro\TP_8')
		file_data = os.path.isfile('D:\Python_project\Pro\TP_8\data.txt')
		if file_data is True:
			os.remove('D:\Python_project\Pro\TP_8\data.txt')
		else:
			pass
		if len(global_argu.Report_band) == 1:
			if global_argu.Report_band[0] == global_argu.dot11_2dg:
				if len(global_argu.Report_distance) == 1:
					if global_argu.degree == '8':
						for i in range(8):
							run_2(i)
						LogMsg(log.logger.info, '2.4G is Tested Over!')
					elif global_argu.degree == '4':
						for i in range(4):
							run_2(i)
						LogMsg(log.logger.info, '2.4G is Tested Over!')
					else:
						LogMsg(log.logger.error, 'NO Degree!')
					copyfile(src, dsc)
					shutil.move('D:\Python_project\Pro\TP_8\iperflog\MyResults', 'D:\iperf\iperf_result\Log_%s'% time.strftime("%Y-%m-%d_%H%M%S",time.localtime()))
					conf.set('other_config', 'Game_Over', '1')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
				elif len(global_argu.Report_distance) == 2:
					if global_argu.degree == '8':
						conf.set('other_config', 'dis_flag', '1')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						for i in range(8):
							run_2(i)
						LogMsg(log.logger.info, '2.4G is over! if you have other Distance,please move to the distance!!!')
						machine.degree_resoval()
						time.sleep(5)
						move_10()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						time.sleep(1)
						stop_distance_check()
						conf.set('other_config', 'dis_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						for i in range(8):
							run_2(i)
						time.sleep(1)
						move_50()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '0')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						LogMsg(log.logger.info, '2.4G is Tested Over!')
					elif global_argu.degree == '4':
						conf.set('other_config', 'dis_flag', '1')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						for i in range(4):
							run_2(i)
						LogMsg(log.logger.info, '2.4G is over! if you have other Distance,please move to the distance!!!')
						machine.degree_resoval()
						time.sleep(5)
						move_10()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						time.sleep(1)
						stop_distance_check()
						conf.set('other_config', 'dis_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						for i in range(4):
							run_2(i)
						time.sleep(1)
						move_50()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '0')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						LogMsg(log.logger.info, '2.4G is Tested Over')
					else:
						LogMsg(log.logger.error, 'NO Degree')
					copyfile(src, dsc)
					shutil.move('D:\Python_project\Pro\TP_8\iperflog\MyResults', 'D:\iperf\iperf_result\Log_%s'% time.strftime("%Y-%m-%d_%H%M%S",time.localtime()))
					conf.set('other_config', 'Game_Over', '1')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
				else:
					LogMsg(log.logger.error, '2.4G: NO Distance!')

			elif global_argu.Report_band[0] == global_argu.dot11_5dg:
				if len(global_argu.Report_distance) == 1:
					if global_argu.degree == '8':
						for i in range(8):
							run_5(i)
						LogMsg(log.logger.info, '5G is Tested Over')
					elif global_argu.degree == '4':
						for i in range(4):
							run_5(i)
						LogMsg(log.logger.info, '5G is Tested Over')
					else:
						LogMsg(log.logger.error, 'NO Degree')
					copyfile(src, dsc)
					shutil.move('D:\Python_project\Pro\TP_8\iperflog\MyResults', 'D:\iperf\iperf_result\Log_%s'% time.strftime("%Y-%m-%d_%H%M%S",time.localtime()))
					conf.set('other_config', 'Game_Over', '1')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
				elif len(global_argu.Report_distance) == 2:
					conf.set('other_config', 'dis_flag', '1')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					if global_argu.degree == '8':
						for i in range(8):
							run_5(i)
						LogMsg(log.logger.info, '5G is over，if you have other Distance,please move to the distance!!!')
						machine.degree_resoval()
						time.sleep(5)
						move_10()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						time.sleep(1)
						stop_distance_check()
						conf.set('other_config', 'dis_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						for i in range(8):
							run_5(i)
						time.sleep(1)
						move_50()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '0')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						LogMsg(log.logger.info, '5G is Tested Over')
					elif global_argu.degree == '4':
						conf.set('other_config', 'dis_flag', '1')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						for i in range(4):
							run_5(i)
						LogMsg(log.logger.info, '5G is over，if you have other Distance,please move to the distance!!!')
						machine.degree_resoval()
						time.sleep(5)
						move_10()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						time.sleep(1)
						stop_distance_check()
						conf.set('other_config', 'dis_flag', '2')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						for i in range(4):
							run_5(i)
						time.sleep(1)
						move_50()
						time.sleep(1)
						conf.set('other_config', 'stop_distance_flag', '0')
						conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
						LogMsg(log.logger.info,	'5G is Tested Over')
					else:
						LogMsg(log.logger.error, 'NO Degree')
					copyfile(src, dsc)
					shutil.move('D:\Python_project\Pro\TP_8\iperflog\MyResults', 'D:\iperf\iperf_result\Log_%s'% time.strftime("%Y-%m-%d_%H%M%S",time.localtime()))
					conf.set('other_config', 'Game_Over', '1')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
				else:
					LogMsg(log.logger.error, '5G: NO Distance!')
			else:
				LogMsg(log.logger.error, 'NO BAND')

		elif len(global_argu.Report_band) == 2:
			if len(global_argu.Report_distance) == 1:
				if global_argu.degree == '8':
					for i in range(8):
						LogMsg(log.logger.info, 'Now we start running 2.4G! Time: %s' % i)
						run_2(i)
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
					# close 2.4G and if pc can ping sta start!!!
					close_2g()
					time.sleep(30)
					ping_test()
					for i in range(8):
						LogMsg(log.logger.info, 'Now we start running 5G! Time: %s' % i)
						run_5(i)
					time.sleep(5)
					start_2g()
					LogMsg(log.logger.info, '2.4G&5G is Tested Over')
				elif global_argu.degree == '4':
					for i in range(4):
						LogMsg(log.logger.info, 'Now we start running 2.4G! Time: %s' % i)
						run_2(i)
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
					close_2g()
					time.sleep(30)
					ping_test()
					for i in range(4):
						LogMsg(log.logger.info, 'Now we start running 5G! Time: %s' % i)
						run_5(i)
					time.sleep(5)
					start_2g()
					LogMsg(log.logger.info, '2.4G&5G is Tested Over')
				else:
					LogMsg(log.logger.error, 'NO Degree!')
			elif len(global_argu.Report_distance) == 2:
				if global_argu.degree == '8':
					conf.set('other_config', 'dis_flag', '1')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					for i in range(8):
						LogMsg(log.logger.info, 'Now we start running 2.4G! Time: %s' % i)
						run_2(i)
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
					# close 2.4G and if pc can ping sta start!!!
					close_2g()
					time.sleep(30)
					ping_test()
					for i in range(8):
						LogMsg(log.logger.info, 'Now we start running 5G! Time: %s' % i)
						run_5(i)
					time.sleep(5)
					start_2g()
					LogMsg(log.logger.info, 'MOVE To Other Distance!')
					time.sleep(30)
					machine.degree_resoval()
					time.sleep(5)
					move_10()
					time.sleep(1)
					conf.set('other_config', 'stop_distance_flag', '2')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					time.sleep(1)
					stop_distance_check()
					ping_test_2()
					conf.set('other_config', 'dis_flag', '2')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					for i in range(8):
						LogMsg(log.logger.info, 'Now we start running 2.4G! Time: %s' % i)
						run_2(i)
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
					# close 2.4G and if pc can ping sta start!!!
					close_2g()
					time.sleep(30)
					ping_test()
					for i in range(8):
						LogMsg(log.logger.info, 'Now we start running 5G! Time: %s' % i)
						run_5(i)
					time.sleep(2)
					move_50()
					time.sleep(1)
					start_2g()
					conf.set('other_config', 'stop_distance_flag', '0')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					LogMsg(log.logger.info, '2.4G&5G is Tested Over')

				elif global_argu.degree == '4':
					conf.set('other_config', 'dis_flag', '1')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					for i in range(4):
						LogMsg(log.logger.info, 'Now we start running 2.4G! Time: %s' % i)
						run_2(i)
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
					close_2g()
					time.sleep(30)
					ping_test()
					for i in range(4):
						LogMsg(log.logger.info, 'Now we start running 5G! Time: %s' % i)
						run_5(i)
					time.sleep(5)
					start_2g()
					LogMsg(log.logger.info, 'MOVE To Other Distance!')
					time.sleep(30)
					machine.degree_resoval()
					time.sleep(5)
					move_10()
					time.sleep(1)
					conf.set('other_config', 'stop_distance_flag', '2')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					time.sleep(1)
					stop_distance_check()
					ping_test_2()
					conf.set('other_config', 'dis_flag', '2')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					for i in range(4):
						LogMsg(log.logger.info, 'Now we start running 2.4G! Time: %s' % i)
						run_2(i)
					time.sleep(1)
					machine.degree_resoval()
					time.sleep(10)
					# close 2.4G and if pc can ping sta start!!!
					close_2g()
					time.sleep(30)
					ping_test()
					for i in range(4):
						LogMsg(log.logger.info, 'Now we start running 5G! Time: %s' % i)
						run_5(i)
					time.sleep(2)
					move_50()
					time.sleep(1)
					start_2g()
					conf.set('other_config', 'stop_distance_flag', '0')
					conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
					LogMsg(log.logger.info, '2.4G&5G is Tested Over')
				else:
					LogMsg(log.logger.error, 'NO Degree')
			else:
				LogMsg(log.logger.error, 'NO Distance!')
			copyfile(src, dsc)
			shutil.move('D:\Python_project\Pro\TP_8\iperflog\MyResults', 'D:\iperf\iperf_result\Log_%s'% time.strftime("%Y-%m-%d_%H%M%S",time.localtime()))
			conf.set('other_config', 'Game_Over', '1')
			conf.write(open('D:\Python_project\Pro\TP_8\config.ini', 'w'))
			time.sleep(1)
			machine.degree_resoval()
			time.sleep(10)
		else:
			LogMsg(log.logger.error, 'No band or band is out of range!')
		kill_process()

	else:
		LogMsg(log.logger.error, 'System Can''t Start!')


if __name__ == '__main__':
	Run()
