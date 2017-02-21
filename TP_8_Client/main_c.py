# -*- coding: utf-8 -*-
__author__ = 'Jerry'
from socket_s import *
import time
import threading
import win32com.client
import re
from log_c import *
import pythoncom


def thread_run():
	threads = []
	t2 = threading.Thread(target=sockets, args=())
	threads.append(t2)
	for t in threads:
		t.start()
	t2.join()


def run():
	#######################################
	#
	# init system
	#
	#######################################
	'''
	# Check listening port kill 5252
	r = os.popen('netstat -aon|findstr "5252"')
	ret = r.read()
	if ret.strip() == '':
		pass
	else:
		process = re.findall(r'\d+.', ret)[-1]
		pythoncom.CoInitialize()
		WMI = win32com.client.GetObject('winmgmts:')
		processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="python.exe"')
		if len(processCodeCov) > 0:
			LogMsg(log.logger.info, 'Process is exit!')
			LogMsg(log.logger.error, 'You Can Use It Now!!!')
			# os.system('TASKKILL /F /PID {0}'.format(process))
		pythoncom.CoUninitialize()
	'''
	# init /log/tmp logfile
	file_data = os.path.isfile('D:\Python_project\Pro\TP_8_Client\log\Running.txt')
	if file_data is True:
		os.remove('D:\Python_project\Pro\TP_8_Client\log\Running.txt')
	else:
		pass
	os.chdir('D:\Python_project\Pro\TP_8_Client\log\\tmp')
	file_data = os.path.isfile('D:\Python_project\Pro\TP_8_Client\log\\tmp\RunX.txt')
	if file_data is True:
		os.remove('RunX.txt')
		f = open('RunX.txt', 'w')
		f.close()
	else:
		f = open('RunX.txt', 'w')
		f.close()
	file_data2 = os.path.isfile('D:\Python_project\Pro\TP_8_Client\log\\tmp\Running.txt')
	if file_data2 is True:
		os.remove('D:\Python_project\Pro\TP_8_Client\log\\tmp\Running.txt')
	else:
		pass
	# run system
	#thread_run()
	sockets()
if __name__ == '__main__':
	run()
