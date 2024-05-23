# -*- coding: utf-8 -*-
"""
Created on Fri Dec 01 17:04:07 2017

@author: fourn
"""

import pygame
from pygame.locals import *

import random

from constants import *

#from sys import maxSize

maxSize = 10000

class Board:
    def __init__(self, s, n):
        self.board = None
        self.size = s
        self.numberPiece = n
    
    
    def boardGeneration(self):
        tempBoard = []
        for i in range(self.size):
            tempLine = []
            for j in range(self.size):
                if i%2 == 0 and j%2 == 0:
                    tempLine.append(0)
                elif i%2 == 1 and j%2 == 1:
                    tempLine.append(0)
                else:
                    tempLine.append(1)
            tempBoard.append(tempLine)
        self.board = tempBoard
    
    
    def initializationPieces(self):
        compteur = self.numberPiece
        i = 0
        j = 0
        while compteur > 0:
            if i < self.size:
                if j < self.size:
                    if self.board[i][j] == 1:
                        self.board[i][j] = 2
                        compteur -= 1
                    j += 1
                else:
                    i += 1
                    j = 0
            else:
                break
        
        compteur = self.numberPiece
        i = self.size - 1
        j = self.size - 1
        while compteur > 0:
            if i >= 0:
                if j >= 0:
                    if self.board[i][j] == 1:
                        self.board[i][j] = 3
                        compteur -= 1
                    j -= 1
                else:
                    i -= 1
                    j = self.size - 1
            else:
                break
    
    
    def show(self,window):
        
        beigeCell = pygame.image.load(image_beigeCell).convert_alpha()
        brownCell = pygame.image.load(image_brownCell).convert_alpha()
        beigePiece = pygame.image.load(image_beigePiece).convert_alpha()
        blackPiece = pygame.image.load(image_blackPiece).convert_alpha()
        beigeKing = pygame.image.load(image_beigeKing).convert_alpha()
        blackKing = pygame.image.load(image_blackKing).convert_alpha()
        
        for i in range(self.size):
            for j in range(self.size):
                #Calcule la position réelle en pixel
                y = i * cellSize
                x = j * cellSize
                if self.board[i][j] == 0:
                    window.blit(beigeCell,(x,y))
                elif self.board[i][j] == 1:
                    window.blit(brownCell,(x,y))
                elif self.board[i][j] == 2:
                    window.blit(brownCell,(x,y))
                    window.blit(beigePiece,(x + 4.5,y + 4.5))
                elif self.board[i][j] == 3:
                    window.blit(brownCell,(x,y))
                    window.blit(blackPiece,(x + 4.5,y + 4.5))
                elif self.board[i][j] == 4:
                    window.blit(brownCell,(x,y))
                    window.blit(beigeKing,(x + 4.5,y + 4.5))                
                elif self.board[i][j] == 5:
                    window.blit(brownCell,(x,y))
                    window.blit(blackKing,(x + 4.5,y + 4.5))
        pygame.display.update()
       
    def printBoard(self):
        print("\n")
        for i in range(self.size):
            print(self.board[i])
            
        
    def possibilities(self,i,j):
        p = []
        currentCell = self.board[i][j]
        if currentCell < 2:
            return p
        
        #Piece
        elif currentCell < 4:
            mvt = 1
            if currentCell == 3:
                mvt = mvt * -1
            
            #Gauche
            if (i + mvt < self.size and i + mvt >= 0) and (j - 1 < self.size and j - 1 >= 0):
                tryCell = self.board[i + mvt][j - 1]
                if(tryCell == 1):
                    p.append([0,i + mvt,j - 1])
                elif(tryCell % 2 != currentCell % 2):
                    if(i + 2*mvt < self.size and i + 2*mvt >=0) and (j - 2 < self.size and j - 2 >= 0):
                        if(self.board[i + 2*mvt][j - 2] == 1):
                            p.append([1, i + 2*mvt, j - 2, i + mvt, j - 1])
            
            #Droite
            if (i + mvt < self.size and i + mvt >=0) and (j + 1 < self.size and j + 1 >= 0):
                tryCell = self.board[i + mvt][j + 1]
                if(tryCell == 1):
                    p.append([0,i + mvt,j + 1])
                elif(tryCell % 2 != currentCell % 2):
                    if(i + 2*mvt < self.size and i + 2*mvt >=0) and (j + 2 < self.size and j + 2 >= 0):
                        if(self.board[i + 2*mvt][j + 2] == 1):
                            p.append([1, i + 2*mvt, j + 2, i + mvt, j + 1])
        
        #King
        elif currentCell < 6:
            
            #Diagonale haut gauche
            l = i - 1
            c = j - 1
            while l >= 0 and c >= 0:
                tryCell = self.board[l][c]
                if tryCell == 1:
                    p.append([0,l,c])
                    l -= 1
                    c -= 1
                elif tryCell % 2 != currentCell % 2:
                    if l - 1 >= 0 and c - 1 >= 0:
                        if self.board[l - 1][c - 1] == 1:
                            p.append([1, l - 1, c - 1, l, c])
                    break
                else:
                    break
            
            #Diagonale haut droit
            l = i - 1
            c = j + 1
            while l >= 0 and c < self.size:
                tryCell = self.board[l][c]
                if tryCell == 1:
                    p.append([0,l,c])
                    l -= 1
                    c += 1
                elif tryCell % 2 != currentCell % 2:
                    if l - 1 >= 0 and c + 1 < self.size:
                        if self.board[l - 1][c + 1] == 1:
                            p.append([1, l - 1, c + 1, l, c])
                    break
                else:
                    break
            
            #Diagonale bas gauche
            l = i + 1
            c = j - 1
            while l < self.size and c >= 0:
                tryCell = self.board[l][c]
                if tryCell == 1:
                    p.append([0,l,c])
                    l += 1
                    c -= 1
                elif tryCell % 2 != currentCell % 2:
                    if l + 1 < self.size and c - 1 >= 0:
                        if self.board[l + 1][c - 1] == 1:
                            p.append([1, l + 1, c - 1, l, c])
                    break
                else:
                    break
            
            #Diagonale bas droit
            l = i + 1
            c = j + 1
            while l < self.size and c < self.size:
                tryCell = self.board[l][c]
                if tryCell == 1:
                    p.append([0,l,c])
                    l += 1
                    c += 1
                elif tryCell % 2 != currentCell % 2:
                    if l + 1 < self.size and c + 1 < self.size:
                        if self.board[l + 1][c + 1] == 1:
                            p.append([1, l + 1, c + 1, l, c])
                    break
                else:
                    break
        
        return p
        
    def showPossibilities(self,window,pos):
        greenPiece = pygame.image.load(image_greenPiece).convert_alpha()
        
        for i in range(len(pos)):
            y = pos[i][1] * cellSize
            x = pos[i][2] * cellSize
            window.blit(greenPiece,(x + 4.5,y + 4.5))
        pygame.display.update()
    
    def showJumpedPiece(self,window,force):
        highlightPiece = pygame.image.load(image_highlightPiece).convert_alpha()
        beigePiece = pygame.image.load(image_beigePiece).convert_alpha()
        blackPiece = pygame.image.load(image_blackPiece).convert_alpha()
        beigeKing = pygame.image.load(image_beigeKing).convert_alpha()
        blackKing = pygame.image.load(image_blackKing).convert_alpha()
        
        for i in range(len(force)):
            y = force[i][4] * cellSize
            x = force[i][5] * cellSize
            window.blit(highlightPiece,(x,y))
            if self.board[force[i][4]][force[i][5]] == 2:
                window.blit(beigePiece,(x + 4.5,y + 4.5))
            elif self.board[force[i][4]][force[i][5]] == 3:
                window.blit(blackPiece,(x + 4.5,y + 4.5))
            elif self.board[force[i][4]][force[i][5]] == 4:
                window.blit(beigeKing,(x + 4.5,y + 4.5))
            elif self.board[force[i][4]][force[i][5]] == 5:
                window.blit(blackKing,(x + 4.5,y + 4.5))
        pygame.display.update()
    
    def showPossibilitiesJumpedPiece(self,window,pos):
        greenPiece = pygame.image.load(image_greenPiece).convert_alpha()
        
        for i in range(len(pos)):
            if pos[i][0] == 1:
                y = pos[i][1] * cellSize
                x = pos[i][2] * cellSize
                window.blit(greenPiece,(x + 4.5,y + 4.5))
        pygame.display.update()
                

    def jumpNotPlay(self,player):
        force = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] >=2:
                    if self.board[i][j] % 2 == player % 2:
                        pos = self.possibilities(i,j)
                        if len(pos) != 0:
                            for k in range(len(pos)):
                                if pos[k][0] == 1:
                                    l = [i,j]
                                    for a in range(1,len(pos[k])):
                                        l.append(pos[k][a])         # [ii,ji,if,jf,is,js]
                                    force.append(l)
        return force


    def mouvement(self,ii,ji,pos):
        if pos[0] == 1:
            self.board[pos[3]][pos[4]] = 1
        if self.board[ii][ji] == 2 and pos[1] == self.size-1:
            self.board[pos[1]][pos[2]] = 4
        elif self.board[ii][ji] == 3 and pos[1] == 0:
            self.board[pos[1]][pos[2]] = 5
        else:
            self.board[pos[1]][pos[2]] = self.board[ii][ji]
        self.board[ii][ji] = 1


    
    def copyBoard(self):
        tempBoard = []
        for i in range(self.size):
            tempLine = []
            for j in range(self.size):
                tempLine.append(self.board[i][j])
            tempBoard.append(tempLine)
        return tempBoard


    def win(self):
        p1 = 0
        p2 = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] < 2:
                    a = 1
                elif self.board[i][j] % 2 == 0:
                    p1 += 1
                else:
                    p2 += 1
        
        if p1 == 0:
            return 2
        elif p2 == 0:
            return 3
        return 0


