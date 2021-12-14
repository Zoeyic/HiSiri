import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self,bg):
        pygame.sprite.Sprite.__init__(self)
        self.image = bg
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0

    def contral(self,x,y):
        self.speedx += x
        self.speedy += y

    def update(self,x1,x2):
        if self.rect.x + self.speedx <= x1 and self.rect.x+ self.speedx >= x2:  #Judging the range of movement
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        else:
            self.rect.x += 0
            self.rect.y += 0