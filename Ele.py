import pygame

ele = pygame.image.load("./Photos/ele.PNG")
bige = pygame.image.load("./Photos/bigevent.PNG")


class Ele(pygame.sprite.Sprite):   #Eat fish
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)       
        self.big = bige
        self.image = ele
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0

    def contral(self,x,y):
        self.speedx += x
        self.speedy += y

    def update(self,x1,x2):
        if self.rect.x + self.speedx <= x1 and self.rect.x+ self.speedx >= x2:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
            if self.rect.x >= 300 and self.rect.x <= 500:
                self.image = self.big
            else:
                self.image = ele
        
        else:
            self.rect.x += 0
            self.rect.y += 0
            
ev0 = Ele()
ev = Ele()
ev1 = Ele()
ev2 = Ele()
ev3 = Ele()
ev4 = Ele()
ev5 = Ele()
ev6 = Ele()
ev7 = Ele()
ev0.image = ele
ev.rect.x = 680
ev.rect.y = 250
ev1.rect.x = 1830
ev1.rect.y = 250 
ev2.rect.x = 2430
ev2.rect.y = 250
ev3.rect.x = 3330
ev3.rect.y = 250  
ev4.rect.x = 3730
ev4.rect.y = 250
ev5.rect.x = 4270
ev5.rect.y = 250        
ev6.rect.x = 4630
ev6.rect.y = 350
ev7.rect.x = 6240
ev7.rect.y = 370             