class IA:
    def __init__(self,b):
        self.board = b
        self.currentPlayer = None
    
    def maxi(self,board,depth,p):
        if depth == 0 or board.win() != 0:
            return self.evaluation(board)
        
        maximum = -maxSize
        tmp = 0
        
        force = board.jumpNotPlay(p)
        
        if len(force) != 0:
            for i in range(len(force)):
                piece = board.board[force[i][4]][force[i][5]]
                board.mouvement(force[i][0],force[i][1],[1,force[i][2],force[i][3],force[i][4],force[i][5]])
                
                tmp = self.mini(board,depth-1,p % 2 + 3)
                
                rand = random.randint(0,1)
                if tmp > maximum or (tmp == maximum and rand % 2 == 0):
                    maximum = tmp
                            
                board.board[force[i][4]][force[i][5]] = piece
                board.mouvement(force[i][2],force[i][3],[0,force[i][0],force[i][1]])
        
        else:
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if board.board[i][j] >= 2:
                        if board.board[i][j] % 2 == p % 2:
                            pos = board.possibilities(i,j)
                            if len(pos) != 0:
                                for k in range(len(pos)):
                                    board.mouvement(i,j,pos[k])
                                    
                                    tmp = self.mini(board,depth-1,p % 2 + 3)
                                    
                                    rand = random.randint(0,1)
                                    if tmp > maximum or (tmp == maximum and rand % 2 == 0):
                                        maximum = tmp
                                    
                                    board.mouvement(pos[k][1],pos[k][2],[0,i,j])
                                
        return maximum
    
    
    def mini(self,board,depth,p):
        if depth == 0 or board.win() != 0:
            return self.evaluation(board)
        
        minimum = maxSize
        tmp = 0
        
        force = board.jumpNotPlay(p)
        
        if len(force) != 0:
            for i in range(len(force)):
                piece = board.board[force[i][4]][force[i][5]]
                board.mouvement(force[i][0],force[i][1],[1,force[i][2],force[i][3],force[i][4],force[i][5]])
                
                tmp = self.maxi(board,depth - 1,p % 2 + 3)
                
                rand = random.randint(0,1)
                if tmp < minimum or (tmp == minimum and rand % 2 == 0):
                    minimum = tmp
                            
                board.board[force[i][4]][force[i][5]] = piece
                board.mouvement(force[i][2],force[i][3],[0,force[i][0],force[i][1]])
        
        else:
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if board.board[i][j] >= 2:
                        if board.board[i][j] % 2 == p % 2:
                            pos = board.possibilities(i, j)
                            if len(pos) != 0:
                                for k in range(len(pos)):
                                    board.mouvement(i, j, pos[k])
                                    
                                    tmp = self.maxi(board, depth-1, p % 2 + 3)
                                    
                                    rand = random.randint(0, 1)
                                    if tmp < minimum or (tmp == minimum and rand % 2 == 0):
                                        minimum = tmp
                                    
                                    board.mouvement(pos[k][1], pos[k][2], [0,i,j])
                                
        return minimum
    
    
    def evaluation(self,board):
        win = board.win()
        if win != 0:
            if win % 2 == self.currentPlayer % 2:
                return maxSize - 1
            else:
                return -maxSize + 1
        else:
            numberCurrentPlayer = 0
            numberOpponentPlayer = 0
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if board.board[i][j] >= 4:
                        if board.board[i][j] % 2 == self.currentPlayer % 2:
                            numberCurrentPlayer += 2 
                        else:
                            numberOpponentPlayer += 2
                    elif board.board[i][j] >= 2:
                        if board.board[i][j] % 2 == self.currentPlayer % 2:
                            numberCurrentPlayer += 1 
                        else:
                            numberOpponentPlayer += 1
            return numberCurrentPlayer - numberOpponentPlayer
    
    
    
    def IA_Play(self,depth,p):
        tempBoard = Board(self.board.size,self.board.numberPiece)
        tempBoard.board = self.board.copyBoard()
        self.currentPlayer = p
        
        maximum = -maxSize
        tmp = 0
        jump = None
        ii = 0
        ji = 0
        ifi = 0
        jfi = 0
        isa = 0
        jsa = 0
        
        force = tempBoard.jumpNotPlay(p)
        
        if len(force) != 0:
            for i in range(len(force)):
                piece = tempBoard.board[force[i][4]][force[i][5]]
                tempBoard.mouvement(force[i][0],force[i][1],[1,force[i][2],force[i][3],force[i][4],force[i][5]])
                                
                tmp = self.mini(tempBoard,depth - 1,p % 2 + 3)
                
                rand = random.randint(0,1)
                if tmp > maximum or (tmp == maximum and rand % 2 == 0):
                    maximum = tmp
                    jump = 1
                    ii = force[i][0]
                    ji = force[i][1]
                    ifi = force[i][2]
                    jfi = force[i][3]
                    isa = force[i][4]
                    jsa = force[i][5]
                            
                tempBoard.board[force[i][4]][force[i][5]] = piece
                tempBoard.mouvement(force[i][2],force[i][3],[0,force[i][0],force[i][1]])
        
        else:
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if tempBoard.board[i][j] >= 2:
                        if tempBoard.board[i][j] % 2 == p % 2:
                            pos = tempBoard.possibilities(i,j)
                            if len(pos) != 0:
                                for k in range(len(pos)):
                                    tempBoard.mouvement(i,j,pos[k])
                                    
                                    
                                    tmp = self.mini(tempBoard, depth - 1, p % 2 + 3)
                                    
                                    rand = random.randint(0,1)
                                    if tmp > maximum or (tmp == maximum and rand % 2 == 0):
                                        maximum = tmp
                                        jump = 0
                                        ii = i
                                        ji = j
                                        ifi = pos[k][1]   
                                        jfi = pos[k][2]
                                        if pos[k][0] == 1:
                                            jump = 1
                                            isa = pos[k][3]
                                            jsa = pos[k][4]
                                    
                                    tempBoard.mouvement(pos[k][1],pos[k][2],[0,i,j])
        if jump != None:
            self.board.mouvement(ii,ji,[jump,ifi,jfi,isa,jsa])


