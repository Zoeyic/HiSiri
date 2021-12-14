import pygame

goose1 = pygame.image.load("./Photos/goose_run1.PNG")
goose2 = pygame.image.load("./Photos/goose_run2.PNG")
goose3 = pygame.image.load("./Photos/goose_run3.PNG")

class Goose(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [goose1, goose2, goose3]
        self.image = goose2
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.speedx = 0
        self.speedy = 0
        self.counter = 0  # set counter

    def contral(self, x, y):
        self.speedx += x
        self.speedy += y

    def update(self,x1,x2):

        distance = 100
        enemy_speed = 5
        if self.rect.x + self.speedx <= x1 and self.rect.x + self.speedx >= x2:
            if self.counter >= 0 and self.counter <= distance:
                self.rect.x += enemy_speed + self.speedx
                self.frame += 1
                if self.frame > 3 * 2:
                    self.frame = 0
                self.image = pygame.transform.flip(self.images[self.frame // 3], True, False)
            elif self.counter >= distance and self.counter <= distance * 2:
                self.rect.x = self.rect.x - enemy_speed + self.speedx
                self.frame += 1
                if self.frame > 3 * 2:
                    self.frame = 0
                self.image = self.images[self.frame // 3]
            else:
                self.counter = 0  # Reset the counter back to 0
        else:
            self.rect.x += 0
            self.rect.y += 0


        self.counter += 1
