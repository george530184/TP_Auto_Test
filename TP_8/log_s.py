# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import logging
import logging.handlers
import logging.config
import time
import os
import re
import difflib
from shutil import copyfile

LOG_FILE = 'D:\Python_project\Pro\TP_8\log\Running.txt'
FILE_SIZE = 10*1024*1024
PATH_DIR = 'D:\Python_project\Pro\TP_8'


class Log(object):
	def __init__(self):
		self.logger = logging.getLogger('TP_8')
		self.logger.setLevel(logging.INFO)
		# basicConfig to cli
		logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
		# formatter to .log
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
		handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=FILE_SIZE, backupCount=3)
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
		handler.close()

	def set_log_level(self, level):
		if level == "NOTSET":
			self.logger.setLevel(logging.NOTSET)
		if level == "DEBUG":
			self.logger.setLevel(logging.DEBUG)
		elif level == "INFO":
			self.logger.setLevel(logging.INFO)
		elif level == "WARNING":
			self.logger.setLevel(logging.WARNING)
		elif level == "ERROR":
			self.logger.setLevel(logging.ERROR)
		elif level == "CRITICAL":
			self.logger.setLevel(logging.CRITICAL)
		else:
			print("[LOG]Unknown log level")
log = Log()


def LogMsg(loglevel, msg):
	loglevel(msg)


class FileEventHandler(object):
	'''
	monitor Running.txt and notify thread logging to GUI
	'''
	def __init__(self):
		pass

	def on_modified(self, event):
		dir_log = os.path.isdir('D:\Python_project\Pro\TP_8\log')
		if dir_log is True:
			pass
		else:
			os.makedirs(r'D:\Python_project\Pro\TP_8\log')
		dir_tmp = os.path.isdir('D:\Python_project\Pro\TP_8\log\\tmp')
		if dir_tmp is True:
			pass
		else:
			os.makedirs(r'D:\Python_project\Pro\TP_8\log\\tmp')
		src = 'D:\Python_project\Pro\TP_8\log\Running.txt'
		dsc = 'D:\Python_project\Pro\TP_8\log\\tmp\Running.txt'
		copyfile(src, dsc)
		os.chdir('D:\Python_project\Pro\TP_8\log\\tmp')
		size_x = os.path.getsize('RunX.txt')
		size = os.path.getsize('Running.txt')
		if size == size_x:
			os.remove('D:\Python_project\Pro\TP_8\log\\tmp\Running.txt')
		elif size > size_x:
			os.chdir('D:\Python_project\Pro\TP_8\log\\tmp')
			Runx = open('RunX.txt', 'U').readlines()
			Running = open('Running.txt', 'U').readlines()
			diff = difflib.ndiff(Runx, Running)
			diff_com = ''.join(diff)
			result_d = re.findall(r'\+\s\d.+', diff_com)
			for i in range(len(result_d)):
				result_diff = result_d[i]
				event.append(result_diff)
			os.remove('D:\Python_project\Pro\TP_8\log\\tmp\RunX.txt')
			os.rename('D:\Python_project\Pro\TP_8\log\\tmp\Running.txt',
					'D:\Python_project\Pro\TP_8\log\\tmp\RunX.txt')
		else:
			LogMsg(log.logger.error, 'ERROR,size < size_x!')