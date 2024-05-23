# -*- coding: utf-8 -*-
"""
Created on Fri Dec 01 16:56:30 2017

@author: fourn
"""

import pygame
from pygame.locals import *

from classes import *
from constants import *

def Test1():

    pygame.init()
    
    size = 10
    numberPiece = 20
    
    windowHeight = cellSize * (size + 3) 
    windowLength = cellSize * size
    
    #Ouverture de la fenêtre Pygame
    window = pygame.display.set_mode((windowLength, windowHeight))
    
    #Titre
    pygame.display.set_caption(windowTitle)
    
    board = Board(size, numberPiece)
    
    
    game = Game(board,window,windowLength,windowHeight)
    
    game.play()
    
    pygame.display.update()
    
    
    continu = 1
    while(continu):
        for event in pygame.event.get():
           if event.type == QUIT:
                continu = 0
    
    
    
    
def Test2():
    size = 10
    numberPiece = 20
    
    board = Board(size, numberPiece)
    
    board.boardGeneration()
    board.initializationPieces()
    
    print(board.board)
    print("\n")
    
    pos = board.possibilities(3,0)
    
    print(pos)
    print("\n")
    
    board.mouvement(3,0,pos[0])
    
    print(board.board)
    print("\n")
    
    pos = board.possibilities(4,1)
    
    print(pos)
    print("\n")
    
    board.mouvement(4,1,pos[1])
    
    print(board.board)
    print("\n")
    
    pos = board.possibilities(6,3)
    
    print(pos)
    print("\n")
    
    force = board.jumpNotPlay(3)
    
    print(force)
    print("\n")
    
    board.mouvement(force[1][0],force[1][1],[1,force[1][2],force[1][3],force[1][4],force[1][5]])
    
    print(board.board)
    print("\n")
    
    board.boardGeneration()
    board.board[3][4] = 5
    
    print(board.board)
    print("\n")
    
    print(board.possibilities(3,4))
    print("\n")
    

def Test3():
    pygame.init()
    
    size = 10
    numberPiece = 20
    
    windowHeight = cellSize * (size + 3) 
    windowLength = cellSize * size
    
    #Ouverture de la fenêtre Pygame
    window = pygame.display.set_mode((windowLength, windowHeight))
    
    #Titre
    pygame.display.set_caption(windowTitle)
    
    board = Board(size, numberPiece)
    iA = IA(board)
    
    board.boardGeneration()
    board.initializationPieces()

    board.show(window)
    pygame.display.update()
    
#    continu = 1
#    while(continu):
#        for event in pygame.event.get():
#            if event.type == KEYDOWN:
#                continu = 0
    i = 0
    quite = 1
    while board.win() == False and quite == 1:
        iA.IA_Play(3,i%2 + 2)
        i += 1
        board.printBoard()
        board.show(window)
        continu = 1
        while(continu):
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    continu = 0
                elif event.type == QUIT:
                    continu = 0
                    quite = 0
    
    
    
def Test4():
    pygame.init()
    
    size = 10
    numberPiece = 20
    
    windowHeight = cellSize * (size + 3) 
    windowLength = cellSize * size
    
    #Ouverture de la fenêtre Pygame
    window = pygame.display.set_mode((windowLength, windowHeight))
    
    #Titre
    pygame.display.set_caption(windowTitle)
    
    board = Board(size, numberPiece)
    
    game = Game(board,window,windowLength,windowHeight)
    
    game.play1_AI_AI()
    
    

def Test5():
    pygame.init()
    
    size = 10
    numberPiece = 20
    
    windowHeight = cellSize * (size + 3) 
    windowLength = cellSize * size
    
    
    board = Board(size, numberPiece)
    
    game = Game(board,windowLength,windowHeight,5)
    
    game.playGame()

#Test2()
#Test3()
#Test4()
Test5()   
    
    