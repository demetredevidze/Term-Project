# Demetre Devidze
# Term Project
# 15-112


import pygame
import random
import time
from pygame import mixer


###############################################################################


pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
displayWidth = 1000
displayHeight = 650
gameDisplay = pygame.display.set_mode(
    (displayWidth, displayHeight), pygame.RESIZABLE)
pygame.display.set_caption("Nemo")
clock = pygame.time.Clock()


###############################################################################


bg = pygame.image.load("ocean.jpg")
nemoImg = pygame.image.load("nemo.png")
shark1Img = pygame.image.load("shark1.png")
shark2Img = pygame.image.load("shark2.png")
shark3Img = pygame.image.load("shark3.png")
shark4Img = pygame.image.load("shark4.png")
sharkSmartImg = pygame.image.load("sharksmart.png")
bubbleImg = pygame.image.load("bubble.png")
goldFishImg = pygame.image.load("goldfish.png")
blackFishImg = pygame.image.load("blackfish.png")
redFishImg = pygame.image.load("redfish.png")
yellowFishImg = pygame.image.load("yellowfish.png")
tunaFishImg = pygame.image.load("tunafish.png")
angelFishImg = pygame.image.load("angelfish.png")
startButtonImg1 = pygame.image.load("startButton1.png")
startButtonImg2 = pygame.image.load("startButton2.png")
exitButtonImg1 = pygame.image.load("exitButton1.png")
exitButtonImg2 = pygame.image.load("exitButton2.png")
continueButtonImg1 = pygame.image.load("continueButton1.png")
continueButtonImg2 = pygame.image.load("continueButton2.png")
restartButtonImg1 = pygame.image.load("restart1.png")
restartButtonImg2 = pygame.image.load("restart2.png")
menuButtonImg1 = pygame.image.load("menu1.png")
menuButtonImg2 = pygame.image.load("menu2.png")
shopButtonImg1 = pygame.image.load("shop1.png")
shopButtonImg2 = pygame.image.load("shop2.png")
goldCoinImg = pygame.image.load("goldcoin.png")
ripImg = pygame.image.load("rip.png")
bubbleSound = mixer.Sound("bubbles.wav")
eatSound = mixer.Sound("eat.wav")
bubbleSound.set_volume(0.01)
biteSound = mixer.Sound("bite.mp3")
mixer.music.load("waterSound.mp3")
pygame.mixer.music.set_volume(0.03)

###############################################################################

class Bubble:

    def __init__(self, displayWidth, displayHeight):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.reset()

    def bubbleUpdate(self, displayWidth, displayHeight):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        gameDisplay.blit(pygame.transform.scale(
            bubbleImg, (self.size, self.size)), (self.x, self.y))
        self.y -= round(self.speed, 2)
        if self.y < 0:
            self.reset()

    def reset(self):
        bubbleSound.play()
        self.y = self.displayHeight
        self.x = random.randint(0, self.displayWidth)
        self.speed = random.uniform(0.5, 3.5)
        self.size = round(2.5*self.speed)

###############################################################################

