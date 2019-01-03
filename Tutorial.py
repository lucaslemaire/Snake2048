#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Menu as Menu

#Classe de la fonction "How to play?" du menu principal.
class Tutorial(QWidget):
	#Initialisation du QWidget
	def __init__(self,arg):
		QWidget.__init__(self)
		self.label = QLabel(self)
		self.initUI(arg)

	#Paramétrage de la fenêtre du QWidget et définition des éléments du QWidget
	def initUI(self,arg):
		self.setFixedSize(320,400)

		self.menu = QPushButton("Return",self)
		self.menu.resize(160,35)
		self.menu.setStyleSheet('QPushButton {font-size:14px;background-color: #ff005c; border-style : outset;font-weight:bold;}')
		self.menu.move(((self.width()//2)-self.menu.width()//2),330)

		self.label = QLabel(self)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setGeometry(10,10,230,100)
		font = QFont("Arial",23,QFont.Bold)
		self.label.setFont(font)
		self.label.move(((self.width()//2)-self.label.width()//2),0)

		self.label1 = QLabel(self)
		self.label1.setAlignment(Qt.AlignCenter)
		self.label1.setGeometry(10,10,230,120)
		font = QFont("Arial",13,QFont.Bold)
		self.label1.setFont(font)
		self.label1.move(110,75)

		self.pixmapK = QPixmap('img/keyboard.png')
		self.pixmapE = QPixmap('img/escape.png')
		self.pixmapW = QPixmap('img/warn.png')

		self.keyboard = QLabel(self)
		self.keyboard.setPixmap(self.pixmapK.scaled(146,99))
		self.keyboard.move(5,85)

		self.escape = QLabel(self)

		if arg == 1 :
			self.setWindowTitle("Tutoriel Original Mode")
			self.classicMode()
		elif arg == 2 :
			self.setWindowTitle("Tutoriel Snake Mode")
			self.snakeMode()

	#Fonction qui affiche les règles du Classic Mode
	def classicMode(self):
		#Push bouton pour retourner au menu.
		self.menu.clicked.connect(self.backToMenu)
		self.menu.show()

		#Attribution d'une image au label keyboard
		self.keyboard.show()

		#Attribution d'une image au label escape
		self.escape.setPixmap(self.pixmapE.scaled(55,55))
		self.escape.move(51,225)
		self.escape.show()

		#Positionnage du label "Classic Mode" et paramétrage
		self.label.setText("Classic Mode")
		self.label.setStyleSheet('color : #8226b6')
		self.label.show()

		#Positionnage et paramétrage du label d'instructions de jeu.
		self.label1.setText("Use arrow keys\nMerge the boxes\nReach 2048 to win !")
		self.label1.setStyleSheet('color : #8226b6')
		self.label1.show()

		#Positionnage et paramétrage du label d'instructions de jeu?
		self.label2 = QLabel(self)
		font = QFont("Arial",13,QFont.Bold)
		self.label2.setFont(font)
		self.label2.setAlignment(Qt.AlignCenter)
		self.label2.setGeometry(10,10,230,120)
		self.label2.setText("Press ESC to\nreturn to the\nmain menu")
		self.label2.setStyleSheet('color : #8226b6')
		self.label2.move(110,192)
		self.label2.show()

	#Fonction qui affiche les règles du Snake Mode.
	def snakeMode(self):
		self.menu.clicked.connect(self.backToMenu)
		self.menu.show()

		self.keyboard.show()

		self.escape.setPixmap(self.pixmapW.scaled(55,53))
		self.escape.move(20,225)
		self.escape.show()

		self.label.setText("Snake Mode")
		self.label.setStyleSheet('color : #0f0f43')
		self.label.show()

		self.label1.setText("Use arrow keys to\ncontrol the snake.")
		self.label1.setStyleSheet('color : #0f0f43')
		self.label1.show()

		self.label3 = QLabel(self)
		font = QFont('Arial',13,QFont.Bold)
		self.label3.setFont(font)
		self.label3.setText("You lose if :\n\n - You touch yourself.\n - You hit sides of window.\n - One of your tiles column\n   is full.")
		self.label3.setStyleSheet('color : #0f0f43')
		self.label3.move(87,200)

		#self.switch.setText("<")
		#self.switch.clicked.connect(self.switchClassic)
		#self.switch.move(33,330)

	#Fonction permettant de retourner au menu principal du jeu.
	def backToMenu(self):
		self.back = Menu.Menu()
		self.hide()
		self.back.show()
