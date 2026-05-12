import pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg=pygame.transform.scale(
    pygame.image.load("background.png"),(WIDTH, HEIGHT)
)
penguin=pygame.transform.scale(
    pygame.image.load("penguin.png"),(200, 200)
)
font=pygame.font.Font(None, 36)
text=font.render("Hello World",True,"black")
running=True
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(bg,(0,0))
    screen.blit(penguin,(150,120))
    screen.blit(text,(170,350))
    pygame.display.update()
    clock.tick(30)