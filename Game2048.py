#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import Menu as Menu

#Classe qui représente une tuile du jeu.
class Tile:
	def __init__(self,value):
		self.value=value

#Classe du Original Mode
class Game2048(QWidget):
	#Initialisation des paramètres du widget et du jeu.
	def __init__(self,parent,width=340,gridSize=4):
		#Lecture du high-score
		scoreFile = open("score.txt", "r")
		score = int(scoreFile.read())
		scoreFile.close()

		QWidget.__init__(self,parent)
		self.setFixedSize(320,400)
		self.setWindowTitle("2048 Original Mode")
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		self.gameRunning=False
		self.panelHeight=80

		self.backgroundBrush=QBrush(QBrush(QColor(0x4b4b4b)))
		self.gridSize=gridSize
		self.tileMargin=16
		self.gridOffsetX=self.tileMargin
		self.gridOffsetY=self.panelHeight+self.tileMargin
		self.brushes={
			0:QBrush(QColor(0x979797)),
			1:QBrush(QColor(0x979797)),
			2:QBrush(QColor(0xA19C9A)),
			4:QBrush(QColor(0xA19C9A)),
			8:QBrush(QColor(0xA19C9A)),
			16:QBrush(QColor(0xA19C9A)),
			32:QBrush(QColor(0xA19C9A)),
			64:QBrush(QColor(0xA19C9A)),
			128:QBrush(QColor(0xA19C9A)),
			256:QBrush(QColor(0xA19C9A)),
			512:QBrush(QColor(0xA19C9A)),
			1024:QBrush(QColor(0xA19C9A)),
			2048:QBrush(QColor(0xA19C9A)),
		}
		self.lightPen=QPen(QColor(0xf9f6f2))
		self.darkPen=QPen(QColor(0x776e65))
		self.scoreRect=QRect(10,10,80,self.panelHeight-20)
		self.hiScoreRect=QRect(100,10,80,self.panelHeight-20)
		self.resetRect=QRectF(190,10,80,self.panelHeight-20)
		self.scoreLabel=QRectF(10,25,80,self.panelHeight-30)
		self.hiScoreLabel=QRectF(100,25,80,self.panelHeight-30)
		self.hiScore=score
		self.lastPoint=None
		self.resize(QSize(width,width+self.panelHeight))
		self.reset_game()

	def resizeEvent(self,e):
		width=min(e.size().width(),e.size().height()-self.panelHeight)
		self.tileSize=(width-self.tileMargin*(self.gridSize+1))/self.gridSize
		self.font=QFont('Arial',self.tileSize/4)

	#Procédure pour changer la taille du plateau (non utilisé dans cette version)
	def changeGridSize(self,x):
		self.gridSize=x
		self.reset_game()

	#Lancer une nouvelle partie.
	def reset_game(self):
		self.tiles=[[None for i in range(0,self.gridSize)] for i in range(0,self.gridSize)]
		self.availableSpots=range(0,self.gridSize*self.gridSize)
		self.score=0
		self.addTile()
		self.addTile()
		self.update()
		self.gameRunning=True

	#Ajouter une nouvelle tuile sur le plateau.
	def addTile(self):
		if len(self.availableSpots)>0:
			x = random.random()
			if x<0.8 :
				v = 2
			else :
				v = 4
			i=self.availableSpots[int(random.random()*len(self.availableSpots))]
			gridX=i%self.gridSize
			gridY=i/self.gridSize
			self.tiles[int(gridX)][int(gridY)]=Tile(v)

	#Procédure appelée quand l'utilisateur appuie sur la touche UP_KEY
	def up(self):
		moved=False
		for gridX in range(0,self.gridSize) :
			for gridY in range(1,self.gridSize):
				if self.tiles[gridX][gridY] is not None:
					i=gridY
					while i-1>=0 and self.tiles[gridX][i-1] is None:
						i-=1
					if i-1>=0 and self.tiles[gridX][i-1].value==self.tiles[gridX][gridY].value:
						self.score+=self.tiles[gridX][gridY].value*2
						self.tiles[gridX][i-1].value*=2
						self.tiles[gridX][gridY]=None
						moved=True
					elif i<gridY:
						self.tiles[gridX][i]=self.tiles[gridX][gridY]
						self.tiles[gridX][gridY]=None
						moved=True
		self.updateTiles()

	#Procédure appelée quand l'utilisateur appuie sur la touche DOWN_KEY
	def down(self):
		moved=False
		for gridX in range(0,self.gridSize) :
			for gridY in range(self.gridSize-2,-1,-1):
				if self.tiles[gridX][gridY] is not None:
					i=gridY
					while i+1<self.gridSize and self.tiles[gridX][i+1] is None:
						i+=1
					if i+1<self.gridSize and self.tiles[gridX][i+1].value==self.tiles[gridX][gridY].value:
						self.score+=self.tiles[gridX][gridY].value*2
						self.tiles[gridX][i+1].value*=2
						self.tiles[gridX][gridY]=None
						moved=True
					elif i>gridY:
						self.tiles[gridX][i]=self.tiles[gridX][gridY]
						self.tiles[gridX][gridY]=None
						moved=True
		self.updateTiles()

	#Procédure appelée quand l'utilisateur appuie sur la touche LEFT_KEY
	def left(self):
		moved=False
		for gridX in range(1,self.gridSize):
			for gridY in range(0,self.gridSize):
				if self.tiles[gridX][gridY] is not None:
					i=gridX
					while i-1>=0 and self.tiles[i-1][gridY] is None:
						i-=1
					if i-1>=0 and self.tiles[i-1][gridY].value==self.tiles[gridX][gridY].value:
						self.score+=self.tiles[gridX][gridY].value*2
						self.tiles[i-1][gridY].value*=2
						self.tiles[gridX][gridY]=None
						moved=True
					elif i<gridX:
						self.tiles[i][gridY]=self.tiles[gridX][gridY]
						self.tiles[gridX][gridY]=None
						moved=True
		self.updateTiles()

	#Procédure appelée quand l'utilisateur appuie sur la touche DOWN_KEY
	def right(self):
		moved=False
		for gridX in range(self.gridSize-2,-1,-1):
			for gridY in range(0,self.gridSize):
				if self.tiles[gridX][gridY] is not None:
					i=gridX
					while i+1<self.gridSize and self.tiles[i+1][gridY] is None:
						i+=1
					if i+1<self.gridSize and self.tiles[i+1][gridY].value==self.tiles[gridX][gridY].value:
						self.score+=self.tiles[gridX][gridY].value*2
						self.tiles[i+1][gridY].value*=2
						self.tiles[gridX][gridY]=None
						moved=True
					elif i>gridX:
						self.tiles[i][gridY]=self.tiles[gridX][gridY]
						self.tiles[gridX][gridY]=None
						moved=True
		self.updateTiles()

	#Procédure pour mettre à jour les tuiles et contrôler si l'utilisateur a gagné, perdu, ou si il continue a jouer.
	def updateTiles(self):
		self.availableSpots=[]
		for i in range(0,self.gridSize):
			for j in range(0,self.gridSize):
				if self.tiles[i][j] is None:
					self.availableSpots.append(i+j*self.gridSize)
		self.addTile()
		self.hiScore=max(self.score,self.hiScore)

		#Sauvegarde du High-score
		scoreFile = open("score.txt", "w")
		scoreFile.write(str(self.hiScore))
		scoreFile.close()

		self.update()

		if not self.movesAvailable():
			self.loseDialog()
		elif self.testWin() :
			self.winDialog()

	#Procédure qui détermine si l'utilisateur peut déplacer les tuiles.
	def movesAvailable(self):
		if not len(self.availableSpots)==0:
			return True
		for i in range(0,self.gridSize):
			for j in range(0,self.gridSize):
				if i<self.gridSize-1 and self.tiles[i][j].value==self.tiles[i+1][j].value:
					return True
				if j<self.gridSize-1 and self.tiles[i][j].value==self.tiles[i][j+1].value:
					return True
		return False

	#Procédure pour tester si l'utilisateur a gagné la partie.
	def testWin(self):
		for i in range(self.gridSize):
			for j in range(self.gridSize):
				if(self.tiles[i][j] != None):
					if(self.tiles[i][j].value == 2048):
						return True
		return False

	#Procédure pour capturer les entrées clavier de l'utilisateur.
	def keyPressEvent(self,e):
		if not self.gameRunning:
			return
		if e.key()==Qt.Key_Escape:
			self.backToMenu()
		elif e.key()==Qt.Key_Up:
			self.up()
		elif e.key()==Qt.Key_Down:
			self.down()
		elif e.key()==Qt.Key_Left:
			self.left()
		elif e.key()==Qt.Key_Right:
			self.right()

	#Procédure pour capturer la position de la souris lors d'un clic.
	def mousePressEvent(self,e):
		self.lastPoint=e.pos()

	#Procédure permettant de déplacer les tuiles lors d'un relâchement de clic.
	def mouseReleaseEvent(self,e):
		if self.resetRect.contains(self.lastPoint.x(),self.lastPoint.y()) and self.resetRect.contains(e.pos().x(),e.pos().y()):
			if QMessageBox.question(self,'','Are you sure you want to start a new game?',
					QMessageBox.Yes,QMessageBox.No)==QMessageBox.Yes:
				self.reset_game()
		elif self.gameRunning and self.lastPoint is not None:
			dx=e.pos().x()-self.lastPoint.x()
			dy=e.pos().y()-self.lastPoint.y()
			if abs(dx)>abs(dy) and abs(dx)>10:
				if dx>0:
					self.right()
				else:
					self.left()
			elif abs(dy)>10:
				if dy>0:
					self.down()
				else:
					self.up()

	#Procédure permettant de retourner au menu principal de l'application.
	def backToMenu(self):
		backDialog = QMessageBox(self)
		backDialog.setWindowTitle("Return to main menu")
		backDialog.setText("Do you really want to return to the main menu ? \nThis action will end your game.")
		backDialog.setStyleSheet('QMessageBox {font-size:13px;}')
		backDialog.setIcon(QMessageBox.Question)
		backDialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		backDialog.setDefaultButton(QMessageBox.Cancel)
		if backDialog.exec_() == QMessageBox.Ok:
			self.hide()
			self.menu = Menu.Menu()
			self.menu.show()

	#MessageBox qui s'affiche lorsque l'utilisateur a perdu la partie.
	def loseDialog(self):
		loseDialog = QMessageBox(self)
		loseDialog.setWindowTitle("You lose :(")
		loseDialog.setText("You don't have any moves available.\nYour score is : " + str(self.score) + ".\nDo you want to start a new game ?")
		loseDialog.setStyleSheet('QMessageBox {font-size:13px;}')
		loseDialog.setIcon(2)
		loseDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		self.gameRunning = False
		if loseDialog.exec_() == QMessageBox.Yes:
			self.game = Game2048(None,340,4)
			self.hide()
			self.game.show()
		else :
			self.hide()
			self.menu = Menu.Menu()
			self.menu.show()

	#MessageBox qui s'affiche lorsque l'utilisateur a gagné la partie.
	def winDialog(self):
		winDialog = QMessageBox(self)
		winDialog.setWindowTitle("You win !")
		winDialog.setText("Congratulations you reach 2048 !\nYour score is : " + str(self.score) + ".\nDo you want to start a new game ?")
		winDialog.setStyleSheet('QMessageBox {font-size:13px}')
		winDialog.setIcon(1)
		winDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		self.gameRunning = False
		if winDialog.exec_() == QMessageBox.Yes:
			self.game = Game2048(None,340,4)
			self.hide()
			self.game.show()
		else :
			self.hide()
			self.menu = Menu.Menu()
			self.menu.show()

	#PaintEvent
	def paintEvent(self,event):
		painter = QPainter(self)
		painter.setPen(Qt.NoPen)
		painter.setBrush(self.backgroundBrush)
		painter.drawRect(self.rect())
		painter.setBrush(self.brushes[1])
		painter.drawRoundedRect(self.scoreRect,10.0,10.0)
		painter.drawRoundedRect(self.hiScoreRect,10.0,10.0)
		painter.drawRoundedRect(self.resetRect,10.0,10.0)
		painter.setFont(QFont('Arial',9))
		painter.setPen(self.darkPen)
		painter.drawText(QRectF(10,15,80,20),'SCORE',QTextOption(Qt.AlignHCenter|Qt.AlignVCenter))
		painter.drawText(QRectF(100,15,80,20),'HIGHSCORE',QTextOption(Qt.AlignHCenter|Qt.AlignVCenter))
		painter.setFont(QFont('Arial',15))
		painter.setPen(self.lightPen)
		painter.drawText(self.resetRect,'RESET',QTextOption(Qt.AlignHCenter|Qt.AlignVCenter))
		painter.setFont(QFont('Arial',15))
		painter.setPen(self.lightPen)
		painter.drawText(self.scoreLabel,str(self.score),QTextOption(Qt.AlignHCenter|Qt.AlignVCenter))
		painter.drawText(self.hiScoreLabel,str(self.hiScore),QTextOption(Qt.AlignHCenter|Qt.AlignVCenter))
		painter.setFont(self.font)
		for gridX in range(0,self.gridSize):
			for gridY in range(0,self.gridSize):
				tile = self.tiles[gridX][gridY]
				if tile is None:
					painter.setBrush(self.brushes[0])
				else:
					painter.setBrush(self.brushes[tile.value])
				rect=QRectF(self.gridOffsetX+gridX*(self.tileSize+self.tileMargin),
										self.gridOffsetY+gridY*(self.tileSize+self.tileMargin),
										self.tileSize,self.tileSize)
				painter.setPen(Qt.NoPen)
				painter.drawRoundedRect(rect,10.0,10.0)
				if tile is not None:
					if tile.value == 2 :
						painter.drawImage(rect,QImage("img/Game2048/trump.png"))
					if tile.value == 4 :
						painter.drawImage(rect,QImage("img/Game2048/kim.png"))
					if tile.value == 8 :
						painter.drawImage(rect,QImage("img/Game2048/poutine.png"))
					if tile.value == 16 :
						painter.drawImage(rect,QImage("img/Game2048/macron.png"))
					if tile.value == 32 :
						painter.drawImage(rect,QImage("img/Game2048/eli.png"))
					if tile.value == 64 :
						painter.drawImage(rect,QImage("img/Game2048/merkel.png"))
					if tile.value == 128 :
						painter.drawImage(rect,QImage("img/Game2048/tamin.png"))
					if tile.value == 256 :
						painter.drawImage(rect,QImage("img/Game2048/xi.png"))
					if tile.value == 512 :
						painter.drawImage(rect,QImage("img/Game2048/kersti.png"))
					if tile.value == 1024 :
						painter.drawImage(rect,QImage("img/Game2048/temer.png"))
					if tile.value == 2048 :
						painter.drawImage(rect,QImage("img/Game2048/obama.png"))