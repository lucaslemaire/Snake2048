#!/usr/bin/python3
import sys,time
from random import randrange
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from math import *
from PyQt5.QtGui import *
import Menu as Menu
from Tutorial import *
from PyQt5.QtMultimedia import *

class Tile:
    def __init__(self,value):
        self.value=value

class Snake(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.newGame()
        self.setFixedSize(800, 600)
        self.setWindowTitle('2048 snake')
        p = QPalette()
        p.setColor(QPalette.Window, QColor(0x808080))
        self.setPalette(p)



    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.jeu==True :
            self.placeFood(qp)
            self.drawSnake(qp)
            self.stockLeft(qp)
            self.stockRight(qp)
            self.stockerFood(qp)
            self.printScore(event,qp)
            self.printVie(event,qp)

        else:
            self.gameOver(event,qp)

        if self.isPaused==True and self.jeu==True:
            self.printEvent(event,qp)
        if self.win == True:
            self.gameWin(event,qp)
        
        qp.end()

#Affiche le score 

    def printScore(self,event , qp) :
        qp.setPen(QColor(Qt.black))

        qp.setFont(QFont('Helvetica', 10))
        qp.drawText(QRectF(530,10,100,20), Qt.AlignCenter, "SCORE : "+ str(self.score))

#Affiche la vie 

    def printVie(self, event ,qp) :
        if self.vie == 3 :
            qp.drawImage(QPointF(100,0),QImage('img/GameSnake/Coeur.png').scaled(30,30))
            qp.drawImage(QPointF(120,0),QImage('img/GameSnake/Coeur.png').scaled(30,30))
            qp.drawImage(QPointF(140,0),QImage('img/GameSnake/Coeur.png').scaled(30,30))

        elif self.vie == 2 :
            qp.drawImage(QPointF(100,0),QImage('img/GameSnake/Coeur.png').scaled(30,30))
            qp.drawImage(QPointF(120,0),QImage('img/GameSnake/Coeur.png').scaled(30,30))
            qp.drawImage(QPointF(143,2),QImage('img/GameSnake/Coeur_grey.png').scaled(25,27))

        elif self.vie == 1 :
            qp.drawImage(QPointF(100,0),QImage('img/GameSnake/Coeur.png').scaled(30,30))
            qp.drawImage(QPointF(123,1),QImage('img/GameSnake/Coeur_grey.png').scaled(25,27))
            qp.drawImage(QPointF(143,1),QImage('img/GameSnake/Coeur_grey.png').scaled(25,27))
        elif self.vie == 0 :
            qp.drawImage(QPointF(103,1),QImage('img/GameSnake/Coeur_grey.png').scaled(25,27))
            qp.drawImage(QPointF(123,1),QImage('img/GameSnake/Coeur_grey.png').scaled(25,27))
            qp.drawImage(QPointF(143,1),QImage('img/GameSnake/Coeur_grey.png').scaled(25,27))

#Affiche "Pause" quand le jeu est en pause  

    def printEvent(self,event,qp) :
        qp.setPen(QColor(Qt.black))
        qp.setFont(QFont('Decorative', 50))
        qp.drawText(event.rect(), Qt.AlignCenter, "PAUSE")
        qp.setFont(QFont('Decorative', 15))
        qp.drawText(QRectF((self.width()/2)-100,200,200,300), Qt.AlignCenter, "P to unpause !")

#Affiche "You Win" quand le jeu est gagner 

    def gameWin(self, event, qp):
        qp.setPen(QColor(Qt.black))
        qp.setFont(QFont('Decorative', 40))
        qp.drawText(event.rect(), Qt.AlignCenter, "YOU WIN")
        qp.setFont(QFont('Decorative', 15))
        qp.drawText(QRectF((self.width()/2)-100,200,200,300), Qt.AlignCenter, "Key_Space to replay !")

#Affiche "Game over" quand le jeu est perdu 

    def gameOver(self, event, qp):
        qp.setPen(QColor(Qt.black))
        qp.setFont(QFont('Decorative', 40))
        qp.drawText(event.rect(), Qt.AlignCenter, "GAME OVER")
        qp.setFont(QFont('Decorative', 15))
        qp.drawText(QRectF((self.width()/2)-125,200,250,300), Qt.AlignCenter, "Key_Space to replay !")

#Affiche le stock de gauche  


    def stockLeft(self,qp) :
        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(QColor(0x260647)))
        qp.drawRect(0,0,100,600)
        for gridX in range(0,1):
            for gridY in range(0,8):
                tile = self.tiles1[gridX][gridY]
                if tile is None:
                    qp.setBrush(self.brushes[1])
                else :
                    qp.setBrush(self.brushes[tile.value])

                rect=QRectF(17+gridX*(60+16),5+gridY*(60+16),60,60)
                self.rect2 = rect
                qp.setPen(Qt.NoPen)
                qp.drawRoundedRect(rect,10.0,10.0)
                if tile is not None:
                    qp.setPen(self.darkPen if tile.value<16 else self.lightPen)
                    qp.drawText(self.rect2,str(tile.value),QTextOption(Qt.AlignHCenter|Qt.AlignVCenter))

