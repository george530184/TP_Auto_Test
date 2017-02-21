# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import os
import win32com.client
import pythoncom
import time
from log_c import *


def iperfs():
	directory = os.path.exists('D:\Python_project\Pro\TP_8\iperf3_64')
	if directory is True:
		os.chdir('D:\Python_project\Pro\TP_8\iperf3_64')
		file = os.path.isfile('D:\Python_project\Pro\TP_8\iperf3_64\iperf3.exe')
		if file is True:
			LogMsg(log.logger.info, 'Start Iperf Server!')
			os.system('iperf3.exe -s')
			pythoncom.CoInitialize()
			WMI = win32com.client.GetObject('winmgmts:')
			processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="iperf3.exe"')
			if len(processCodeCov) > 0:
				LogMsg(log.logger.info, 'Iperf Start OK!')
			else:
				time.sleep(15)
				if len(processCodeCov) > 0:
					pass
				else:
					os.system('iperf3.exe -s')
			pythoncom.CoUninitialize()
		else:
			LogMsg(log.logger.error, 'No Iperf File!')
	else:
		LogMsg(log.logger.error, 'No Iperf Directory!')


if __name__ == '__main__':
	iperfs()