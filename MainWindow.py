#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Menu as Menu

class Application(QApplication):
	def __init__(self, argv):
		super().__init__(argv)
		self.initUI()

	def initUI(self):
		self.setStyle(QStyleFactory.create('fusion'))
		p = self.palette()
		p.setColor(QPalette.Window, QColor(0xbbada0))
		p.setColor(QPalette.Button, QColor(53,53,53))
		p.setColor(QPalette.Highlight, QColor(142,45,197))
		p.setColor(QPalette.ButtonText, QColor(255,255,255))
		p.setColor(QPalette.WindowText, QColor(255,255,255))
		self.setPalette(p)

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(10, 10, 340, 400)
		self.setFixedSize(320,400)
		self.setCenter()
		self.setWindowTitle('  2048')
		self.setWindowIcon(QIcon('logo_2048.png'))
		self.menu = Menu.Menu()
		self.menu.show()

	def setCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())



app = Application(sys.argv)
win = Window()
app.exec_()
