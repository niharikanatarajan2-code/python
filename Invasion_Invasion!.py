import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Invasion Invasion!")
bg=pygame.image.load("space-cartoon-background-hb2q1.jpg")
player_img=pygame.image.load("rocket2.jpg")
enemy_img=pygame.image.load("enemy2.png")
bullet_img=pygame.image.load("bullet2.png")
icon=pygame.image.load("ufo2.jpg")
pygame.display.set_icon(icon)
playerX,playerY=370,380
player_speed=0
enemies=[]
for i in range(6):
    enemies.append([
        random.randint(0,736),
        random.randint(50,150),
        4
        ])
    bulletX,bulletY=0,380
    bullet_state="ready"
    score=0
    font=pygame.font.Font("freesansbold.ttf",32)