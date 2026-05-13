import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
font=pygame.font.Font(None,36)
done=False
while not done:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,60))
            text=font.render("Hello Pygame!",True,(0,0,0))
    screen.blit(text,(120,40))
    pygame.display.flip()
    pygame.quit()