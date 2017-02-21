# -*- coding: utf-8 -*-
__author__ = 'Jerry'
import socket
import sys
from Sta_RSSI import *
from other_rssi import *
import time
from log_c import *
import globle_argu_c


# Symbolic name meaning all available interfaces
HOST = ''
PORT = 5252
BUF_SIZE = 1024
#host = globle_argu_c.STA_IP
host = '192.168.1.2'


def sockets():
	LogMsg(log.logger.info, 'Start Socket Server!')
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error:
		LogMsg(log.logger.error, 'Create Socket Error!')
		sys.exit()
	try:
		s.bind((HOST, PORT))
	except socket.error:
		LogMsg(log.logger.error, 'Bind Socket ERROR!')
		sys.exit()
	s.listen(2)
	LogMsg(log.logger.info, 'Socket Server Running OK!')
	while 1:
		conn, addr = s.accept()
		print('connected by', addr)
		conn.settimeout(5)
		data = conn.recv(BUF_SIZE).decode()
		print(data)  # key
		if data == '2':
			rssi_1931 = WF_1931(host)
			Sta_Rssi = rssi_1931.wf1931_rssi_2g().encode(encoding='utf-8')
		elif data == '5':
			rssi_1931 = WF_1931(host)
			Sta_Rssi = rssi_1931.wf1931_rssi_5g().encode(encoding='utf-8')
		else:
			rssi = get_BSSI()
			RSSI = rssi.get(data)   # value
			Sta_Rssi = RSSI.encode(encoding='utf-8')
		print(Sta_Rssi)
		# print("s is {0}".format(s))
		LogMsg(log.logger.info, Sta_Rssi)
		conn.sendall(Sta_Rssi)
		time.sleep(1)
	s.close()


if __name__ == '__main__':
	sockets()
