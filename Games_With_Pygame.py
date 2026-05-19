import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
player=pygame.Rect(50,50,50,50)
enemy=pygame.Rect(300,200,50,50)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            keys=pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.x-=5
            if keys[pygame.K_RIGHT]:
                player.y+=5
                screen.fill((0,0,0))
                pygame.draw.rect(screen,(255,0,0),player)
                pygame.draw.rect(screen,(0,255,0),enemy)
                pygame.display.update()
                pygame.quit()
   