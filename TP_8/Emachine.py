# -*- coding: utf-8 -*-
__author__ = 'Jerry'

"""
Control E-machine 8 angles
"""

import os
import win32gui, win32con, win32api
import win32com.client
import time
import pythoncom
from ctypes import *
from log_s import *


class Emachine(object):

	def __init__(self):
		pass

	def degree_45(self, p):
		pythoncom.CoInitialize()
		WMI = win32com.client.GetObject('winmgmts:')
		processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="MotorControl.exe"')
		if len(processCodeCov) > 0:
			LogMsg(log.logger.info, 'process is exit!!!')
			os.system('TASKKILL /F /IM MotorControl.exe')
		else:
			try:
				os.chdir('D:\Python_project\Pro\TP_8\Emachine')
				os.system('start MotorControl.exe')
			except Exception as e:
				LogMsg(log.logger.error, 'degree_45:Can’t Open MotorControl!')
				pythoncom.CoInitialize()
				WMI = win32com.client.GetObject('winmgmts:')
				processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="EXCEL.EXE"')
				if len(processCodeCov) > 0:
					LogMsg(log.logger.info, 'process excel is exit!!!')
					os.system('TASKKILL /F /IM EXCEL.EXE')
				else:
					pass
				pythoncom.CoUninitialize()
		pythoncom.CoUninitialize()

		# Move window
		time.sleep(0.5)
		hWnd = win32gui.FindWindow(None, 'ER-A Cradle Head Controller')
		win32gui.MoveWindow(hWnd, 0, 0, 400, 500, True)  # new window(w:400 h:500)
		# start
		windll.user32.SetCursorPos(335, 125)    # mouse move to
		time.sleep(0.5)
		# mouse
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		time.sleep(0.5)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(0.5)
		windll.user32.SetCursorPos(160, 65)
		time.sleep(0.5)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(0.5)
		# keybd
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(100, 0, 0, 0)
		win32api.keybd_event(101, 0, 0, 0)
		win32api.keybd_event(101, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(100, 0, win32con.KEYEVENTF_KEYUP, 0)
		time.sleep(0.5)
		windll.user32.SetCursorPos(140, 180)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		windll.user32.SetCursorPos(80, 175)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(12)
		os.system('TASKKILL /F /IM MotorControl.exe')

	def degree_90(self, p):
		pythoncom.CoInitialize()
		WMI = win32com.client.GetObject('winmgmts:')
		processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="MotorControl.exe"')
		if len(processCodeCov) > 0:
			LogMsg(log.logger.info, 'process is exit!!!')
			os.system('TASKKILL /F /IM MotorControl.exe')
		else:
			try:
				os.chdir('D:\Python_project\Pro\TP_8\Emachine')
				os.system('start MotorControl.exe')
			except Exception as e:
				LogMsg(log.logger.error, 'degree_90:Can’t Open MotorControl!')
				pythoncom.CoInitialize()
				WMI = win32com.client.GetObject('winmgmts:')
				processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="EXCEL.EXE"')
				if len(processCodeCov) > 0:
					LogMsg(log.logger.info, 'process excel is exit!!!')
					os.system('TASKKILL /F /IM EXCEL.EXE')
				else:
					pass
				pythoncom.CoUninitialize()
		pythoncom.CoUninitialize()

		# Move window
		time.sleep(0.5)
		hWnd = win32gui.FindWindow(None, 'ER-A Cradle Head Controller')
		win32gui.MoveWindow(hWnd, 0, 0, 400, 500, True)  # new window(w:400 h:500)
		# start
		windll.user32.SetCursorPos(335, 125)    # mouse move to
		time.sleep(0.5)
		# mouse
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		time.sleep(0.5)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(0.5)
		windll.user32.SetCursorPos(160, 65)
		time.sleep(0.5)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(0.5)
		# keybd
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(105, 0, 0, 0)
		win32api.keybd_event(96, 0, 0, 0)
		win32api.keybd_event(96, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(105, 0, win32con.KEYEVENTF_KEYUP, 0)
		time.sleep(0.5)
		windll.user32.SetCursorPos(140, 180)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		windll.user32.SetCursorPos(80, 175)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(12)
		os.system('TASKKILL /F /IM MotorControl.exe')

	def degree_resoval(self):
		pythoncom.CoInitialize()
		WMI = win32com.client.GetObject('winmgmts:')
		processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="MotorControl.exe"')
		if len(processCodeCov) > 0:
			LogMsg(log.logger.info, 'process is exit!!!')
			os.system('TASKKILL /F /IM MotorControl.exe')
		else:
			try:
				os.chdir('D:\Python_project\Pro\TP_8\Emachine')
				os.system('start MotorControl.exe')
			except Exception as e:
				LogMsg(log.logger.error, 'degree_resoval:Can’t Open MotorControl!')
				pythoncom.CoInitialize()
				WMI = win32com.client.GetObject('winmgmts:')
				processCodeCov =WMI.ExecQuery('select * from Win32_Process where name ="EXCEL.EXE"')
				if len(processCodeCov) > 0:
					LogMsg(log.logger.info, 'process excel is exit!!!')
					os.system('TASKKILL /F /IM EXCEL.EXE')
				else:
					pass
				pythoncom.CoUninitialize()
		pythoncom.CoUninitialize()
		# Move window
		time.sleep(0.5)
		hWnd = win32gui.FindWindow(None, 'ER-A Cradle Head Controller')
		win32gui.MoveWindow(hWnd, 0, 0, 400, 500, True)  # new window(w:400 h:500)
		# start
		windll.user32.SetCursorPos(335, 125)    # mouse move to
		time.sleep(0.5)
		# mouse
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		time.sleep(0.5)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(0.5)
		windll.user32.SetCursorPos(160, 65)
		time.sleep(0.5)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(0.5)
		#keybd
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, 0, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(97, 0, 0, 0)
		win32api.keybd_event(104, 0, 0, 0)
		win32api.keybd_event(96, 0, 0, 0)
		win32api.keybd_event(96, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(104, 0, win32con.KEYEVENTF_KEYUP, 0)
		win32api.keybd_event(97, 0, win32con.KEYEVENTF_KEYUP, 0)
		time.sleep(0.5)
		windll.user32.SetCursorPos(32, 122)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(0.5)
		windll.user32.SetCursorPos(320, 402)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(6)
		windll.user32.SetCursorPos(140, 180)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		windll.user32.SetCursorPos(80, 175)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(15)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		time.sleep(15)
		os.system('TASKKILL /F /IM MotorControl.exe')

if __name__ == '__main__':
	run = Emachine()
	p = '1'
	#run.degree_45(p)
	#run.degree_90()
	run.degree_resoval()