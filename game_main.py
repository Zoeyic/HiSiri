
import pygame
import sys
from Cat import Cat
from Dog import Dog
from Goose import Goose
from startInterface import startInterface, Intro, End
from Background import Background
from DialogBox import catDia,auntDia,firemanDia,gooseDia,handkerchiefs ,timeDia, hintDia
from Fish import fs, fs2, Lives, Retry
from Obstacle import ob1,ob2,ob3,ob4
from Crazy_Goose import Crazy_Goose
from Ele import ev,ev1,ev2,ev3,ev4,ev5,ev6,ev7,ev0
from Music import Playmusic

pygame.mixer.init()

#Loading Sound Module
sound_select = pygame.mixer.Sound("./Music/sound_select.WAV")
sound_select.set_volume(1)
sound_enter = pygame.mixer.Sound("./Music/sound_enter.WAV")
sound_select.set_volume(0.1)
sound_jump = pygame.mixer.Sound("./Music/sound_jump.WAV")
sound_jump.set_volume(0.05)
sound_walk = pygame.mixer.Sound("./Music/sound_walk.WAV")
sound_walk.set_volume(0.05)
sound_dialogue = pygame.mixer.Sound("./Music/sound_dialogue.WAV")
sound_dialogue.set_volume(0.1)
sound_gain = pygame.mixer.Sound("./Music/sound_gain.WAV")
sound_gain.set_volume(0.1)
sound_wrong = pygame.mixer.Sound("./Music/sound_wrong.WAV")
sound_wrong.set_volume(0.2)
sound_fight = pygame.mixer.Sound("./Music/sound_fight.WAV")
sound_fight.set_volume(0.2)
sound_finish = pygame.mixer.Sound("./Music/sound_finish.WAV")
sound_finish.set_volume(0.1)
sound_fail = pygame.mixer.Sound("./Music/sound_fail.WAV")
sound_fail.set_volume(0.3)

#Loding Images Module
back = pygame.image.load("./Photos/background.PNG")
back2 = pygame.image.load("./Photos/background2.JPG")


