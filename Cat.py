import pygame

cat1 = pygame.image.load("./Photos/cat_run1.PNG")
cat2 = pygame.image.load("./Photos/cat_stand.PNG")
cat3 = pygame.image.load("./Photos/cat_run2.PNG")
cat_h1 = pygame.image.load("./Photos/cat_hurt1.PNG")
cat_h2 = pygame.image.load("./Photos/cat_hurt_stand.PNG")
cat_h3 = pygame.image.load("./Photos/cat_hurt2.PNG")


class Cat(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [cat1, cat2, cat3]
        self.hurt_images = [cat1, cat_h2, cat3, cat_h1, cat2, cat_h3]
        self.standImage = cat2
        self.image = self.standImage
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.vel_y = 0
        self.jumped = False
        self.hurt = True     #Judge whether it is invincible

    def contral(self, x, y):
        self.speedx += x
        self.speedy += y

    def update(self,bg,lf):
        x_move = 0
        y_move = 0
        if self.speedx < 0:
            self.frame += 1
            if self.hurt:
                if self.frame > 3 * 2:
                    self.frame = 0
                self.image = pygame.transform.flip(self.images[self.frame // 3], True, False)
            else:
                if self.frame > 6 * 2:
                    self.frame = 0
                self.image = pygame.transform.flip(self.hurt_images[self.frame // 6], True, False)

        if self.speedx > 0:
            self.frame += 1
            if self.hurt:
                if self.frame > 3 * 2:
                    self.frame = 0
                self.image = self.images[self.frame // 3]
            else:
                if self.frame > 6 * 2:
                    self.frame = 0
                self.image = self.hurt_images[self.frame // 6]
        '''JUMP'''
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped is False:
            if (bg.rect.x > -750 and bg.rect.x < -500) or \
               (bg.rect.x > -2200 and bg.rect.x < -1950):
                self.vel_y = -25
            else:
                self.vel_y = -18
            self.jumped = True
        # Prevent continuous jumping
        if self.rect.bottom >= 450:
            self.jumped = False

        # Added character gravity (falling naturally after jumping)
        self.vel_y += 1.2
        if self.vel_y > 10:
            self.vel_y = 10
        y_move += self.vel_y
        # Fall on the ground and stop
        if self.rect.bottom > 450:
            self.rect.bottom = 450

        self.rect.x += x_move
        self.rect.y += y_move
        
        '''River crossing system'''
        if (bg.rect.x > -4350 and bg.rect.x < -4180 and self.rect.bottom == 460) or\
           (bg.rect.x > -4650 and bg.rect.x < -4460 and self.rect.bottom == 460) or\
           (bg.rect.x > -5000 and bg.rect.x < -4850 and self.rect.bottom == 460) or\
           (bg.rect.x > -5500 and bg.rect.x < -5280 and self.rect.bottom == 460) or\
           (bg.rect.x > -5700 and bg.rect.x < -5580 and self.rect.bottom == 460) or\
           (bg.rect.x > -5880 and bg.rect.x < -5830 and self.rect.bottom == 460):
            lf.image = lf.images[0]