#Stock la food dans les stocks 

    def stockerFood(self,qp) :
        if len(self.lista)>0 and self.oktruc==True:
            if self.FoodPlaced==True and self.ok==False and self.jeu==True:
                if self.v%2==0 :

                    for x in range(0,7) :
                        if self.tiles1[0][0] is not None and self.tiles1[0][0].value != self.lista[0]:
                            self.jeu=False
                        elif self.tiles1[0][x+1] is None and x+1==7:
                            self.tiles1[0][x+1]=Tile(self.lista[0])
                        elif self.tiles1[0][x] is None and self.tiles1[0][x+1] is not None :
                            self.tiles1[0][x]=Tile(self.lista[0])

                    for gridY in range(0,7) :
                        if self.tiles1[0][gridY] is not None and self.tiles1[0][gridY+1] is not None :
                            if self.tiles1[0][gridY].value==self.tiles1[0][gridY+1].value :
                                self.tiles1[0][gridY+1].value = self.tiles1[0][gridY+1].value+self.tiles1[0][gridY].value
                                if self.tiles1[0][gridY+1].value == 2048:
                                    self.win = True
                                self.tiles1[0][gridY]=None
                    self.ok=True
                else :

                    for x in range(0,7) :
                        if self.tiles2[0][0] is not None and self.tiles2[0][0].value != self.lista[0]:
                            self.jeu=False
                        elif self.tiles2[0][x+1] is None and x+1==7:
                            self.tiles2[0][x+1]=Tile(self.lista[0])
                        elif self.tiles2[0][x] is None and self.tiles2[0][x+1] is not None :
                            self.tiles2[0][x]=Tile(self.lista[0])

                    for gridX in range(0,7) :
                        if self.tiles2[0][gridX] is not None and self.tiles2[0][gridX+1] is not None:
                            if  self.tiles2[0][gridX+1].value==self.tiles2[0][gridX].value :
                                self.tiles2[0][gridX+1].value = self.tiles2[0][gridX+1].value+self.tiles2[0][gridX].value
                                if self.tiles2[0][gridX+1].value == 2048:
                                    self.win = True
                                self.tiles2[0][gridX]=None
                    self.ok=True



#Affiche le stock de droite 

    def stockRight(self,qp) :
        qp.setPen(Qt.NoPen)
        qp.setBrush(QBrush(QColor(0x260647)))
        qp.drawRect(700,0,100,600)
        for gridX in range(0,1):
            for gridY in range(0,8):
                tile = self.tiles2[gridX][gridY]
                if tile is None:
                    qp.setBrush(self.brushes[1])
                else :
                    qp.setBrush(self.brushes[tile.value])


                rect=QRectF(718+gridX*(60+16),5+gridY*(60+16),60,60)
                self.rect3=rect
                qp.setPen(Qt.NoPen)
                qp.drawRoundedRect(rect,10.0,10.0)
                if tile is not None:
                    qp.setPen(self.darkPen if tile.value<16 else self.lightPen)
                    qp.drawText(self.rect3,str(tile.value),QTextOption(Qt.AlignHCenter|Qt.AlignVCenter))

