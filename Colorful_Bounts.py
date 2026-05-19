import pygame
import random
pygame.init()
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Moving Sprite")
clock=pygame.time.Clock()
bg_colors=["blue","light blue","dark blue"]
sprite_colors=["yellow","magenta","orange","white"]
bg_color="blue"
sprite=pygame.Rect(100,100,30,20)
sprite_color="white"
dx=4
dy=4
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    sprite.x +=dx
    sprite.y +=dy
    if sprite.left<0 or sprite.right>=500:
                dx=-dx
                sprite_color=random.choice(sprite_colors)
                bg_color=random.choice(bg_colors)
    if sprite.top<=0 or sprite.bottom>=400:
                dy=-dy
                sprite_color=random.choice(sprite_colors)
                bg_color=random.choice(bg_colors)                           
    screen.fill(bg_color)
    pygame.draw.rect(screen,sprite_color,sprite)
    pygame.display.update()
    clock.tick(60)
pygame.quit()