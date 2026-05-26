import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Space Invaders")
bg=pygame.image.load("space.jpg")
player_img=pygame.image.load("rocket.webp")
enemy_img=pygame.image.load("enemy.png")
bullet_img=pygame.image.load("bullet.jpg")
icon=pygame.image.load("ufo.webp")
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
               
