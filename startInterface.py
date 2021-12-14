import pygame


init_s = pygame.image.load("./Photos/init_start.JPG")
init_q = pygame.image.load("./Photos/init_quit.JPG")

intro1 = pygame.image.load("./Photos/intro_start1.PNG")
intro2 = pygame.image.load("./Photos/intro_start2.PNG")
intro3 = pygame.image.load("./Photos/intro_start3.PNG")
intro4 = pygame.image.load("./Photos/intro_start4.PNG")
intro5 = pygame.image.load("./Photos/intro_press.PNG")

end1 = pygame.image.load("./Photos/end_quit.JPG")
end2 = pygame.image.load("./Photos/end_retry.JPG")


class startInterface(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = init_s
        self.in_s = init_s
        self.in_q = init_q
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0

class Intro(pygame.sprite.Sprite):  #Beginning background and input introduction
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [intro1,intro2,intro3,intro4,intro5]
        self.image = intro1
        self.rect = self.image.get_rect()


class End(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = end1
        self.quit = end1
        self.retry = end2
        self.rect = self.image.get_rect()