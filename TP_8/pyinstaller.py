# -*- coding: utf-8 -*-
__author__ = 'Jerry'

import os

if __name__ == '__main__':
	from PyInstaller.__main__ import run

	opts = ['gui.py', '-F', '-n serverd']
	run(opts)