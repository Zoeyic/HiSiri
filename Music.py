import pygame

class Playmusic():
    music_play = True

    def __init__(self):
        self.play_image = pygame.image.load("./Photos/mute.PNG")
        self.stop_image = pygame.image.load("./Photos/unmute.PNG")
        self.sp_music = pygame.mixer.music.load("./Music/sp_music.OGG")
        
    def click(self):    #Detect mouse trigger music event
        mouse = pygame.mouse.get_pos()
        width, height = self.play_image.get_size()
        if 850 < mouse[0] < 850 + width and 650 < mouse[1] < 650 + height:
            return mouse
