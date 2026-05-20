import pygame,random
W,H=500,400
pygame.init()
screen=pygame.display.set_mode((W,H))
bg = pygame.transform.scale(pygame.image.load("1.webp"), (W, H))
font=pygame.font.SysFont("Times New Roman",72)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image=pygame.Surface((30,20))
        self.image.fill(color)
        self.rect=self.image.get_rect(
            topleft=(random.randint(0,W-30),random.randint(0,H-20))
        )
    def move(self,dx,dy):
            self.rect.x=max(0,min(W-30,self.rect.x+dx))
            self.rect.y=max(0,min(H-20,self.rect.y+dy))
p1=Sprite("black")
p2=Sprite("red")
sprites=pygame.sprite.Group(p1,p2)
clock,won,run=pygame.time.Clock(),False,True
while run:
                for e in pygame.event.get():
                    if e.type==pygame.QUIT or e.type==pygame.KEYDOWN and e.key==pygame.K_x:
                        run=False
                    if not won:
                            k=pygame.key.get_pressed()
                            p1.move((k[pygame.K_RIGHT]-k[pygame.K_LEFT])*5,
                                    (k[pygame.K_DOWN]-k[pygame.K_UP])*5)
                            if p1.rect.colliderect(p2.rect):
                                sprites.remove(p2)
                    screen.blit(bg,(0,0))
                    sprites.draw(screen)
                    if won:
                                    txt=font.render("You Win!",True,"black")
                                    screen.blit(txt,((W-txt.get_width())//2,(H-txt.get_height())//2))
                    pygame.display.flip()
                    clock.tick(90)
pygame.quit()


