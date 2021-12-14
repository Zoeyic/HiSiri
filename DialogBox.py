import pygame
pygame.display.init()

screen = pygame.display.set_mode((1000,750))
screen.fill((255,255,255))

dia_cat = pygame.image.load("./Photos/dia_cat.PNG")
dia_aunt = pygame.image.load("./Photos/dia_aunt.PNG")
dia_fireman = pygame.image.load("./Photos/dia_fireman.PNG")
dia_goose = pygame.image.load("./Photos/dia_goose.PNG")
handkerchiefs = pygame.image.load("./Photos/Handkerchiefs.PNG")
dia_hint = pygame.image.load("./Photos/dia_hint.PNG")

class DialogBox():
    def __init__(self,image = 0):
        self.image = image

    def drawDia(self,content):
        pygame.font.init()
        font = pygame.font.Font("./Font/Arial Black.ttf",38)
        text_sf = font.render(content,True,(90,105,127))
        return text_sf


catDia = DialogBox(dia_cat)
auntDia = DialogBox(dia_aunt)
firemanDia = DialogBox(dia_fireman)
gooseDia = DialogBox(dia_goose)
hintDia = DialogBox(dia_hint)
timeDia = DialogBox()