class Game:
    def __init__(self,b,wL,wH,d):
         self.board = b
         self.player1 = 2
         self.player2 = 3
         self.currentPlayer=None
         self.IA = None
         self.window = None
         self.windowLength = wL
         self.windowHeight = wH
         self.gameType = 0
         self.depth = d


    def convertXYToIJ(self,x,y):
        j = x // cellSize
        i = y // cellSize
        return [i,j]
        
    
    def home(self):
        self.window = pygame.display.set_mode((590, 767))
        pygame.display.set_caption(windowTitle + " home")
        quite = 0
        homeImage = pygame.image.load(image_homePage).convert_alpha()
        self.window.blit(homeImage,(0,0))
        pygame.display.update()
        while quite == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quite = 1
                    pygame.display.quit()
                elif(event.type == KEYDOWN and event.key == K_F1):
                    self.gameType = 1
                    quite = 1
                    pygame.display.quit()
                elif(event.type == KEYDOWN and event.key == K_F2):
                    self.gameType = 2
                    quite = 1
                    pygame.display.quit()
                elif(event.type == KEYDOWN and event.key == K_F3):
                    self.gameType = 3
                    quite = 1
                    pygame.display.quit()
    
    
    def play1_AI_AI(self):
        self.window = pygame.display.set_mode((self.windowLength, self.windowHeight))
        pygame.display.set_caption(windowTitle + " AI vs AI")
        self.board.boardGeneration()
        self.board.initializationPieces()
        self.board.show(self.window)
        iA = IA(self.board)
        quite = 1
        continu = 1
        while(continu):
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_SPACE:
                    continu = 0
                elif event.type == QUIT:
                    continu = 0
                    quite = 0
                    pygame.display.quit()
                elif event.type == KEYDOWN and event.key == K_F1:
                    newGame = False
        quite = 1
        newGame = False
        i = 0
        while quite == 1 or self.board.win() != 0 or newGame == False:
            iA.IA_Play(3,i%2 + 2)
            i += 1
            self.board.show(self.window)
            continu = 1
            while(continu):
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        continu = 0
                    elif event.type == QUIT:
                        continu = 0
                        quite = 0
                        pygame.display.quit()
                    elif event.type == KEYDOWN and event.key == K_F1:
                        newGame = False
        
    
    def play2_Human_Human(self):
        self.window = pygame.display.set_mode((self.windowLength, self.windowHeight))
        pygame.display.set_caption(windowTitle + " human vs human")
        self.board.boardGeneration()
        self.board.initializationPieces()
        self.board.show(self.window)
        currentPlayer = self.player1
        
        continu = 1
        newLoop = 0
        newGame = False
        
        pos = None
        force = None
        
        while continu == 1 or self.board.win() != 0 or newGame == False:
            self.board.show(self.window)
            newLoop = 0
            force = self.board.jumpNotPlay(currentPlayer)
            if len(force) != 0:
                self.board.showJumpedPiece(self.window,force)
                while newLoop == 0:
                    iJ = []
                    iJinitial = []
                    continuWait = 1
                    while continuWait == 1:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                continuWait = 0
                                continu = 0
                                newLoop = 1
                                pygame.display.quit()
                            elif event.type == KEYDOWN and event.key == K_F1:
                                newLoop = 1
                                continuWait = 0
                                continu = 0
                                newGame = True
                            elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                    if self.board.board[iJ[0]][iJ[1]] >= 2:
                                        if self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                            for k in range(len(force)):
                                                if iJ[0] == force[k][0] and iJ[1] == force[k][1]:
                                                    iJinitial = [iJ[0],iJ[1]]
                                                    pos = self.board.possibilities(iJinitial[0],iJinitial[1])
                                                    if len(pos) != 0:               
                                                        self.board.showPossibilitiesJumpedPiece(self.window,pos)
                                                        continuWait2 = 1
                                                        while continuWait2 == 1:
                                                            for event in pygame.event.get():
                                                                if event.type == QUIT:
                                                                    continuWait = 0
                                                                    continuWait2 = 0
                                                                    continu = 0
                                                                    newLoop = 1
                                                                    pygame.display.quit()
                                                                elif event.type == KEYDOWN and event.key == K_F1:
                                                                    newLoop = 1
                                                                    continuWait = 0
                                                                    continuWait2 = 0
                                                                    continu = 0
                                                                    newGame = True
                                                                elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                                                    iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                                                    if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                                                        if self.board.board[iJ[0]][iJ[1]] >= 2 and self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                                                            continuWait2 = 0
                                                                        else:
                                                                            for k in range(len(pos)):
                                                                                if pos[k][0] == 1:
                                                                                    if iJ[0] == pos[k][1] and iJ[1] == pos[k][2]:
                                                                                        continuWait = 0
                                                                                        continuWait2 = 0
                                                                                        newLoop = 1
                                                                                        currentPlayer = currentPlayer % 2 + 3
                                                                                        self.board.mouvement(iJinitial[0],iJinitial[1],pos[k])
                                                                                        break
                                                        self.board.show(self.window)
                                                        self.board.showJumpedPiece(self.window,force)
        
            else:
                while newLoop == 0:
                    iJ = []
                    iJinitial = []
                    continuWait = 1
                    while continuWait == 1:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                continuWait = 0
                                continu = 0
                                newLoop = 1
                                pygame.display.quit()
                            elif event.type == KEYDOWN and event.key == K_F1:
                                newLoop = 1
                                continuWait = 0
                                continu = 0
                                newGame = True
                            elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                    if self.board.board[iJ[0]][iJ[1]] >= 2:
                                        if self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                            iJinitial = [iJ[0],iJ[1]]
                                            pos = self.board.possibilities(iJinitial[0],iJinitial[1])
                                            if len(pos) != 0:               
                                                self.board.showPossibilities(self.window,pos)
                                                continuWait2 = 1
                                                while continuWait2 == 1:
                                                    for event in pygame.event.get():
                                                        if event.type == QUIT:
                                                            continuWait = 0
                                                            continuWait2 = 0
                                                            continu = 0
                                                            newLoop = 1
                                                            pygame.display.quit()
                                                        elif event.type == KEYDOWN and event.key == K_F1:
                                                            newLoop = 1
                                                            continuWait = 0
                                                            continuWait2 = 0
                                                            continu = 0
                                                            newGame = True
                                                        elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                                            iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                                            if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                                                if self.board.board[iJ[0]][iJ[1]] >= 2 and self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                                                    continuWait2 = 0
                                                                else:
                                                                    for k in range(len(pos)):
                                                                        if iJ[0] == pos[k][1] and iJ[1] == pos[k][2]:
                                                                            continuWait = 0
                                                                            continuWait2 = 0
                                                                            newLoop = 1
                                                                            currentPlayer = currentPlayer % 2 + 3
                                                                            self.board.mouvement(iJinitial[0],iJinitial[1],pos[k])
                                                                            break
                                                self.board.show(self.window)
        
        
        
        
        

                        
    def play3_AI_Human(self):
        self.window = pygame.display.set_mode((self.windowLength, self.windowHeight))
        pygame.display.set_caption(windowTitle + " human vs human")
        self.board.boardGeneration()
        self.board.initializationPieces()
        self.board.show(self.window)
        currentPlayer = self.player1
        
        iA = IA(self.board)
        
        continu = 1
        newLoop = 0
        newGame = False
        
        pos = None
        force = None
        
        while continu == 1 or self.board.win() != 0 or newGame == False:
            if currentPlayer % 2 == 0:
                self.board.show(self.window)
                newLoop = 0
                force = self.board.jumpNotPlay(currentPlayer)
                if len(force) != 0:
                    self.board.showJumpedPiece(self.window,force)
                    while newLoop == 0:
                        iJ = []
                        iJinitial = []
                        continuWait = 1
                        while continuWait == 1:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    continuWait = 0
                                    continu = 0
                                    newLoop = 1
                                    pygame.display.quit()
                                elif event.type == KEYDOWN and event.key == K_F1:
                                    newLoop = 1
                                    continuWait = 0
                                    continu = 0
                                    newGame = True
                                elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                    iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                    if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                        if self.board.board[iJ[0]][iJ[1]] >= 2:
                                            if self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                                for k in range(len(force)):
                                                    if iJ[0] == force[k][0] and iJ[1] == force[k][1]:
                                                        iJinitial = [iJ[0],iJ[1]]
                                                        pos = self.board.possibilities(iJinitial[0],iJinitial[1])
                                                        if len(pos) != 0:               
                                                            self.board.showPossibilitiesJumpedPiece(self.window,pos)
                                                            continuWait2 = 1
                                                            while continuWait2 == 1:
                                                                for event in pygame.event.get():
                                                                    if event.type == QUIT:
                                                                        continuWait = 0
                                                                        continuWait2 = 0
                                                                        continu = 0
                                                                        newLoop = 1
                                                                        pygame.display.quit()
                                                                    elif event.type == KEYDOWN and event.key == K_F1:
                                                                        newLoop = 1
                                                                        continuWait = 0
                                                                        continuWait2 = 0
                                                                        continu = 0
                                                                        newGame = True
                                                                    elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                                                        iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                                                        if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                                                            if self.board.board[iJ[0]][iJ[1]] >= 2 and self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                                                                continuWait2 = 0
                                                                            else:
                                                                                for k in range(len(pos)):
                                                                                    if pos[k][0] == 1:
                                                                                        if iJ[0] == pos[k][1] and iJ[1] == pos[k][2]:
                                                                                            continuWait = 0
                                                                                            continuWait2 = 0
                                                                                            newLoop = 1
                                                                                            currentPlayer = currentPlayer % 2 + 3
                                                                                            self.board.mouvement(iJinitial[0],iJinitial[1],pos[k])
                                                                                            break
                                                            self.board.show(self.window)
                                                            self.board.showJumpedPiece(self.window,force)
            
                else:
                    while newLoop == 0:
                        iJ = []
                        iJinitial = []
                        continuWait = 1
                        while continuWait == 1:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    continuWait = 0
                                    continu = 0
                                    newLoop = 1
                                    pygame.display.quit()
                                elif event.type == KEYDOWN and event.key == K_F1:
                                    newLoop = 1
                                    continuWait = 0
                                    continu = 0
                                    newGame = True
                                elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                    iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                    if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                        if self.board.board[iJ[0]][iJ[1]] >= 2:
                                            if self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                                iJinitial = [iJ[0],iJ[1]]
                                                pos = self.board.possibilities(iJinitial[0],iJinitial[1])
                                                if len(pos) != 0:               
                                                    self.board.showPossibilities(self.window,pos)
                                                    continuWait2 = 1
                                                    while continuWait2 == 1:
                                                        for event in pygame.event.get():
                                                            if event.type == QUIT:
                                                                continuWait = 0
                                                                continuWait2 = 0
                                                                continu = 0
                                                                newLoop = 1
                                                                pygame.display.quit()
                                                            elif event.type == KEYDOWN and event.key == K_F1:
                                                                newLoop = 1
                                                                continuWait = 0
                                                                continuWait2 = 0
                                                                continu = 0
                                                                newGame = True
                                                            elif(event.type == MOUSEBUTTONDOWN and event.button == 1):
                                                                iJ = self.convertXYToIJ(event.pos[0],event.pos[1])
                                                                if iJ[0] < self.board.size and iJ[1] < self.board.size:
                                                                    if self.board.board[iJ[0]][iJ[1]] >= 2 and self.board.board[iJ[0]][iJ[1]] % 2 == currentPlayer % 2:
                                                                        continuWait2 = 0
                                                                    else:
                                                                        for k in range(len(pos)):
                                                                            if iJ[0] == pos[k][1] and iJ[1] == pos[k][2]:
                                                                                continuWait = 0
                                                                                continuWait2 = 0
                                                                                newLoop = 1
                                                                                currentPlayer = currentPlayer % 2 + 3
                                                                                self.board.mouvement(iJinitial[0],iJinitial[1],pos[k])
                                                                                break
                                                    self.board.show(self.window)
        
            elif currentPlayer % 2 == 1:
                pygame.time.wait(500)
                iA.IA_Play(self.depth,3)
                self.board.show(self.window)
                currentPlayer = currentPlayer % 2 + 3
                
    
    
    def playGame(self):
        self.home()
        if self.gameType == 1:
            self.play1_AI_AI()
        elif self.gameType == 2:
            self.play2_Human_Human()
        elif self.gameType == 3:
            self.play3_AI_Human()