def main():
    pygame.init()
    pygame.mixer.init()
    fps = pygame.time.Clock()    #Use a clock object to control the frame rate
    screen = pygame.display.set_mode((1000,750))  #Set screen size
    pygame.display.set_caption("Where is my owner?")

    play_music = Playmusic()
    button_image = play_music.play_image #Mute button
    pygame.mixer.music.play(-1) #play background music
    
    '''Initialize variables'''
    cat = Cat(450,350)
    goose1 = Goose(1200,350)
    goose2 = Goose(1800,350)
    goose3 = Goose(2400,350)
    goose4 = Crazy_Goose(3800,350)
    goose5 = Crazy_Goose(3800,350)
    goose6 = Crazy_Goose(3800,350)
    dog = Dog(1250,385)
    bg = Background(back)   #Nearby background
    bg2 = Background(back2) #Distant background
    ev.image = ev0.image    #hint tips
    st = startInterface()
    ed = End()
    rtry = Retry()    
    lf = Lives()
    inr = Intro()
    inr.rect.x = 255
    inr.rect.y = 15
    bg.rect.x = 0
    bg.rect.y = 0
    bg2.rect.x = -500
    bg2.rect.y = 0
    lf.rect.x = 0
    lf.rect.y = 0
    '''Set up a total sprite group'''
    player_list = pygame.sprite.Group()
    player_list.add(bg2,bg)
    player_list.add(ob1,ob2,ob3,ob4)
    player_list.add(cat,dog)
    player_list.add(goose1,goose2,goose3)
    player_list.add(ev,ev1,ev2,ev3,ev4,ev5,ev6,ev7)
    player_list.add(fs,fs2)
    player_list.add(lf)
    introbg = pygame.sprite.Group()
    introbg.add(inr)
    initbg = pygame.sprite.Group()
    initbg.add(st)
    enemies = pygame.sprite.Group()
    enemies.add(goose1,goose2,goose3,dog)
    eatfish = pygame.sprite.Group()
    eatfish.add(fs,fs2)
    rtrybg = pygame.sprite.Group()
    rtrybg.add(rtry)
    endbg = pygame.sprite.Group()
    endbg.add(ed)
    step = 10  #Moving distance
    tep = True #control loop in dialog code and initial interface
    retry = True #control loop in Game Over Interface
    t = 0 #play time
    end = False #control loop in ending interface
    
    def again():    #Reset
        cat.rect.x = 450
        cat.speedx = 0
        dog.rect.x = 1250
        dog.speedx = 0
        goose1.rect.x = 1200
        goose2.rect.x = 1800
        goose3.rect.x = 2400
        goose4.rect.x = 3800
        goose5.rect.x = 3800
        goose6.rect.x = 3800
        goose1.speedx = 0
        goose2.speedx = 0
        goose3.speedx = 0
        goose4.speedx = 0
        goose5.speedx = 0
        goose6.speedx = 0
        ob1.speedx = 0
        ob2.speedx = 0
        ob3.speedx = 0
        ob4.speedx = 0
        ob1.rect.x = 1300
        ob2.rect.x = 2700
        ob3.rect.x = 1000
        ob4.rect.x = 2450
        bg.rect.x = 0
        bg.speedx = 0
        bg2.rect.x = -500
        bg2.speedx = 0
        lf.rect.x = 0
        lf.speedx = 0
        ev.rect.x = 680
        ev.speedx = 0
        ev1.rect.x = 1830
        ev1.speedx = 0
        ev2.rect.x = 2430
        ev2.speedx = 0
        ev3.rect.x = 3330
        ev3.speedx = 0
        ev4.rect.x = 3730
        ev4.speedx = 0
        ev5.rect.x = 4270
        ev5.speedx = 0
        ev6.rect.x = 4630
        ev6.speedx = 0
        ev7.rect.x = 6240
        ev7.speedx = 0
        fs.rect.x = 1050
        fs.speedx = 0
        fs2.rect.x = 3050
        fs2.speedx = 0
        eatfish.add(fs,fs2)
        player_list.add(ev,ev1,ev2,ev3,ev4,ev5,ev6,ev7)
        bg.speedx = 0
        lf.image = lf.images[3]
        ev.image = ev0.image
        ev1.image = ev0.image
        ev2.image = ev0.image
        ev3.image = ev0.image
        ev4.image = ev0.image
        ev5.image = ev0.image
        ev6.image = ev0.image
        ev7.image = ev0.image
        
    while True:     #main loop
        fps.tick(60)
        screen.fill((255,255,255))
        
        while tep: #Start screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #quit game
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:    #Get keyboard events
                    if event.key == pygame.K_UP:
                        st.image = st.in_s
                        sound_select.play(0)
                        
                    if event.key == pygame.K_DOWN:
                        st.image = st.in_q
                        sound_select.play(0)

                    if event.key == pygame.K_RETURN:
                        if st.image == st.in_s:
                            sound_enter.play(0)
                            tep = False
                            intro = True
                            retry = False
                        if st.image == st.in_q:
                            pygame.quit()
                            sys.exit()
            initbg.draw(screen)
            pygame.display.update()
        
        while intro:  #Game background and control introduction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pygame.mixer.music.pause()
                        button_image = play_music.stop_image
                    if event.key == pygame.K_o:
                        pygame.mixer.music.unpause()
                        button_image = play_music.play_image
                    if event.key == pygame.K_w and inr.image == inr.images[0]:
                        sound_select.play(0)
                        inr.image = inr.images[1]
                    elif event.key == pygame.K_w and inr.image == inr.images[1]:
                        sound_select.play(0)
                        inr.image = inr.images[2]
                    elif event.key == pygame.K_w and inr.image == inr.images[2]:
                        sound_select.play(0)
                        inr.image = inr.images[3]
                    elif event.key == pygame.K_w and inr.image == inr.images[3]:
                        sound_select.play(0)
                        inr.image = inr.images[4]
                    elif event.key == pygame.K_RETURN and inr.image == inr.images[4]:
                        sound_enter.play(0)
                        intro = False
                        lf.image = lf.images[3]                               
            introbg.draw(screen)
            pygame.display.update() 
        
        '''Life System'''
        if pygame.sprite.spritecollide(cat,enemies,False):
            if cat.hurt:
                if lf.image == lf.images[3]:
                    sound_wrong.play(0)
                    lf.image = lf.images[2]
                    cat.hurt = False
                    t = pygame.time.get_ticks()
                elif lf.image == lf.images[2]:
                    sound_wrong.play(0)
                    lf.image = lf.images[1]
                    cat.hurt = False
                    t = pygame.time.get_ticks()
                elif lf.image == lf.images[1]:
                    sound_wrong.play(0)
                    lf.image = lf.images[0]
                    cat.hurt = False
                    t = pygame.time.get_ticks()

        if pygame.time.get_ticks() - t >= 1000:   #Calculate invincibility time (milliseconds)
                cat.hurt = True
         

        if lf.image == lf.images[0]:    #Death condition
            sound_walk.stop()
            sound_fail.play(0)
            retry = True
            
        if pygame.sprite.spritecollide(cat,eatfish,True): #Cat eat Fish and Restore health
            sound_gain.play(0)
            if lf.image == lf.images[1]:
                lf.image = lf.images[2]
            elif lf.image == lf.images[2]:
                lf.image = lf.images[3]

        
        while retry:    # Retry after Die
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:    #control pause music
                        pygame.mixer.music.pause()
                        button_image = play_music.stop_image
                    if event.key == pygame.K_o:   #unpause
                        pygame.mixer.music.unpause()
                        button_image = play_music.play_image
                        
                    if event.key == pygame.K_UP:  #whether retry
                        rtry.image = rtry.images[0]
                        sound_select.play(0)
                    if event.key == pygame.K_DOWN:
                            rtry.image = rtry.images[1]
                            sound_select.play(0)

                    if event.key == pygame.K_RETURN:  #confirm selection
                        if rtry.image == rtry.images[0]:
                            sound_enter.play(0)
                            retry = False
                            again()
                        if rtry.image == rtry.images[1]:
                            pygame.quit()
                            sys.exit()
            
            rtrybg.draw(screen)
            pygame.display.update()
           

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONUP:   #music button
                if play_music.click():
                    if play_music.music_play:
                        button_image = play_music.stop_image
                        play_music.music_play = False
                        pygame.mixer.music.pause()
                    else:
                        button_image = play_music.play_image
                        play_music.music_play = True
                        pygame.mixer.music.unpause()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                        pygame.mixer.music.pause()
                        button_image = play_music.stop_image
                if event.key == pygame.K_o:
                        pygame.mixer.music.unpause()
                        button_image = play_music.play_image
                        
                if event.key == pygame.K_LEFT:
                    ev.contral(step,0)
                    ev1.contral(step,0)
                    ev2.contral(step,0)
                    ev3.contral(step,0)
                    ev4.contral(step,0)
                    ev5.contral(step,0)
                    ev6.contral(step,0)
                    ev7.contral(step,0)
                    cat.contral(-step, 0)
                    fs.contral(step,0)
                    fs2.contral(step,0)
                    dog.contral(step, 0)
                    goose1.contral(step, 0)
                    goose2.contral(step, 0)
                    goose3.contral(step, 0)
                    goose4.contral(step, 0)
                    goose5.contral(step, 0)
                    goose6.contral(step, 0)
                    bg.contral(step,0)
                    bg2.contral(1.2 * step,0)
                    ob1.contral(step,0)
                    ob2.contral(step,0)
                    ob3.contral(step,0)
                    ob4.contral(step,0)
                    sound_walk.play(-1)
                if event.key == pygame.K_RIGHT:
                    ev.contral(-step,0)
                    ev1.contral(-step,0)
                    ev2.contral(-step,0)
                    ev3.contral(-step,0)
                    ev4.contral(-step,0)
                    ev5.contral(-step,0)
                    ev6.contral(-step,0)
                    ev7.contral(-step,0)
                    cat.contral(step, 0)
                    fs.contral(-step,0)
                    fs2.contral(-step,0)
                    dog.contral(-step, 0)
                    goose1.contral(-step, 0)
                    goose2.contral(-step, 0)
                    goose3.contral(-step, 0)
                    goose4.contral(-step, 0)
                    goose5.contral(-step, 0)
                    goose6.contral(-step, 0)
                    bg.contral(-step,0)
                    bg2.contral(-1.2 * step, 0)
                    ob1.contral(-step,0)
                    ob2.contral(-step,0)
                    ob3.contral(-step,0)
                    ob4.contral(-step,0)
                    sound_walk.play(-1)
                if event.key == pygame.K_SPACE:
                    sound_jump.play(0)
                if event.key == pygame.K_ESCAPE: #pause game
                    tep = True
                    pygame.mixer.music.pause()
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_TAB: #continue
                                    sound_dialogue.play(0)
                                    pygame.mixer.music.unpause()
                                    tep = False
                            screen.blit(hintDia.image, (0, 0))
                            screen.blit(hintDia.drawDia("Press TAB"), (300, 300))
                            screen.blit(hintDia.drawDia("to continue"), (300, 340))
                            player_list.remove(ev)
                            pygame.display.update()
                    
                if event.key == pygame.K_RETURN and bg.rect.x >= -285 and bg.rect.x <= -176:   #Tips board
                    tep = True
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_dialogue.play(0)
                                    tep = False
                            screen.blit(hintDia.image, (0, 0))
                            screen.blit(hintDia.drawDia("Beware of"), (300, 300))
                            screen.blit(hintDia.drawDia("dogs and geese"), (300, 340))
                            player_list.remove(ev)
                            pygame.display.update()

                if event.key == pygame.K_RETURN and bg.rect.x >= -1435 and bg.rect.x <= -1305:   #The Bakery
                    tep = True
                    num = 0
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_dialogue.play(0)
                                    num += 1
                                    if num == 3:
                                        tep = False
                            if num == 0:
                                screen.blit(catDia.image, (0, 0))
                                screen.blit(catDia.drawDia("Hi, do you see my owner?"), (350, 550))
                            if num == 1:
                                screen.blit(auntDia.image, (0,0))
                                screen.blit(auntDia.drawDia("She seems to go to the"), (300, 550))
                                screen.blit(auntDia.drawDia("riverside to buy fishes."), (300, 590))
                            if num == 2:
                                screen.blit(catDia.image, (0, 0))
                                screen.blit(catDia.drawDia("Thank you dear."), (350, 550))
                            player_list.remove(ev1)
                            pygame.display.update()

                if event.key == pygame.K_RETURN and bg.rect.x >= -2110 and bg.rect.x <= -1840:   #Fire Department
                    tep = True
                    num = 0
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_dialogue.play(0)
                                    num += 1
                                    if num == 3:
                                        tep = False
                            if num == 0:
                                screen.blit(catDia.image, (0, 0))
                                screen.blit(catDia.drawDia("Could you tell me how to"), (350, 550))
                                screen.blit(catDia.drawDia("go to the riverside?"), (350, 590))
                            if num == 1:
                                screen.blit(firemanDia.image,(0,0))
                                screen.blit(firemanDia.drawDia("Oh cute kitty, just go"),(350,550))
                                screen.blit(firemanDia.drawDia("straight on and take care"),(350,590))
                                screen.blit(firemanDia.drawDia("of the dogs and geese."), (350, 630))
                            if num == 2:
                                screen.blit(catDia.image, (0, 0))
                                screen.blit(catDia.drawDia("Thank you!"), (350, 550))
                            player_list.remove(ev2)
                            pygame.display.update()

                if event.key == pygame.K_RETURN and bg.rect.x >= -2995 and bg.rect.x <= -2847:   #Café
                    tep = True
                    num = 0
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_dialogue.play(0)
                                    num += 1
                                    if num == 2:
                                        tep = False
                            if num == 0:
                                screen.blit(handkerchiefs,(0,0))
                            if num == 1:
                                screen.blit(catDia.image, (0, 0))
                                screen.blit(catDia.drawDia("It's my owner's handkerchief."), (350, 550))
                                screen.blit(catDia.drawDia("She's nearby!"), (350, 590))
                            player_list.remove(ev3)
                            pygame.display.update()

                if event.key == pygame.K_RETURN and bg.rect.x >= -3361 and bg.rect.x <= -3238:   #basket
                    tep = True
                    num = 0
                    sound_fight.play(0)
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_fight.play(0)
                                    sound_dialogue.play(0)
                                    num += 1
                                    if num == 1:
                                        tep = False
                            if num == 0:
                                screen.blit(gooseDia.image, (0,0))
                                screen.blit(gooseDia.drawDia("HOW DARE YOU!"), (350, 550))
                                screen.blit(gooseDia.drawDia("GO DIE!"), (350, 590))
                                
                                enemies.add(goose4, goose5, goose6)
                                goose1.kill()
                                goose2.kill()
                                goose3.kill()
                            player_list.remove(ev4)
                            pygame.display.update()

                if event.key == pygame.K_RETURN and bg.rect.x >= -3906 and bg.rect.x <= -3708:   #church
                    tep = True
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_dialogue.play(0)
                                    tep = False
                            screen.blit(catDia.image,(0,0))
                            screen.blit(hintDia.drawDia("The door is locked,"), (350, 550))
                            screen.blit(catDia.drawDia("there is nothing to find."),(350,590))
                            screen.blit(hintDia.drawDia("Where is my owner..."), (350, 630))
                            player_list.remove(ev5)
                            pygame.display.update()

                if event.key == pygame.K_RETURN and bg.rect.x >= -4206 and bg.rect.x <= -4008:   #water warning
                    tep = True
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_dialogue.play(0)
                                    tep = False
                            screen.blit(hintDia.image,(0,0))
                            screen.blit(hintDia.drawDia("You would better not"),(300,300))
                            screen.blit(hintDia.drawDia("to touch the water"), (300, 340))
                            player_list.remove(ev6)
                            
                            pygame.display.update()
                            
                if event.key == pygame.K_RETURN and bg.rect.x >= -5816 and bg.rect.x <= -5616: # Last "!"
                    tep = True
                    sound_dialogue.play(0)
                    while tep:
                        player_list.draw(screen)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    sound_dialogue.play(0)
                                    tep = False
                            screen.blit(catDia.image,(0,0))
                            screen.blit(catDia.drawDia("Meow!!Owner!!!"),(350,510))
                            screen.blit(catDia.drawDia("Here you are!!"), (350, 550))
                            screen.blit(catDia.drawDia("I miss you so much!!"),(350,590))
                            screen.blit(catDia.drawDia("Never be lost again!"), (350, 630))
                            player_list.remove(ev7)
                            
                            pygame.display.update()

            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT:
                    sound_walk.stop()
                    ev.contral(-step,0)
                    ev1.contral(-step,0)
                    ev2.contral(-step,0)
                    ev3.contral(-step,0)
                    ev4.contral(-step,0)
                    ev5.contral(-step,0)
                    ev6.contral(-step,0)
                    ev7.contral(-step,0)
                    cat.contral(step, 0)
                    fs.contral(-step,0)
                    fs2.contral(-step,0)
                    dog.contral(-step, 0)
                    goose1.contral(-step, 0)
                    goose2.contral(-step, 0)
                    goose3.contral(-step, 0)
                    goose4.contral(-step, 0)
                    goose5.contral(-step, 0)
                    goose6.contral(-step, 0)
                    bg.contral(-step, 0)
                    bg2.contral(-1.2 * step, 0)
                    ob1.contral(-step,0)
                    ob2.contral(-step,0)
                    ob3.contral(-step,0)
                    ob4.contral(-step,0)
                    cat.image = pygame.transform.flip(cat.standImage, True, False)
                if event.key == pygame.K_RIGHT:
                    sound_walk.stop()
                    ev.contral(step,0)
                    ev1.contral(step,0)
                    ev2.contral(step,0)
                    ev3.contral(step,0)
                    ev4.contral(step,0)
                    ev5.contral(step,0)
                    ev6.contral(step,0)
                    ev7.contral(step,0)
                    cat.contral(-step, 0)
                    fs.contral(step,0)
                    fs2.contral(step,0)
                    cat.image = cat.standImage
                    dog.contral(step, 0)
                    goose1.contral(step, 0)
                    goose2.contral(step, 0)
                    goose3.contral(step, 0)
                    goose4.contral(step, 0)
                    goose5.contral(step, 0)
                    goose6.contral(step, 0)
                    bg.contral(step,0)
                    bg2.contral(1.2 * step, 0)
                    ob1.contral(step,0)
                    ob2.contral(step,0)
                    ob3.contral(step,0)
                    ob4.contral(step,0)


        if bg.rect.x <= -6000:
            end = True
            endtime = pygame.time.get_ticks() // 1000
            sound_walk.stop()
            sound_finish.play(0)
        while end:  # happy ending interface
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        ed.image = ed.quit
                        sound_select.play(0)

                    if event.key == pygame.K_LEFT:
                        ed.image = ed.retry
                        sound_select.play(0)

                    if event.key == pygame.K_RETURN:
                        if ed.image == ed.retry:
                            sound_enter.play(0)
                            end = False
                            again()
                        if ed.image == ed.quit:
                            pygame.quit()
                            sys.exit()
            endbg.draw(screen)
            screen.blit(timeDia.drawDia(str(endtime) + "seconds"), (180, 280))
            pygame.display.update()

        '''Refresh function for each sprite'''
        ev.update(680,-7000)
        ev1.update(1830,-7000)
        ev2.update(2430,-7000)
        ev3.update(3330,-7000)
        ev4.update(3730,-7000)
        ev5.update(4270,-7000)
        ev6.update(4630,-7000)
        ev7.update(6240,-7000)
        cat.update(bg,lf)
        lf.update(0,-7000)
        fs.update(1050,-7000)
        fs2.update(3050,-7000)
        bg.update(0,-7000)
        bg2.update(-500,-8500)
        ob1.update(1000, -7000)
        ob2.update(2700, -7000)
        ob3.update(1000, -7000)
        ob4.update(2450, -7000)
        dog.update(1250,-7000)
        goose1.update(1200,-7000)
        goose2.update(1800,-7000)
        goose3.update(2400,-7000)
        goose4.update(3800,-7000)
        goose5.update(3800,-7000)
        goose6.update(3800,-7000)
        player_list.draw(screen)
        eatfish.draw(screen)
        enemies.draw(screen)
        screen.blit(button_image, (850, 650))
        pygame.display.update()

main()
