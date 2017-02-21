# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import telnetlib
import re
from log_c import *


class WF_1931(object):
	"""
	AP in STA modle  4*4 ,Read RSSI from AP
	"""
	def __init__(self, host):
		self.host = host

	def wf1931_rssi_2g(self):
		try:
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
			t.write('iwconfig ath1 \n'.encode('ascii'))  # str
			ret = t.read_until('root@OpenWrt:/#'.encode('utf-8'))
			print(ret)
			# re
			Rssi = re.findall(r'-\d+'.encode('utf-8'), ret)[0].decode('utf-8')
			print(Rssi)
			#close
			t.write('exit \n'.encode('ascii'))
			t.close()
			return Rssi
		except Exception as e:
			LogMsg(log.logger.error, 'state_2g: Telnet ERROR!')

	def wf1931_rssi_5g(self):
		try:
			t = telnetlib.Telnet(host=self.host, port=23, timeout=10)
			t.set_debuglevel(2)
			t.read_until('root@OpenWrt:/#'.encode('utf-8'))  # !str
			t.write('iwconfig ath0 \n'.encode('ascii'))  # str
			ret = t.read_until('root@OpenWrt:/#'.encode('utf-8'))
			print(ret)
			# re
			Rssi = re.findall(r'-\d+'.encode('utf-8'), ret)[0].decode('utf-8')
			print(Rssi)
			# close
			t.write('exit \n'.encode('ascii'))
			t.close()
			return Rssi
		except Exception as e:
			LogMsg(log.logger.error, 'state_2g: Telnet ERROR!')

if __name__ == '__main__':
	hostd = '192.168.1.2'
	p = WF_1931(hostd)
	p.wf1931_rssi_2g()


