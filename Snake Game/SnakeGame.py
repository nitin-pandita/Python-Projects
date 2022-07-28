from email import message
from tkinter import LEFT
import pygame
import os
import pygame
import random
import sys
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

#we will declear global constant definitions

speed = 0.30
SNAKE_SIZE = 9 #enum
APPLE_SIZE= 9
SEPREATION = 10
SCREEN_HEIGH = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"LEFT":1,"RIGHT":2,"UP":3,"DOWN":4}


screen = pygame.display.set_mode((SCREEN_HEIGH,SCREEN_WIDTH),pygame.HWSURFACE)

#Hw surface which stand for hardware surface refers using memory on the video card for storing 

#Resources

score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score: ",1,pygame.color("green"))
background_color = pygame.Color(0,0,0) #black background
black = pygame.Color(0,0,0)


#for clock
gameclock = pygame.time.Clock()

#defining keys

def getkey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_LEFT:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_LEFT:
                return KEY["RIGHT"]
            
            #for exit
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            elif event.key == pygame.K_y:
                return "yes"
            elif event.key == pygame.K_n:
                return "no"
            
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame():
    message = game_over_font.render("Game over",1,pygame.color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N",1,pygame.Color("green"))

    screen.blit(message,(360,240))