class SmartShark:

    def __init__(self, displayWidth, displayHeight):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.reset()

    def smarkSharkUpdate(self):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        gameDisplay.blit(pygame.transform.scale(
            sharkSmartImg, (self.sharkSmartWidth, self.sharkSmartHeight)), (self.x, self.y))
        self.x -= self.speed
        if self.x < -self.sharkSmartWidth:
            self.reset()

    def reset(self):
        self.sharkSmartWidth = random.randint(self.displayWidth//5, self.displayWidth//4)
        self.sharkSmartHeight = round(self.sharkSmartWidth//2)
        self.y = random.randint(-self.sharkSmartHeight, self.displayHeight)
        self.x = self.displayWidth + random.randint(self.displayWidth,self.displayWidth*2)
        self.speed = random.uniform(3, 8)

###############################################################################

class GoldFish:

    def __init__(self, eat, displayWidth, displayHeight):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.eat = eat
        self.reset()

    def goldFishUpdate(self, displayWidth, displayHeight):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        if self.eat == False:
            gameDisplay.blit(pygame.transform.scale(goldFishImg,
                (self.goldFishWidth, self.goldFishHeight)), (self.x, self.y))
        self.x -= self.speed
        if self.x < -self.goldFishWidth:
            self.eat = False
            self.reset()

    def reset(self):
        self.goldFishWidth = round(self.displayWidth/16)
        self.goldFishHeight = round(self.goldFishWidth/2)
        self.x = self.goldFishWidth + self.displayWidth
        self.y = random.randint(-self.goldFishHeight, self.displayHeight)
        self.speed = random.uniform(5, 7)

###############################################################################

class Sharks:

    def __init__(self, displayWidth, displayHeight,sharksImg,caught):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.sharksImg = sharksImg
        self.caught = caught
        self.reset()

    def sharksUpdate(self, displayWidth, displayHeight):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        if self.caught == False:
            gameDisplay.blit(pygame.transform.scale(
        self.sharksImg, (self.sharksWidth, self.sharksHeight)), (self.x, self.y))
        if self.x < -self.sharksWidth:
            self.reset()
        self.x -= round(self.speed,2)

    def reset(self):
        self.sharksWidth = random.randint(self.displayWidth//5, self.displayWidth//4)
        self.sharksHeight = self.sharksWidth//2
        self.speed = random.uniform(2, 8)
        self.x = self.displayWidth
        self.y = random.randint(-self.sharksHeight, self.displayHeight)

###############################################################################

class PreyFish:

    def __init__(self, displayWidth, displayHeight, preysImg, eatPreys):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.preysImg = preysImg
        self.eatPreys = eatPreys
        self.reset()

    def preysUpdate(self, displayWidth, displayHeight, eatPreys):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.eatPreys = eatPreys
        if self.eatPreys == False:
            gameDisplay.blit(pygame.transform.scale(self.preysImg, (self.preyFishWidth, self.preyFishHeight)), (self.x, self.y))
        if self.x < - self.preyFishWidth:
            self.eatPreys = False
            self.reset()
        self.x -= round(self.speed,2)

    def reset(self):
        self.preyFishWidth = random.randint(20, 70)
        self.preyFishHeight = self.preyFishWidth//2
        self.speed = random.uniform(2, 8)
        self.x = self.displayWidth + self.preyFishWidth
        self.y = random.randint(-self.preyFishHeight, self.displayHeight)

###############################################################################

def Nemo(nemox, nemoy, nemoWidth, nemoHeight, flip, increaseWidth=0, increaseHeight=0):
    nemoImg1 = pygame.transform.scale(
        nemoImg, (nemoWidth+increaseWidth, nemoHeight+increaseHeight))
    gameDisplay.blit(pygame.transform.flip(
        nemoImg1, flip, False), (nemox, nemoy))

###############################################################################

def displayScore(score, displayWidth, displayHeight):
    font = pygame.font.SysFont(None, displayWidth//30)
    text = font.render("Your Score : " + str(score), True, white)
    gameDisplay.blit(text, (displayWidth//50, displayHeight/40))


def displayCoins(coins, displayWidth, displayHeight):
    gameDisplay.blit(pygame.transform.scale(
        goldCoinImg, (displayWidth//20, displayWidth//20)), (displayWidth//3.5, 0))
    font = pygame.font.SysFont(None, displayWidth//30)
    text = font.render(" : " + str(coins), True, white)
    gameDisplay.blit(text, (displayWidth//3, displayHeight/40))


def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

###############################################################################

def gameIntro(displayWidth, displayHeight, intro=True):

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        mouse = pygame.mouse.get_pos()

        startButtonWidth = displayWidth//5
        buttonHeight = displayHeight//13
        exitButtonWidth = displayWidth//10
        continueButtonWidth = displayWidth//8
        shopButtonWidth = displayWidth//8

        exitStart = displayWidth - displayWidth//4
        startStart = displayWidth//4 - exitButtonWidth
        buttonsY = displayHeight//1.6
        shopStart = displayWidth//2

        gameDisplay.blit(pygame.transform.scale(
            bg, (displayWidth, displayHeight)), (0, 0))
        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("Welcome to Nemo", largeText)
        TextRect.center = ((displayWidth//2), (displayHeight//2.5))
        gameDisplay.blit(TextSurf, TextRect)

        click = pygame.mouse.get_pressed()

        if startStart <= mouse[0] <= (startStart+startButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg2, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg1, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))
            time.sleep(0.01)
            pygame.display.update()
            if click[0] == 1:
                intro = False

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg2, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg1, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg1, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))
            if click[0] == 1:
                pygame.quit()
                quit()

        elif shopStart <= mouse[0] <= (shopStart+shopButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg1, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg2, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))

        else:
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg1, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg1, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))

        pygame.display.update()
        clock.tick(60)

###############################################################################

def gamePause(displayWidth, displayHeight):

    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        mouse = pygame.mouse.get_pos()

        startButtonWidth = displayWidth//5
        buttonHeight = displayHeight//13
        exitButtonWidth = displayWidth//10
        continueButtonWidth = displayWidth//8
        menuButtonWidth = displayWidth//8

        exitStart = displayWidth - displayWidth//4
        continueStart = displayWidth//4 - exitButtonWidth
        buttonsY = displayHeight//1.6
        menuStart = displayWidth//2 - menuButtonWidth//2

        gameDisplay.blit(pygame.transform.scale(
            bg, (displayWidth, displayHeight)), (0, 0))

        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("Paused", largeText)
        TextRect.center = ((displayWidth//2), (displayHeight//2))
        gameDisplay.blit(TextSurf, TextRect)

        click = pygame.mouse.get_pressed()
        if continueStart <= mouse[0] <= (continueStart+continueButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg2, (continueButtonWidth, buttonHeight)), (continueStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            time.sleep(0.01)
            if click[0] == 1:
                pause = False

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg2, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg1, (continueButtonWidth, buttonHeight)), (continueStart, buttonsY))
            if click[0] == 1:
                pygame.quit()
                quit()

        elif menuStart <= mouse[0] <= (menuStart+menuButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg1, (continueButtonWidth, buttonHeight)), (continueStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg2, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            if click[0] == 1:
                game_loop(True, displayWidth, displayHeight)

        else:
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg1, (continueButtonWidth, buttonHeight)), (continueStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))

        pygame.display.update()
        clock.tick(60)

###############################################################################

def crash(displayWidth, displayHeight):

    crash = True

    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        mouse = pygame.mouse.get_pos()

        buttonHeight = displayHeight//13
        exitButtonWidth = displayWidth//10
        restartButtonWidth = displayWidth//8
        menuButtonWidth = displayWidth//8

        exitStart = displayWidth - displayWidth//4
        restartStart = displayWidth//4 - exitButtonWidth
        buttonsY = displayHeight//1.6
        menuStart = displayWidth//2 - menuButtonWidth//2

        gameDisplay.blit(pygame.transform.scale(
            bg, (displayWidth, displayHeight)), (0, 0))

        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("You got eaten by a shark", largeText)
        TextRect.center = ((displayWidth//2), (displayHeight//2))
        gameDisplay.blit(TextSurf, TextRect)

        gameDisplay.blit(pygame.transform.scale(ripImg, (displayWidth//4, displayWidth//4)),
                         (displayWidth//2-(displayWidth//4)//2, displayHeight//15))

        click = pygame.mouse.get_pressed()

        if restartStart <= mouse[0] <= (restartStart+restartButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                restartButtonImg2, (restartButtonWidth, buttonHeight)), (restartStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(False, displayWidth, displayHeight)

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg2, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                restartButtonImg1, (restartButtonWidth, buttonHeight)), (restartStart, buttonsY))
            if click[0] == 1:
                pygame.quit()
                quit()

        elif menuStart <= mouse[0] <= (menuStart+menuButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                restartButtonImg1, (restartButtonWidth, buttonHeight)), (restartStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg2, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            if click[0] == 1:
                game_loop(True, displayWidth, displayHeight)

        else:
            gameDisplay.blit(pygame.transform.scale(
                restartButtonImg1, (restartButtonWidth, buttonHeight)), (restartStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))

        pygame.display.update()
        clock.tick(60)

###############################################################################

def game_loop(intro, displayWidth=1000, displayHeight=650):

    pygame.mixer.music.play(-1)

###############################################################################

    caught = [False]*4
    sharksImg = [shark1Img, shark2Img, shark3Img, shark4Img]
    sharks = []
    for i in range(4):
        sharks += [Sharks(displayWidth,displayHeight,sharksImg[i],caught[i])]

###############################################################################

    bubbles = []
    for i in range(15):
        bubbles += [Bubble(displayWidth,displayHeight)]

###############################################################################

    goldFish = GoldFish(False,displayWidth,displayHeight)
    smartShark = SmartShark(displayWidth,displayHeight)

###############################################################################

    preysImg = [blackFishImg, redFishImg,yellowFishImg, tunaFishImg, angelFishImg]*2
    eatPreys = [False]*10
    preyFish = []
    for i in range(10):
        preyFish += [PreyFish(displayWidth,displayHeight,preysImg[i],eatPreys[i])]

###############################################################################

    nemoWidth = round(displayWidth/12)
    nemoHeight = round(nemoWidth/2)
    nemox = (displayWidth * (0.5))
    nemoy = (displayHeight * (0.5))
    nemoMovex = 0
    nemoMovey = 0
    score = 0
    coins = 0
    flip = False
    gameExit = False

    gameIntro(displayWidth, displayHeight, intro)

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    nemoMovex = -(5-score/500)
                    flip = True
                elif event.key == pygame.K_RIGHT:
                    nemoMovex = (5-score/500)
                    flip = False
                elif event.key == pygame.K_UP:
                    nemoMovey = -(5-score/500)
                elif event.key == pygame.K_DOWN:
                    nemoMovey = (5-score/500)
                elif event.key == pygame.K_p:
                    gamePause(displayWidth, displayHeight)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    nemoMovex = 0
                if event.key == pygame.K_RIGHT:
                    nemoMovex = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    nemoMovey = 0

        nemox += nemoMovex
        nemoy += nemoMovey

        score += 0.01

        gameDisplay.blit(pygame.transform.scale(bg, (displayWidth, displayHeight)), (0, 0))

###############################################################################

        for i in range(15):
            bubbles[i].bubbleUpdate(displayWidth,displayHeight)

###############################################################################

        for i in range(10):
            preyFish[i].preysUpdate(displayWidth,displayHeight,eatPreys[i])
            eatPreys[i] = preyFish[i].eatPreys

###############################################################################

        for i in range(4):
            sharks[i].sharksUpdate(displayWidth,displayHeight)

###############################################################################

        smartShark.smarkSharkUpdate()
        goldFish.goldFishUpdate(displayWidth,displayHeight)

###############################################################################

        increaseWidth = round(score//10)
        increaseHeight = round(increaseWidth/2)
        nemoWidth = round(displayWidth/12)
        nemoHeight = (nemoWidth//2)

        Nemo(nemox, nemoy, nemoWidth, nemoHeight,
             flip, increaseWidth, increaseHeight)

        if nemox > displayWidth:
            nemox = -(nemoWidth+increaseWidth)

        if nemox < -(nemoWidth+increaseWidth):
            nemox = displayWidth

        if nemoy > displayHeight:
            nemoy = -(nemoHeight+increaseHeight)

        if nemoy < -(nemoHeight+increaseHeight):
            nemoy = displayHeight

###############################################################################

        preysImg1 = []
        preysMasks = []
        offset3 = []
        collision3 = []

        sharksImg1 = []
        sharksMasks = []
        offsetSharks = []
        sharkCollisions = []

        preysImg1 = []
        preysMasks = []
        offset3 = []
        collision3 = []

        sharksImg1 = []
        sharksMasks = []
        offsetSharks = []
        sharkCollisions = []

        nemoImg1 = pygame.transform.scale(
            nemoImg, (nemoWidth+increaseWidth, nemoHeight+increaseHeight))
        nemoImg2 = nemoImg1.convert_alpha()
        nemoMask = pygame.mask.from_surface(nemoImg2)

        sharkSmartImg1 = pygame.transform.scale(
            sharkSmartImg, (smartShark.sharkSmartWidth, smartShark.sharkSmartHeight))
        sharkSmartImg1 = sharkSmartImg1.convert_alpha()
        sharkSmartMask = pygame.mask.from_surface(sharkSmartImg1)

        goldFishImg1 = pygame.transform.scale(goldFishImg, (goldFish.goldFishWidth,goldFish.goldFishHeight))
        goldFishImg1 = goldFishImg1.convert_alpha()
        goldFishMask = nemoMask = pygame.mask.from_surface(goldFishImg1)

        offset1 = (round(nemox + increaseWidth - smartShark.x),
                   round(nemoy + increaseHeight - smartShark.y))
        collision1 = sharkSmartMask.overlap(nemoMask, offset1)

        if collision1:
            biteSound.play()
            crash(displayWidth, displayHeight)

        offset2 = (round(nemox + increaseWidth - goldFish.x),
                   round(nemoy + increaseHeight - goldFish.y))
        collision2 = goldFishMask.overlap(nemoMask, offset2)

        if goldFish.eat == False:
            if collision2:
                eatSound.play()
                coins += 50
                score += 100
                goldFish.eat = True

        for preyImg in preysImg:
            i = 0
            preysImg1 += [pygame.transform.scale(preyImg,
                                                 (preyFish[i].preyFishWidth, preyFish[i].preyFishHeight))]
            preysImg1[i] = preysImg1[i].convert_alpha()
            preysMasks += [pygame.mask.from_surface(preysImg1[i])]
            i += 1

        for i in range(10):
            offset3 += [(round(nemox + increaseWidth - preyFish[i].x),
                         round(nemoy + increaseHeight - preyFish[i].y))]
            collision3 += [preysMasks[i].overlap(nemoMask, offset3[i])]

        for i in range(10):
            if collision3[i] and eatPreys[i] == False:
                biteSound.play()
                eatPreys[i] = True
                score += preyFish[i].preyFishWidth/10
                coins += 1

        for sharkImg in sharksImg:
            i = 0
            sharksImg1 += [pygame.transform.scale(
                sharkImg, (sharks[i].sharksWidth, sharks[i].sharksHeight))]
            sharksImg1[i] = sharksImg1[i].convert_alpha()
            sharksMasks += [pygame.mask.from_surface(sharksImg1[i])]
            i += 1

        for i in range(4):
            offsetSharks += [(round(nemox + increaseWidth - sharks[i].x),
                              round(nemoy + increaseHeight - sharks[i].y))]
            sharkCollisions += [sharksMasks[i]
                                .overlap(nemoMask, offsetSharks[i])]

        for i in range(4):
            if sharkCollisions[i] and caught[i] == False:
                biteSound.play()
                crash(displayWidth, displayHeight)

###############################################################################

        if ((nemox + nemoWidth - goldFish.x)**(2) + (nemoy + nemoHeight/2 - goldFish.y - goldFish.goldFishHeight/2)**(2))**(1/2) <= displayWidth//3:
            if (goldFish.y + goldFish.goldFishHeight/2) >= (nemoy + goldFish.goldFishHeight/2):
                goldFish.y += 5
                goldFish.x -= 1
            else:
                goldFish.y -= 5
                goldFish.x -= 1

###############################################################################

        if ((nemox + nemoWidth - smartShark.x)**(2) + (nemoy + nemoHeight/2 - smartShark.y - smartShark.sharkSmartHeight/2)**(2))**(1/2) <= displayWidth//3\
           and (smartShark.x + smartShark.sharkSmartWidth) >= nemox:
            if (smartShark.y + smartShark.sharkSmartHeight/2) >= (nemoy + nemoHeight/2):
                smartShark.y -= 2.5
            else:
                smartShark.y += 2.5

###############################################################################

        displayScore(round(score), displayWidth, displayHeight)

        displayCoins(round(coins), displayWidth, displayHeight)

        pygame.display.update()

        clock.tick(60)

###############################################################################

game_loop(True, displayWidth, displayHeight)

pygame.quit()

quit()