import pygame
obs1 = pygame.image.load("./Photos/obstacle_1.PNG")
obs2 = pygame.image.load("./Photos/obstacle_2.PNG")
obs3 = pygame.image.load("./Photos/obstacle_3.PNG")
obs4 = pygame.image.load("./Photos/obstacle_3.PNG")

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,ob,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ob
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0

    def contral(self,x,y):
        self.speedx += x
        self.speedy += y

    def update(self,x1,x2):
        if self.rect.x + self.speedx <= x1 and self.rect.x + self.speedx >= x2:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        else:
            self.rect.x += 0
            self.rect.y += 0

ob1 = Obstacle(obs1,1300,350)
ob2 = Obstacle(obs2,2700,280)
ob3 = Obstacle(obs3,1000,425)
ob4 = Obstacle(obs3,2450,425)
