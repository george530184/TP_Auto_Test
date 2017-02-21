# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import os
import shutil


def test():
	os.chdir('D:\Python_project\Pro\TP_8\iperflog\MyResults')
	#os.makedirs('D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_10m')
	a = 'D:\Python_project\Pro\TP_8\iperflog\MyResults'
	b = 'D:\Python_project\Pro\TP_8\iperflog\MyResults\\test_10m'
	for i in os.listdir(a):
		if i.endswith('.txt') or i.endswith('.tst'):
			shutil.move(a+os.sep+i, b+os.sep)
if __name__ == '__main__':
	test()