#récupére les directions 

    def keyPressEvent(self, e):
        if not self.isPaused:
            if e.key() == Qt.Key_Up and self.lastKeyPress != 'UP' and self.lastKeyPress != 'DOWN':
                self.direction("UP")
                self.lastKeyPress = 'UP'
            elif e.key() == Qt.Key_Down and self.lastKeyPress != 'DOWN' and self.lastKeyPress != 'UP':
                self.direction("DOWN")
                self.lastKeyPress = 'DOWN'
            elif e.key() == Qt.Key_Left and self.lastKeyPress != 'LEFT' and self.lastKeyPress != 'RIGHT':
                self.direction("LEFT")
                self.lastKeyPress = 'LEFT'
            elif e.key() == Qt.Key_Right and self.lastKeyPress != 'RIGHT' and self.lastKeyPress != 'LEFT':
                self.direction("RIGHT")
                self.lastKeyPress = 'RIGHT'
            elif e.key() == Qt.Key_P:
                self.pause()
            elif e.key() == Qt.Key_Escape :
                self.pause()
                self.menuTest()

        elif e.key() == Qt.Key_P:
            self.start()
        elif e.key() == Qt.Key_Space:
            self.newGame()

        elif e.key() == Qt.Key_Escape :
            self.pause()
            self.menuTest()

