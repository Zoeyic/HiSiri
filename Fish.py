import pygame

fish = pygame.image.load("./Photos/fish.PNG")
fish0 = pygame.image.load("./Photos/fish0.PNG")
die1 = pygame.image.load("./Photos/die1.JPG")
die2 = pygame.image.load("./Photos/die2.JPG")
fish1 = pygame.image.load("./Photos/fish1.PNG")
fish2 = pygame.image.load("./Photos/fish2.PNG")
fish3 = pygame.image.load("./Photos/fish3.PNG")

class Fish(pygame.sprite.Sprite):   #Eat fish
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)       
        self.image = fish
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
        else:
            self.rect.x += 0
            self.rect.y += 0
    
fs = Fish()
fs2 = Fish()
fs.image = fish0
fs.rect.x = 1050
fs.rect.y = 110
fs2.rect.x = 3050
fs2.rect.y = 300
fs.update(1050, -4000)
fs2.update(3050, -4000)
            
class Lives(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)       
        self.images = [die1,fish1,fish2,fish3]
        self.image = self.images[3]
        self.rect = self.image.get_rect()

class Retry(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)       
        self.images = [die1,die2]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        
    