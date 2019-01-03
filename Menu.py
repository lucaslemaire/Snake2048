#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Game2048 import *
from GameSnake import *
from Tutorial import *

#Classe du menu principal de l'application.
class Menu(QWidget):
	#Initialisation du widget
	def __init__(self):
		QWidget.__init__(self)
		self.initUI()

	#Initialisation du widget
	def initUI(self):
		self.setWindowTitle("2048 Menu Principal")
		self.setFixedSize(320,400)
		self.label = QLabel(self)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setGeometry(10,10,230,100)
		font = QFont("Arial",60,QFont.Bold)
		self.label.setFont(font)
		self.label.setText("<font color=\"#8226b6\">2</font><font color=\"#0f0f43\">0</font><font color=\"#8226b6\">4</font><font color=\"#0f0f43\">8</font>")
		self.label.move(((self.width()//2)-self.label.width()//2),40)

		self.label1 = QLabel(self)
		self.label1.setAlignment(Qt.AlignCenter)
		self.label1.setGeometry(10,10,230,120)
		font = QFont("Arial",14,QFont.Bold)
		self.label1.setFont(font)
		self.label1.setText("Swipe to move\n and join the matching \ncards.\n\nGet 2048 to Win ! ")
		self.label1.move(((self.width()//2)-self.label1.width()//2),150)
		self.label1.hide()


		self.playButton=QPushButton("Classic mode",self)
		self.playButton.resize(160,35)
		self.playButton.move(((self.width()//2)-self.playButton.width()//2),165)
		self.playButton.setStyleSheet('QPushButton {font-size:14px;background-color: #8226b6; border-style : outset;font-weight:bold;}')

		self.helpButton=QPushButton("?",self)
		self.helpButton.resize(35,35)
		self.helpButton.move((self.width()//2)+ 90,165)
		self.helpButton.setStyleSheet('QPushButton {font-size:16px;background-color: #AD33F2; border-style : outset;font-weight:bold;}')
		self.helpButton.clicked.connect(self.tutorialSection)

		self.helpButton2=QPushButton("?",self)
		self.helpButton2.resize(35,35)
		self.helpButton2.move((self.width()//2)+90,205)
		self.helpButton2.setStyleSheet('QPushButton {font-size:16px;background-color: #1A1A75; border-style : outset;font-weight:bold;}')
		self.helpButton2.clicked.connect(self.tutorialSection2)

		self.playButton2 = QPushButton("Snake mode",self)
		self.playButton2.resize(160,35)
		self.playButton2.move(((self.width()//2)-self.playButton2.width()//2),205)
		self.playButton2.setStyleSheet('QPushButton {font-size:14px;background-color: #0f0f43; border-style : outset;font-weight:bold;}')

		self.leaveButton=QPushButton("Exit",self)
		self.leaveButton.resize(160,35)
		self.leaveButton.move(((self.width()//2)-self.leaveButton.width()//2),275)
		self.leaveButton.setStyleSheet('QPushButton {font-size:14px;background-color: #ff005c; border-style : outset;font-weight:bold;}')

		self.playButton.clicked.connect(self.game2048)
		self.playButton2.clicked.connect(self.gameSnake)
		self.leaveButton.clicked.connect(self.quit)

		self.show()

	#Procédure permettant d'ouvrir la section tutoriel du 2048.
	def tutorialSection(self):
		self.tuto = Tutorial(1)
		self.hide()
		self.tuto.show()

	#Procédure permettant d'ouvrir la section tutoriel du Snake Mode.
	def tutorialSection2(self):
		self.tuto = Tutorial(2)
		self.hide()
		self.tuto.show()

	#Procédure permettant d'ouvrir le jeu 2048.
	def game2048(self) :
		self.jeu1 = Game2048(None,340,4)
		self.hide()
		self.jeu1.show()

	#Procédure permettant d'ouvrir le jeu Snake 2048.
	def gameSnake(self):
		self.jeu2 = Snake()
		self.hide()
		self.jeu2.show()

	#Procédure permettant de centrer la fenêtre.
	def setCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	#Procédure permettant de quitter l'application.
	def quit(self):
		dialog = QMessageBox(self)
		dialog.setWindowTitle("Exit")
		dialog.setText("Do you really want to leave us ?")
		dialog.setStyleSheet('QMessageBox {font-size:13px;}')
		dialog.setIcon(QMessageBox.Question)
		dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		dialog.setDefaultButton(QMessageBox.Ok)
		if dialog.exec_() == QMessageBox.Ok:
			QCoreApplication.instance().quit()