#Affiche le menu du snake 

    def menuTest(self ):
        self.w = QWidget()
        self.w.show()
        self.w.setFixedSize(320,375)
        self.setCenter(self.w)
        self.w.setWindowTitle("Snake2048")


        self.resume = QPushButton("Resume",self.w)
        self.resume.resize(160,35)
        self.resume.move(((self.w.width()//2)-self.resume.width()//2),120)
        self.resume.show()

        self.tuto=QPushButton("Tutorial",self.w)
        self.tuto.resize(160,35)
        self.tuto.move(((self.w.width()//2)-self.tuto.width()//2),170)
        self.tuto.show()

        self.menu=QPushButton("Menu",self.w)
        self.menu.resize(160,35)
        self.menu.move(((self.w.width()//2)-self.menu.width()//2),230)
        self.menu.show()

        self.labeltext = QLabel(self.w)
        self.labeltext.setAlignment(Qt.AlignCenter)
        self.labeltext.setGeometry(10,10,230,100)
        font = QFont("Arial",60,QFont.Bold)
        self.labeltext.setFont(font)
        self.labeltext.move(((self.w.width()//2)-self.labeltext.width()//2),10)
        self.labeltext.setText("<font color=\"#8226b6\">2</font><font color=\"#0f0f43\">0</font><font color=\"#8226b6\">4</font><font color=\"#0f0f43\">8</font>")
        self.labeltext.show()

        self.labelimage = QLabel(self.w)
        self.labelimage.setAlignment(Qt.AlignCenter)
        self.labelimage.setGeometry(0,280,400,95)
        self.labelimage.setPixmap(QPixmap('img/GameSnake/snakePicture.png').scaled(400,100))
        self.labelimage.show()

        self.resume.clicked.connect(self.backToSnake)
        self.menu.clicked.connect(self.backToMenu)
        self.tuto.clicked.connect(self.openTuto)

        self.menu.setStyleSheet('QPushButton {font-size:14px;background-color: #ff005c; border-style : outset;font-weight:bold;}')
        self.resume.setStyleSheet('QPushButton {font-size:14px;background-color: #0f0f43; border-style : outset;font-weight:bold;}')
        self.tuto.setStyleSheet('QPushButton {font-size:14px;background-color: #8226b6; border-style : outset;font-weight:bold;}')

#Retourne en jeu

    def backToSnake(self) :
        self.w.hide()

#Retourne au menu principal 

    def backToMenu(self):
        self.back=Menu.Menu()
        self.hide()
        self.w.hide()
        self.back.show()

#Affiche le tuto quand l'utilisateur appuie sur "Tutorial"

    def openTuto(self) :
        self.menu = QWidget()
        self.w.hide()
        self.menu.setFixedSize(320,400)
        self.menu.move((self.width()//2)+115,(self.height()//2)-150)

        self.retour = QPushButton("Return",self.menu)
        self.retour.resize(160,35)
        self.retour.setStyleSheet('QPushButton {font-size:14px;background-color: #ff005c; border-style : outset;font-weight:bold;}')
        self.retour.move(((self.menu.width()//2)-self.retour.width()//2),330)
        self.retour.show()





        self.label = QLabel(self.menu)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(10,10,230,100)
        font = QFont("Arial",23,QFont.Bold)
        self.label.setFont(font)
        self.label.move(((self.menu.width()//2)-self.label.width()//2),0)

        self.label1 = QLabel(self.menu)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setGeometry(10,10,230,120)
        font = QFont("Arial",13,QFont.Bold)
        self.label1.setFont(font)
        self.label1.move(110,75)

        self.escape = QLabel(self.menu)

        self.pixmapK = QPixmap('img/keyboard.png')
        self.pixmapE = QPixmap('img/escape.png')
        self.pixmapW = QPixmap('img/warn.png')

        self.keyboard = QLabel(self.menu)
        self.keyboard.setPixmap(self.pixmapK.scaled(146,99))
        self.keyboard.move(5,85)

        self.retour.clicked.connect(self.backToMenuSnake)


        self.escape.setPixmap(self.pixmapW.scaled(55,53))
        self.escape.move(20,225)
        self.escape.show()

        self.label.setText("Snake Mode")
        self.label.setStyleSheet('color : #0f0f43')
        self.label.show()

        self.label1.setText("Use arrow keys to\ncontrol the snake.")
        self.label1.setStyleSheet('color : #0f0f43')
        self.label1.show()

        self.label3 = QLabel(self.menu)
        font = QFont('Arial',13,QFont.Bold)
        self.label3.setFont(font)
        self.label3.setText("You lose if :\n\n - You touch yourself.\n - You hit sides of window.\n - One of your tiles column\n   is full.")
        self.label3.setStyleSheet('color : #0f0f43')
        self.label3.move(87,200)


        self.keyboard.show()
        self.menu.show()

#Retourne au menu du snake 

    def backToMenuSnake(self) :
        self.w.show()
        self.menu.hide()

#Centre        

    def setCenter(self, QWidget):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#Créer ue nouvelle game 

    def newGame(self):
        self.score = 0
        self.x = 120
        self.y = 40
        self.lastKeyPress = 'RIGHT'
        self.timer = QBasicTimer()
        self.snakeArray = [[self.x, self.y],[self.x+12, self.y+12]]
        self.lista = []
        self.foodx = 0
        self.foody = 0
        self.isPaused = False
        self.nb=0
        self.nb1=0
        self.randnb=0
        self.v=0
        self.isOver = False
        self.FoodPlaced = False
        self.choix=0
        self.choix1 = 0
        self.ok=False
        self.rect2=0
        self.rect3=0
        self.speed = 70
        self.jeu=True
        self.truc=0
        self.tiles1=[[None for i in range(0,8)] for i in range(0,1)]
        self.tiles2=[[None for i in range(0,8)] for i in range(0,1)]
        self.listTri1=[]
        self.t1 = []
        self.listTri2=[]
        self.t2 = []
        self.choix3 = 0
        self.test = False
        self.oktruc=True
        self.vie = 3
        self.win = False

        self.lightPen=QPen(QColor(0xf9f6f2))
        self.darkPen=QPen(QColor(0x776e65))
        self.brushes={
            0:QBrush(QColor(0xcdc1b4)),
            1:QBrush(QColor(0x884EC7)),
            2:QBrush(QColor(0xEEE4DA)),
            4:QBrush(QColor(0xFFF655)),
            8:QBrush(QColor(0xF7E12A)),
            16:QBrush(QColor(0xF7B22F)),
            32:QBrush(QColor(0xFF392C)),
            64:QBrush(QColor(0x7BFF3C)),
            128:QBrush(QColor(0x4AC71D)),
            256:QBrush(QColor(0x40E0C6)),
            512:QBrush(QColor(0x00AEFF)),
            1024:QBrush(QColor(0xD346FF)),
            2048:QBrush(QColor(0x7E1CE8)),
        }
        self.start()

#Met le jeu en pause 

    def pause(self):
        self.isPaused = True
        self.timer.stop()
        self.update()

#Redémarre le jeu 

    def start(self):
        self.isPaused = False
        self.timer.start(self.speed, self)
        self.update()

#Fait bouger le snake 

    def direction(self, dir):
        if (dir == "DOWN" and self.checkStatus(self.x, self.y+20)):
            self.y += 20
            self.repaint()
            self.snakeArray.insert(0 ,[self.x, self.y])


        elif (dir == "UP" and self.checkStatus(self.x, self.y-20)):
            self.y -= 20
            self.repaint()
            self.snakeArray.insert(0 ,[self.x, self.y])


        elif (dir == "RIGHT" and self.checkStatus(self.x+20, self.y)):
            self.x += 20
            self.repaint()
            self.snakeArray.insert(0 ,[self.x, self.y])


        elif (dir == "LEFT" and self.checkStatus(self.x-20, self.y)):
            self.x -= 20
            self.repaint()
            self.snakeArray.insert(0 ,[self.x, self.y])


#Vérifie le statue du snake 


    def checkStatus(self, x, y):
        if y > 590 or x > 690 or x < 96 or y < 0:
            self.pause()
            self.isPaused = True
            self.jeu = False
            return False
        elif self.snakeArray[0] in self.snakeArray[1:len(self.snakeArray)]:
            self.pause()
            self.isPaused = True
            self.jeu=False
            return False
        elif self.y == self.foody and self.x == self.foodx:
            self.FoodPlaced = False
            self.ok=False
            self.v+=1
            self.oktruc=True

            if self.choix == 8 :
                self.lista.insert(0,8)
            elif self.choix == 16 :
                self.lista.insert(0,16)

            self.score += self.lista[0]

            return True

        elif self.y == self.foody1 and self.x == self.foodx1:
            self.FoodPlaced = False
            self.ok=False
            self.v+=1
            self.oktruc=True
            if self.choix1 == 8 :
                self.lista.insert(0,8)
            elif self.choix1 == 16 :
                self.lista.insert(0,16)
            self.score += self.lista[0]


            return True


        elif self.y == self.foody2 and self.x == self.foodx2 :
            self.FoodPlaced = False
            self.ok=False
            self.v+=1
            self.oktruc=False

            if self.choix3 == 0 :
                self.oktruc=False
                self.FoodPlaced = False
                self.ok=False

                self.snakeArray = [[self.x, self.y],[self.x+12, self.y+12]]
            elif self.choix3 == 1 :

                if len(self.lista)>0 :

                    self.listTri1=[]
                    for x in range(0,8) :
                        if self.tiles1[0][x] is not None :
                            self.listTri1.append(self.tiles1[0][x].value)
                    self.t1 = sorted(self.listTri1)

                    indice = 0
                    for gridY in range(0,8) :
                        if self.tiles1[0][gridY] is not None :
                            self.tiles1[0][gridY].value = self.t1[indice]
                            indice+=1

                    for gridY2 in range(0,7) :
                        if self.tiles1[0][gridY2] is not None and self.tiles1[0][gridY2+1] is not None :
                             if  self.tiles1[0][gridY2+1].value==self.tiles1[0][gridY2].value :
                                self.tiles1[0][gridY2+1].value = self.tiles1[0][gridY2+1].value+self.tiles1[0][gridY2].value
                                self.tiles1[0][gridY2]=None

                    self.t1 = []

                    for x in range(0,8) :
                        if self.tiles1[0][x] is not None :
                            self.t1.append(self.tiles1[0][x].value)

                    self.t1 = sorted(self.t1)
                    self.t1.reverse()

                    for i in range(0,8) :
                        if self.tiles1[0][i] is not None :
                            self.tiles1[0][i] = None

                    indice=0
                    istock = 7
                    while indice < len(self.t1) :
                        self.tiles1[0][istock]=Tile(self.t1[indice])
                        istock-=1
                        indice+=1





                    self.listTri2=[]
                    for x in range(0,8) :
                        if self.tiles2[0][x] is not None :
                            self.listTri2.append(self.tiles2[0][x].value)
                    self.t2 = sorted(self.listTri2)

                    indice = 0
                    for gridY in range(0,8) :
                        if self.tiles2[0][gridY] is not None :
                            self.tiles2[0][gridY].value = self.t2[indice]
                            indice+=1

                    for gridY2 in range(0,7) :
                        if self.tiles2[0][gridY2] is not None and self.tiles2[0][gridY2+1] is not None :
                             if  self.tiles2[0][gridY2+1].value==self.tiles2[0][gridY2].value :
                                self.tiles2[0][gridY2+1].value = self.tiles2[0][gridY2+1].value+self.tiles2[0][gridY2].value
                                self.tiles2[0][gridY2]=None

                    self.t2 = []


                    for x in range(0,8) :
                        if self.tiles2[0][x] is not None :
                            self.t2.append(self.tiles2[0][x].value)
                    self.t2 = sorted(self.t2)
                    self.t2.reverse()



                    for i in range(0,8) :
                        if self.tiles2[0][i] is not None :
                            self.tiles2[0][i] = None



                    indice=0
                    istock = 7
                    while indice < len(self.t2) :
                        self.tiles2[0][istock]=Tile(self.t2[indice])
                        istock-=1
                        indice+=1

            elif self.choix3 == 2 :
                if self.vie == 0 :
                    self.jeu=False 
                else :
                    self.vie-=1

        self.snakeArray.pop()
        return True

#Place la food 

    def placeFood(self, qp):
        if self.FoodPlaced == False:
            self.foodx = randrange(10,24)*20
            self.foody = randrange(2, 24)*20

            self.foodx1 = randrange(10,24)*20
            self.foody1 = randrange(2,24)*20

            self.foodx2 = randrange(10,24)*20
            self.foody2 = randrange(2,24)*20

            if self.foody2 == self.foody1 or self.foody2 == self.foody :
                self.foody2 = randrange(2,24)*20
            if self.foodx2 == self.foodx2 or self.foodx2 == self.foodx :
                self.foodx2 = randrange(10,24)*20


            self.nb=randrange(0,100)
            self.nb1=randrange(0,100)
            self.nb3=randrange(0,100)


            if not [self.foodx, self.foody] in self.snakeArray:
                self.FoodPlaced = True
            else :
                self.FoodPLaced = False

            if not [self.foodx1, self.foody1] in self.snakeArray:
                self.FoodPlaced = True
            else :
                self.FoodPLaced = False

        if self.nb3<=30 :
            img3= QImage('img/GameSnake/Trie.png')
            self.choix3=1
        elif self.nb3 >=31 and self.nb3<=50 :
            img3= QImage('img/GameSnake/reset.png')
            self.choix3=0
        else :
            img3 = QImage('img/GameSnake/bombe.png')
            self.choix3=2


        if self.nb>=0 and self.nb<=60 :
            img = QImage('img/GameSnake/8.png')
            self.choix=8
        else :
            img = QImage('img/GameSnake/16.png')
            self.choix=16



        if self.nb1>=0 and self.nb1<=60 :
            img2 = QImage('img/GameSnake/8.png')
            self.choix1=8
        else :
            img2 = QImage('img/GameSnake/16.png')
            self.choix1=16


        rect=QRect(self.foodx,self.foody,20,20)
        rect2=QRect(self.foodx1,self.foody1,20,20)
        rect3=QRect(self.foodx2,self.foody2,20,20)

        qp.drawImage(rect,img)
        qp.drawImage(rect2,img2)
        qp.drawImage(rect3,img3)



#Draw le snake 

    def drawSnake(self, qp):
        qp.setPen(Qt.NoPen)
        img = QImage('img/GameSnake/rond-purple.png')

        for i in self.snakeArray:
            rect = QRect(i[0], i[1], 20, 20)
            qp.drawImage(rect,img)
            qp.drawRect(rect)


#Minuteur 

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.direction(self.lastKeyPress)
            self.repaint()
        else:
            QFrame.timerEvent(self, event)
