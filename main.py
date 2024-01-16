import pygame
from random import *
from math import *
pygame.init()

pygame.display.set_caption("Fisc Simulator")
screen = pygame.display.set_mode((1170, 780))
background = [pygame.image.load('assets\Textures\city_background1.png'), pygame.image.load('assets\Textures\city_background2.png'), pygame.image.load('assets\Textures\city_background3.png'), pygame.image.load('assets\Textures\city_background4.png'), pygame.image.load('assets\Textures\city_background5.png'), pygame.image.load('assets\Textures\city_background6.png')]
fight_background = [pygame.image.load('assets\Textures\Fight_background1.png'), pygame.image.load('assets\Textures\Fight_background2.png'), pygame.image.load('assets\Textures\Fight_background3.png')]
choice_yes = pygame.image.load('assets\Textures\choice_yes.png')
choice_no = pygame.image.load('assets\Textures\choice_no.png')
beforeFight_background = pygame.image.load('assets\Textures\BeforeFight_background.png')
numbers = [pygame.image.load('assets\Textures\Chif_0.png'), pygame.image.load('assets\Textures\Chif_1.png'), pygame.image.load('assets\Textures\Chif_2.png'), pygame.image.load('assets\Textures\Chif_3.png'), pygame.image.load('assets\Textures\Chif_4.png'), pygame.image.load('assets\Textures\Chif_5.png'), pygame.image.load('assets\Textures\Chif_6.png'), pygame.image.load('assets\Textures\Chif_7.png'), pygame.image.load('assets\Textures\Chif_8.png'), pygame.image.load('assets\Textures\Chif_9.png')]
monster_sprite = [pygame.image.load('assets\Textures\monster_creditor.png'), pygame.image.load('assets\Textures\monster_deputy.png'), pygame.image.load('assets\Textures\monster_warMinister.png'), pygame.image.load('assets\Textures\monster_president.png')]
monster_name = [pygame.image.load('assets\Textures\monsterName_creditor.png'), pygame.image.load('assets\Textures\monsterName_deputy.png'), pygame.image.load('assets\Textures\monsterName_warMinister.png'), pygame.image.load('assets\Textures\monsterName_president.png')]
self_sprite = pygame.image.load('assets\Textures\self_sprite.png')
self_name = pygame.image.load('assets\Textures\self_name.png')
stats_background = pygame.image.load('assets\Textures\stats_background.png')
win_background = pygame.image.load('assets\Textures\win_background.png')
lose_background = pygame.image.load('assets\Textures\lose_background.png')
caractere_slash = pygame.image.load('assets\Textures\caractere_slash.png')
end_background =pygame.image.load('assets\Textures\end_background.png')
end_backgroundAlternate = pygame.image.load('assets\Textures\end_backgroundAlternate.png')
caractere_plus =pygame.image.load('assets\Textures\caractere_plus.png')
caractere_minus =pygame.image.load('assets\Textures\caractere_minus.png')
caractere_dollar = pygame.image.load('assets\Textures\caractere_dollar.png')
monney_background =pygame.image.load('assets\Textures\monney_background.png')
text_times = pygame.image.load('assets\Textures\Text_times.png')
choice_atk = [pygame.image.load('assets\Textures\choice_atk1.png'), pygame.image.load('assets\Textures\choice_atk2.png'), pygame.image.load('assets\Textures\choice_atk3.png'), pygame.image.load('assets\Textures\choice_atk4.png')]
frame_atk = [pygame.image.load('assets\Textures\Frame_atk01.png'), pygame.image.load('assets\Textures\Frame_atk02.png'), pygame.image.load('assets\Textures\Frame_atk03.png'), pygame.image.load('assets\Textures\Frame_atk04.png'), pygame.image.load('assets\Textures\Frame_atk05.png'), pygame.image.load('assets\Textures\Frame_atk06.png'), pygame.image.load('assets\Textures\Frame_atk07.png'), pygame.image.load('assets\Textures\Frame_atk08.png'), pygame.image.load('assets\Textures\Frame_atk09.png'), pygame.image.load('assets\Textures\Frame_atk10.png'), pygame.image.load('assets\Textures\Frame_atk11.png'), pygame.image.load('assets\Textures\Frame_atk12.png'), pygame.image.load('assets\Textures\Frame_atk13.png'), pygame.image.load('assets\Textures\Frame_atk14.png'), pygame.image.load('assets\Textures\Frame_atk15.png'), pygame.image.load('assets\Textures\Frame_atk16.png'), pygame.image.load('assets\Textures\Frame_atk17.png'), pygame.image.load('assets\Textures\Frame_atk18.png'), pygame.image.load('assets\Textures\Frame_atk19.png'), pygame.image.load('assets\Textures\Frame_atk20.png'), pygame.image.load('assets\Textures\Frame_atk21.png'), pygame.image.load('assets\Textures\Frame_atk22.png'), pygame.image.load('assets\Textures\Frame_atk23.png'), pygame.image.load('assets\Textures\Frame_atk24.png'), pygame.image.load('assets\Textures\Frame_atk25.png'), pygame.image.load('assets\Textures\Frame_atk26.png'), pygame.image.load('assets\Textures\Frame_atk27.png'), pygame.image.load('assets\Textures\Frame_atk28.png'), pygame.image.load('assets\Textures\Frame_atk29.png'), pygame.image.load('assets\Textures\Frame_atk30.png'), pygame.image.load('assets\Textures\Frame_atk31.png'), pygame.image.load('assets\Textures\Frame_atk32.png'), pygame.image.load('assets\Textures\Frame_atk33.png'), pygame.image.load('assets\Textures\Frame_atk34.png'), pygame.image.load('assets\Textures\Frame_atk35.png'), pygame.image.load('assets\Textures\Frame_atk36.png'), pygame.image.load('assets\Textures\Frame_atk37.png'), pygame.image.load('assets\Textures\Frame_atk38.png'), pygame.image.load('assets\Textures\Frame_atk39.png'), pygame.image.load('assets\Textures\Frame_atk40.png'), pygame.image.load('assets\Textures\Frame_atk41.png'), pygame.image.load('assets\Textures\Frame_atk42.png'), pygame.image.load('assets\Textures\Frame_atk43.png'), pygame.image.load('assets\Textures\Frame_atk44.png'), pygame.image.load('assets\Textures\Frame_atk45.png'), pygame.image.load('assets\Textures\Frame_atk46.png'), pygame.image.load('assets\Textures\Frame_atk47.png'), pygame.image.load('assets\Textures\Frame_atk48.png'), pygame.image.load('assets\Textures\Frame_atk49.png'), pygame.image.load('assets\Textures\Frame_atk50.png'), pygame.image.load('assets\Textures\Frame_atk51.png'), pygame.image.load('assets\Textures\Frame_atk52.png'), pygame.image.load('assets\Textures\Frame_atk53.png'), pygame.image.load('assets\Textures\Frame_atk54.png'), pygame.image.load('assets\Textures\Frame_atk55.png'), pygame.image.load('assets\Textures\Frame_atk56.png'), pygame.image.load('assets\Textures\Frame_atk57.png'), pygame.image.load('assets\Textures\Frame_atk58.png'), pygame.image.load('assets\Textures\Frame_atk59.png'), pygame.image.load('assets\Textures\Frame_atk60.png'), pygame.image.load('assets\Textures\Frame_atk61.png'), pygame.image.load('assets\Textures\Frame_atk62.png'), pygame.image.load('assets\Textures\Frame_atk63.png'), pygame.image.load('assets\Textures\Frame_atk64.png'), pygame.image.load('assets\Textures\Frame_atk65.png'), pygame.image.load('assets\Textures\Frame_atk66.png'), pygame.image.load('assets\Textures\Frame_atk67.png'), pygame.image.load('assets\Textures\Frame_atk68.png'), pygame.image.load('assets\Textures\Frame_atk69.png'), pygame.image.load('assets\Textures\Frame_atk70.png'), pygame.image.load('assets\Textures\Frame_atk71.png'), pygame.image.load('assets\Textures\Frame_atk72.png'), pygame.image.load('assets\Textures\Frame_atk73.png'), pygame.image.load('assets\Textures\Frame_atk74.png')]
frame_flag = [pygame.image.load('assets\Textures\Frame_flag0.png'), pygame.image.load('assets\Textures\Frame_flag1.png'), pygame.image.load('assets\Textures\Frame_flag2.png'), pygame.image.load('assets\Textures\Frame_flag3.png'), pygame.image.load('assets\Textures\Frame_flag4.png'), pygame.image.load('assets\Textures\Frame_flag5.png'), pygame.image.load('assets\Textures\Frame_flag6.png'), pygame.image.load('assets\Textures\Frame_flag7.png'), pygame.image.load('assets\Textures\Frame_flag8.png'), pygame.image.load('assets\Textures\Frame_flag9.png')]
frame_gun = [pygame.image.load('assets\Textures\Frame_gun1.png'), pygame.image.load('assets\Textures\Frame_gun2.png')]
frame_punch = [pygame.image.load('assets\Textures\Frame_punch1.png'), pygame.image.load('assets\Textures\Frame_punch2.png')]
frame_hammer = pygame.image.load('assets\Textures\Frame_hammer.png')
frame_plane = pygame.image.load('assets\Textures\Frame_plane.png')
running = True
play = False
fight = False
bank = False
stats = False
width = screen.get_width()
height = screen.get_height()
incr = 1
defeat = 0
frameId = 5
level = 1
selfXp = 0
selfAtk = 5
selfHpIn = 5
monney = 0
monneyTot = 0
neg = 0
pos = 0
victory = 0
lose = 0
dep = 0
def anim_atk(choice, monsterType):
    for i in range(296):
        screen.blit(fight_background[choice], (0, 0))
        screen.blit(monster_sprite[monsterType - 1], (650, 60))
        screen.blit(frame_atk[i//4], (750, 120))
        screen.blit(self_sprite, (0, 350))
        pygame.display.flip()
while running:
    while play:
        screen.blit(beforeFight_background, (0, 0))
        screen.blit(choice_no, (0, height-140))
        screen.blit(choice_yes, (0, height-280))
        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        if fight:
            monsterHp = int((level**2)*1.5)
            monsterHpIn = monsterHp
            monsterAtk = int((level**2)/2)+level*randint(0, int(level/2)+1)
            monsterType = randint(1, 4)
            selfHp = selfHpIn
            while fight:
                screen.blit(fight_background[choice], (0, 0))
                screen.blit(monster_sprite[monsterType-1], (650, 60))
                screen.blit(monster_name[monsterType-1], (700, 370))
                screen.blit(self_sprite, (0, 350))
                screen.blit(self_name, (70, 570))
                screen.blit(choice_atk[0], (20, height-105))
                screen.blit(choice_atk[1], (305, height - 105))
                screen.blit(choice_atk[2], (590, height - 105))
                screen.blit(choice_atk[3], (875, height - 105))
                for event in pygame.event.get():
                    mouse = pygame.mouse.get_pos()
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        running = False
                        play = False
                        fight = False
                        stats = False
                        pyqame.quit()
                        print("Merci d'avoir joué à Fisc Simulator")
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        if keys[pygame.K_ESCAPE]:
                            play = False
                            fight = False
                            bank = False
                            stats = False
                        elif keys[pygame.K_1] or (height-105 <= mouse[1] and 20 <= mouse[0] <= 295):
                            if monsterType == 1:
                                monsterHp = monsterHp - int(selfAtk*randint(7, 11)/10)
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    if monsterHp > 0:
                                        selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                        xplus = 0
                                        ymoins = 0
                                        for loop in range(100):
                                            screen.blit(fight_background[choice], (0, 0))
                                            screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                            screen.blit(self_sprite, (0, 350))
                                            screen.blit(frame_gun[0], (650, 120))
                                            pygame.display.flip()
                                        for loop in range(100):
                                            screen.blit(fight_background[choice], (0, 0))
                                            screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                            screen.blit(self_sprite, (0, 350))
                                            screen.blit(frame_gun[1], (650, 120))
                                            pygame.display.flip()
                            else:
                                monsterHp = monsterHp - int(selfAtk*randint(1, 8)/(2*level))
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[0], (20, 300))
                                        pygame.display.flip()
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[1], (20, 300))
                                        pygame.display.flip()
                        elif keys[pygame.K_2] or (height-105 <= mouse[1] and 305 <= mouse[0] <= 580):
                            if monsterType == 2:
                                monsterHp = monsterHp - int(selfAtk*randint(7, 11)/10)
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    if monsterHp > 0:
                                        selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                        xplus = 0
                                        ymoins = 0
                                        for loop in range(300):
                                            screen.blit(fight_background[choice], (0, 0))
                                            screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                            screen.blit(self_sprite, (0, 350))
                                            screen.blit(frame_hammer, (620 + xplus, 80 + ymoins))
                                            xplus = xplus - 3
                                            ymoins = ymoins + 1.5
                                            pygame.display.flip()
                            else:
                                monsterHp = monsterHp - int(selfAtk*randint(1, 8)/(2*level))
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[0], (20, 300))
                                        pygame.display.flip()
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[1], (20, 300))
                                        pygame.display.flip()
                        elif keys[pygame.K_3] or (height-105 <= mouse[1] and 590 <= mouse[0] <= 865):
                            if monsterType == 3:
                                monsterHp = monsterHp - int(selfAtk*randint(7, 11)/10)
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    xplus = 0
                                    ymoins = 0
                                    for loop in range(300):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_plane, (620+xplus, 80+ymoins))
                                        xplus = xplus - 3
                                        ymoins = ymoins + 1.5
                                        pygame.display.flip()
                            else:
                                monsterHp = monsterHp - int(selfAtk*randint(1, 8)/(2*level))
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[0], (20, 300))
                                        pygame.display.flip()
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[1], (20, 300))
                                        pygame.display.flip()
                        elif keys[pygame.K_4] or (height-105 <= mouse[1] and 815 <= mouse[0] <= width-20):
                            if monsterType == 4:
                                monsterHp = monsterHp - int(selfAtk*randint(7, 11)/10)
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    frameId = 0
                                    incr= 1
                                    for loop in range(200):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_flag[frameId // 5], (20, 200))
                                        frameId = frameId + (incr)
                                        if frameId == 49:
                                            incr = -1
                                        elif frameId == 1:
                                            incr = 1
                                        pygame.display.flip()
                                    frameId = 0
                                    incr = 1
                            else:
                                monsterHp = monsterHp - int(selfAtk*randint(1, 8)/(2*level))
                                anim_atk(choice, monsterType)
                                if monsterHp > 0:
                                    selfHp = selfHp - int(monsterAtk * randint(7, 12) / 10)
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[0], (20, 300))
                                        pygame.display.flip()
                                    for loop in range(100):
                                        screen.blit(fight_background[choice], (0, 0))
                                        screen.blit(monster_sprite[monsterType - 1], (650, 60))
                                        screen.blit(self_sprite, (0, 350))
                                        screen.blit(frame_punch[1], (20, 300))
                                        pygame.display.flip()
                        if monsterHp <= 0:
                            fight=False
                            victory = 1
                            next = True
                            while next:
                                screen.blit(win_background, (0,0))
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    keys = pygame.key.get_pressed()
                                    if event.type == pygame.QUIT:
                                        running = False
                                        play = False
                                        stats = False
                                        pyqame.quit()
                                        print("Merci d'avoir joué à Fisc Simulator")
                                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                                        if keys[pygame.K_ESCAPE]:
                                            play = False
                                            stats = False
                                            next = False
                                        else:
                                            next = False
                        elif selfHp <= 0:
                            fight = False
                            lose = 1
                            defeat = defeat + 1
                            next = True
                            while next:
                                screen.blit(lose_background, (0,0))
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    keys = pygame.key.get_pressed()
                                    if event.type == pygame.QUIT:
                                        running = False
                                        play = False
                                        stats = False
                                        pyqame.quit()
                                        print("Merci d'avoir joué à Fisc Simulator")
                                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                                        if keys[pygame.K_ESCAPE]:
                                            play = False
                                            stats = False
                                            next = False
                                        else:
                                            next = False
                if monsterHp > 0 and selfHp>0:
                    monsterHpList = str(monsterHp)
                    monsterHpInList = str(monsterHpIn)
                    monsterHpLong = len(monsterHpList)
                    monsterHpInLong = len(monsterHpInList)
                    dep = 0
                    for rang in range(0, monsterHpLong):
                        numToDisplay = int(monsterHpList[rang])
                        screen.blit(numbers[numToDisplay], ( 690+dep, 420))
                        dep = dep + 39
                    screen.blit(caractere_slash, (690+dep, 420))
                    dep = dep + 39
                    for rang in range(0, monsterHpInLong):
                        numToDisplay = int(monsterHpInList[rang])
                        screen.blit(numbers[numToDisplay], ( 690+dep, 420))
                        dep = dep + 39
                    selfHpList = str(selfHp)
                    selfHpInList = str(selfHpIn)
                    selfHpLong = len(selfHpList)
                    selfHpInLong = len(selfHpInList)
                    dep = 0
                    for rang in range(0, selfHpLong):
                        numToDisplay = int(selfHpList[rang])
                        screen.blit(numbers[numToDisplay], (70 + dep, 630))
                        dep = dep + 39
                    screen.blit(caractere_slash, (70 + dep, 630))
                    dep = dep + 39
                    for rang in range(0, selfHpInLong):
                        numToDisplay = int(selfHpInList[rang])
                        screen.blit(numbers[numToDisplay], (70 + dep, 630))
                        dep = dep + 39
                pygame.display.flip()
            if victory == 1:
                selfXp = selfXp + int((sqrt(level)*level+level**2)/sqrt(level))
                victory = 0
                pos = 1
                monney = randint(0, level) * 50 + randint(0, level ** 2) * 25
                monneyTot = monneyTot + monney
            elif lose == 1:
                lose = 0
                neg = 1
                monney = randint(0, level) * 20
                monneyTot = monneyTot - monney
                selfXp = selfXp + randint(0, level) * 10
            while selfXp >= int((sqrt(level)*level+level**2)/2):
                selfXp = selfXp - int((sqrt(level)*level+level**2)/2)
                selfAtk = selfAtk + int(sqrt(level) * randint(0, int(sqrt(level))*2)) + 2 * int(sqrt(level))
                selfHpIn = selfHpIn + int(sqrt(level) * randint(0, level))+ 10 * int(sqrt(level)) * randint(1, level+1)
                level = level +1
        while bank:
            screen.blit(monney_background, (0, 0))
            monneyList = str(monney)
            monneyTotList = str(monneyTot)
            monneyLong = len(monneyList)
            monneyTotLong = len(monneyTotList)
            if neg == 1:
                screen.blit(caractere_minus, (400, 450))
            elif pos == 1:
                screen.blit(caractere_plus, (400, 450))
            for rang in range(0, monneyLong):
                numToDisplay = int(monneyList[rang])
                screen.blit(numbers[numToDisplay], (440 + dep, 450))
                dep = dep + 39
            screen.blit(caractere_dollar, (440+dep, 450))
            dep = 0
            for rang in range(0, monneyTotLong):
                numToDisplay = int(monneyTotList[rang])
                screen.blit(numbers[numToDisplay], (430 + dep, 580))
                dep = dep + 39
            screen.blit(caractere_dollar, (430+dep, 580))
            dep = 0
            pygame.display.flip()
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    running = False
                    play = False
                    bank = False
                    stats = False
                    pyqame.quit()
                    print("Merci d'avoir joué à Fisc Simulator")
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    if keys[pygame.K_ESCAPE]:
                        play = False
                        stats = False
                        bank = False
                    else:
                        bank = False
                        neg = 0
                        pos = 0
                        monney = 0
        if monneyTot >= 1000000:
            end= True
            while end:
                if defeat == 0:
                    screen.blit(end_backgroundAlternate, (0, 0))
                else:
                    screen.blit(end_background, (0, 0))
                defeatList = str(defeat)
                defeatLong = len(defeatList)
                for rang in range(0, defeatLong):
                    numToDisplay = int(defeatList[rang])
                    screen.blit(numbers[numToDisplay], (645 + dep, 400))
                    dep = dep + 39
                screen.blit(text_times, (430 + dep, 580))
                pygame.display.flip()
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        running = False
                        play = False
                        end = False
                        stats = False
                        pyqame.quit()
                        print("Merci d'avoir joué à Fisc Simulator")
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        play = False
                        stats = False
                        end = False
                        running = False
                        pygame.quit()
        while stats:
            screen.blit(stats_background, (0, 0))
            selfAtkList = str(selfAtk)
            selfHpInList = str(selfHpIn)
            selfXpList = str(selfXp)
            levelList = str(level)
            selfAtkLong = len(selfAtkList)
            selfHpInLong = len(selfHpInList)
            selfXpLong = len(selfXpList)
            levelLong = len(levelList)
            dep = 0
            for rang in range(0, selfAtkLong):
                numToDisplay = int(selfAtkList[rang])
                screen.blit(numbers[numToDisplay], (255 + dep, 278))
                dep = dep + 39
            dep = 0
            for rang in range(0, selfHpInLong):
                numToDisplay = int(selfHpInList[rang])
                screen.blit(numbers[numToDisplay], (220 + dep, 438))
                dep = dep + 39
            dep = 0
            for rang in range(0, selfXpLong):
                numToDisplay = int(selfXpList[rang])
                screen.blit(numbers[numToDisplay], (220 + dep, 598))
                dep = dep + 39
            dep = 0
            for rang in range(0, levelLong):
                numToDisplay = int(levelList[rang])
                screen.blit(numbers[numToDisplay], (950 + dep, 78))
                dep = dep + 39
            pygame.display.flip()
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    running = False
                    play = False
                    stats = False
                    pyqame.quit()
                    print("Merci d'avoir joué à Fisc Simulator")
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    if keys[pygame.K_ESCAPE]:
                        play = False
                        stats = False
                    else:
                        stats = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False
                play = False
                pyqame.quit()
                print("Merci d'avoir joué à Fisc Simulator")
            elif event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE]:
                    play = False
                elif keys[pygame.K_1]:
                    fight = True
                    bank = True
                    stats = True
                    choice = randint(-1, 2)
                elif keys[pygame.K_2]:
                    fight = False
                    bank = True
                    stats = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if height-140 <= mouse[1]:
                    fight = False
                    bank = True
                    stats = True
                elif height-280 <= mouse[1] < height-140:
                    fight = True
                    bank = True
                    stats = True
                    choice = randint(-1, 2)
    screen.blit(background[frameId // 5], (0, 0))
    frameId = frameId + (incr)
    if frameId == 29:
        incr = -1
    elif frameId == 1:
        incr = 1
    pygame.display.flip()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
            pyqame.quit()
            print("Merci d'avoir joué à Fisc Simulator")
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            if keys[pygame.K_ESCAPE]:
                running = False
                pyqame.quit()
                print("Merci d'avoir joué à Fisc Simulator")
            else:
                play = True