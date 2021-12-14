import pygame

dog1 = pygame.image.load("./Photos/dog_run1.PNG")
dog2 = pygame.image.load("./Photos/dog_run2.PNG")
dog3 = pygame.image.load("./Photos/dog_run3.PNG")

class Dog(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [dog1, dog2, dog3]
        self.standImage = dog2
        self.image = self.standImage
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.counter = 0

    def contral(self, x, y):
        self.speedx += x
        self.speedy += y

    def update(self,x1,x2):

        distance = 500
        enemy_speed = 3

        if self.rect.x + self.speedx <= x1 and self.rect.x + self.speedx >= x2:
            if self.counter >= 0 and self.counter <= distance:
                self.rect.x += enemy_speed + self.speedx
                self.frame += 1
                if self.frame > 3 * 2:
                    self.frame = 0
                self.image = self.images[self.frame // 3]
            elif self.counter >= distance and self.counter <= distance * 2:
                self.rect.x = self.rect.x - enemy_speed + self.speedx
                self.frame += 1
                if self.frame > 3 * 2:
                    self.frame = 0
                self.image = pygame.transform.flip(self.images[self.frame // 3], True, False)
            else:
                self.counter = 0  # Reset the counter back to 0

        else:
            self.rect.x += 0
            self.rect.y += 0

        self.counter += 1
        