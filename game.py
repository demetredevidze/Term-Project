# Demetre Devidze
# Term Project


import pygame
import random
import time
from pygame import mixer


###############################################################################


pygame.init()

black = (0,0,0)
white = (255,255,255)


displayWidth = 1000
displayHeight = 650
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.RESIZABLE)
pygame.display.set_caption("Nemo")
clock = pygame.time.Clock()


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
bubbleSound.set_volume(0.01)
biteSound = mixer.Sound("bite.mp3")
mixer.music.load("waterSound.mp3")
pygame.mixer.music.set_volume(0.03)


###############################################################################

def sharks(x, y, sharksWidth, sharksHeight, sharksImg):
    gameDisplay.blit(pygame.transform.scale(sharksImg, (sharksWidth, sharksHeight)), (x,y))

###############################################################################

def sharkSmart(x, y, sharkSmartWidth, sharkSmartHeight):
    gameDisplay.blit(pygame.transform.scale(sharkSmartImg, (sharkSmartWidth, sharkSmartHeight)), (x,y))

###############################################################################

def bubbles(x, y, size):
    gameDisplay.blit(pygame.transform.scale(bubbleImg, (size, size)), (x,y))

###############################################################################

def Nemo(nemox, nemoy,nemoWidth, nemoHeight, increaseWidth=0, increaseHeight=0):
    gameDisplay.blit(pygame.transform.scale(nemoImg, (nemoWidth+increaseWidth, nemoHeight+increaseHeight)), (nemox,nemoy))

###############################################################################

def preyFish(x, y, preyFishImg, preyFishWidth, preyFishHeight):
    gameDisplay.blit(pygame.transform.scale(preyFishImg, (preyFishWidth, preyFishHeight)), (x,y))

###############################################################################

def goldFish(x, y, goldFishWidth, goldFishHeight):
    gameDisplay.blit(pygame.transform.scale(goldFishImg, (goldFishWidth, goldFishHeight)), (x,y))

###############################################################################

def goldCoin(displayWidth, displayHeight):
    gameDisplay.blit(pygame.transform.scale(goldCoinImg, (displayWidth//20, displayWidth//20)), (displayWidth//3.5,0))

###############################################################################


def gameIntro(displayWidth, displayHeight, intro = True):


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

        gameDisplay.blit(pygame.transform.scale(bg, (displayWidth, displayHeight)), (0,0))
        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("Welcome to Nemo", largeText)
        TextRect.center = ((displayWidth//2),(displayHeight//2.5))
        gameDisplay.blit(TextSurf, TextRect)

        click = pygame.mouse.get_pressed()

        if startStart <= mouse[0] <= (startStart+startButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(startButtonImg2, (startButtonWidth,buttonHeight)),(startStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth, buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(shopButtonImg1, (shopButtonWidth, buttonHeight)),(shopStart,buttonsY))
            time.sleep(0.01)
            pygame.display.update()
            if click[0] == 1:
                intro = False

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(exitButtonImg2, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(startButtonImg1, (startButtonWidth, buttonHeight)),(startStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(shopButtonImg1, (shopButtonWidth, buttonHeight)),(shopStart,buttonsY))
            if click[0] == 1:
                pygame.quit()
                quit()

        elif shopStart <= mouse[0] <= (shopStart+shopButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(startButtonImg1, (startButtonWidth, buttonHeight)),(startStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(shopButtonImg2, (shopButtonWidth, buttonHeight)),(shopStart,buttonsY))


        else:
            gameDisplay.blit(pygame.transform.scale(startButtonImg1, (startButtonWidth, buttonHeight)),(startStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth, buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(shopButtonImg1, (shopButtonWidth, buttonHeight)),(shopStart,buttonsY))

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

        gameDisplay.blit(pygame.transform.scale(bg, (displayWidth, displayHeight)), (0,0))

        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("Paused", largeText)
        TextRect.center = ((displayWidth//2),(displayHeight//2))
        gameDisplay.blit(TextSurf, TextRect)

        click = pygame.mouse.get_pressed()
        if continueStart <= mouse[0] <= (continueStart+continueButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(menuButtonImg1, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(continueButtonImg2, (continueButtonWidth,buttonHeight)), (continueStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            time.sleep(0.01)
            if click[0] == 1:
                pause = False

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(menuButtonImg1, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg2, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(continueButtonImg1, (continueButtonWidth,buttonHeight)),(continueStart,buttonsY))
            if click[0] == 1:
                pygame.quit()
                quit()

        elif menuStart <= mouse[0] <= (menuStart+menuButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(continueButtonImg1, (continueButtonWidth, buttonHeight)),(continueStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(menuButtonImg2, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))
            if click[0] == 1:
               game_loop(True,displayWidth,displayHeight)

        else:
            gameDisplay.blit(pygame.transform.scale(continueButtonImg1, (continueButtonWidth,buttonHeight)),(continueStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(menuButtonImg1, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))

        pygame.display.update()
        clock.tick(60)



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


        gameDisplay.blit(pygame.transform.scale(bg, (displayWidth, displayHeight)), (0,0))

        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("You got eaten by a shark", largeText)
        TextRect.center = ((displayWidth//2),(displayHeight//2))
        gameDisplay.blit(TextSurf, TextRect)

        gameDisplay.blit(pygame.transform.scale(ripImg, (displayWidth//4,displayWidth//4)), (displayWidth//2-(displayWidth//4)//2,displayHeight//15))

        click = pygame.mouse.get_pressed()

        if restartStart <= mouse[0] <= (restartStart+restartButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(menuButtonImg1, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(restartButtonImg2, (restartButtonWidth,buttonHeight)),(restartStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(False,displayWidth,displayHeight)

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(menuButtonImg1, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg2, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(restartButtonImg1, (restartButtonWidth,buttonHeight)),(restartStart,buttonsY))
            if click[0] == 1:
                pygame.quit()
                quit()

        elif menuStart <= mouse[0] <= (menuStart+menuButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(restartButtonImg1, (restartButtonWidth, buttonHeight)),(restartStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(menuButtonImg2, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))
            if click[0] == 1:
               game_loop(True,displayWidth,displayHeight)

        else:
            gameDisplay.blit(pygame.transform.scale(restartButtonImg1, (restartButtonWidth,buttonHeight)),(restartStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(exitButtonImg1, (exitButtonWidth,buttonHeight)),(exitStart,buttonsY))
            gameDisplay.blit(pygame.transform.scale(menuButtonImg1, (menuButtonWidth, buttonHeight)),(menuStart,buttonsY))

        pygame.display.update()
        clock.tick(60)


def displayScore(score,displayWidth,displayHeight):
    font = pygame.font.SysFont(None, displayWidth//30)
    text = font.render("Your Score : " +str(score), True, white)
    gameDisplay.blit(text, (displayWidth//50,displayHeight/40))


def displayCoins(coins,displayWidth,displayHeight):
    font = pygame.font.SysFont(None, displayWidth//30)
    text = font.render(" : " +str(coins), True, white)
    gameDisplay.blit(text, (displayWidth//3,displayHeight/40))


def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect.center = ((displayWidth//2),(displayHeight//2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    gameIntro(displayWidth, displayHeight)


##def crash():
##    message_display("You Crashed")

###############################################################################

def game_loop(x,displayWidth = 1000, displayHeight = 650):

    nemoWidth = round(displayWidth/12)
    nemoHeight = round(nemoWidth/2)

    goldFishWidth = round(displayWidth/16)
    goldFishHeight = round(goldFishWidth/2)

    preyFishWidth = round(displayWidth/22)
    preyFishHeight = round(preyFishWidth/2)

    pygame.mixer.music.play(-1)

    sharksImg = [shark1Img, shark2Img, shark3Img, shark4Img]*2

    sharksWidth = []
    sharksHeight = []
    sharksStarty = []
    sharksStartx = []
    sharksSpeed = []

    for i in range(8):
        sharksWidth += [random.randint(displayWidth//5,displayWidth//4)]
        sharksHeight += [sharksWidth[i]//2]
        sharksSpeed += [random.uniform(2,8)]
        sharksStartx += [displayWidth]
        sharksStarty += [random.randint(-sharksHeight[i], displayHeight)]

###############################################################################

    sharkSmartWidth = random.randint(displayWidth//5,displayWidth//4)
    sharkSmartHeight = round(sharkSmartWidth/2)
    sharkSmartStarty = random.randint(-sharkSmartHeight, displayHeight)
    sharkSmartSpeed = random.uniform(2,8)
    sharkSmartStartx = displayWidth + sharkSmartWidth

###############################################################################

    bubblesSpeed = []
    bubblesStartx = []
    bubblesStarty = [displayHeight]*15

    for a in range(3):
        for b in range(5):
            bubblesSpeed += [random.uniform(a+0.5,a+1.5)]

    for i in range(15):
        bubblesStartx += [random.randint(0, displayWidth)]

###############################################################################

    goldFishStarty = random.randint(-goldFishHeight, displayHeight)
    goldFishSpeed = random.uniform(5,10)
    goldFishStartx = displayWidth + goldFishWidth

###############################################################################

    preysImg = [blackFishImg, redFishImg, yellowFishImg, tunaFishImg, angelFishImg]*2

    preysWidth = []
    preysHeight = []
    preysStarty = []
    preysStartx = []
    preysSpeed = []

    for i in range(10):
        preysWidth += [random.randint(20,50)]
        preysHeight += [preysWidth[i]//2]
        preysStarty += [random.randint(-preysHeight[i],displayHeight)]
        preysStartx += [displayWidth + preysWidth[i]]
        preysSpeed += [random.uniform(2,8)]

###############################################################################

    nemox = (displayWidth * (0.5))
    nemoy = (displayHeight * (0.5))

    nemoMovex = 0
    nemoMovey = 0

    score = 0
    coins = 0
    d = 0

    gameExit = False

    gameIntro(displayWidth, displayHeight, x)

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
                    nemoMovex = -5
                elif event.key == pygame.K_RIGHT:
                    nemoMovex = 5
                elif event.key == pygame.K_UP:
                    nemoMovey = -5
                elif event.key == pygame.K_DOWN:
                    nemoMovey = 5
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

##        if nemoMovex > 0:
##            nemoMovex -= 0.1
##
##        if nemoMovex < 0:
##            nemoMovex += 0.1

        gameDisplay.blit(pygame.transform.scale(bg, (displayWidth, displayHeight)), (0,0))


###############################################################################

        for i in range(15):
            bubbles(bubblesStartx[i],bubblesStarty[i],round(2.5*bubblesSpeed[i]))
            bubblesStarty[i] = bubblesStarty[i] - round(bubblesSpeed[i],2)
            if bubblesStarty[i] < 0:
                bubbleSound.play()
                bubblesStarty[i] = displayHeight
                bubblesStartx[i] = random.randint(0,displayWidth)
                bubblesSpeed[i] = random.uniform(bubblesSpeed[i]//1,bubblesSpeed[i]//1 + 1)

###############################################################################

        for i in range(8):
            sharks(sharksStartx[i], sharksStarty[i], sharksWidth[i], sharksHeight[i], sharksImg[i])
            sharksStartx[i] = sharksStartx[i] - round(sharksSpeed[i],2)
            if sharksStartx[i] < -sharksWidth[i]:
                sharksStartx[i] = displayWidth
                sharksStarty[i] = random.randint(-sharksHeight[i], displayHeight)
                sharksSpeed[i] = random.uniform(2,8)
                sharksWidth[i] = random.randint(displayWidth//5,displayWidth//4)
                sharksHeight[i] = sharksWidth[i]//2

###############################################################################

        sharkSmart(sharkSmartStartx, sharkSmartStarty, sharkSmartWidth, sharkSmartHeight)
        sharkSmartStartx -= sharkSmartSpeed

        if sharkSmartStartx < -sharkSmartWidth:
            sharkSmartWidth = random.randint(displayWidth//5,displayWidth//4)
            sharkSmartHeight = (sharkSmartWidth//2)
            sharkSmartStarty = random.randint(-sharkSmartHeight, displayHeight)
            sharkSmartSpeed = random.uniform(2,8)
            sharkSmartStartx = displayWidth + sharkSmartWidth

###############################################################################

        goldFishWidth = round(displayWidth/16)
        goldFishHeight = (goldFishWidth//2)
        goldFish(goldFishStartx, goldFishStarty,goldFishWidth, goldFishHeight)
        goldFishStartx -= goldFishSpeed

        if goldFishStartx < -goldFishWidth:
            goldFishStarty = random.randint(-goldFishHeight, displayHeight)
            goldFishSpeed = random.uniform(5,10)
            goldFishStartx = displayWidth + goldFishWidth

        if goldFishStarty > displayHeight:
            goldFishStarty = -goldFishHeight

        if goldFishStarty < -goldFishHeight:
            goldFishStarty = displayHeight

###############################################################################

        preyFishWidth = round(displayWidth/22)
        preyFishHeight = round(preyFishWidth/2)

        for i in range(10):
            preyFish(preysStartx[i], preysStarty[i], preysImg[i], preysWidth[i], preysHeight[i])
            preysStartx[i] = preysStartx[i] - preysSpeed[i]
            if preysStartx[i] < -preysWidth[i]:
                preysWidth[i] = random.randint(20,50)
                preysHeight[i] = preysWidth[i]//2
                preysStarty[i] = random.randint(-preysHeight[i],displayHeight)
                preysStartx[i] = displayWidth + preysWidth[i]
                preysSpeed[i] = random.uniform(2,8)

###############################################################################

        increaseWidth = round(score//10)
        increaseHeight = round(increaseWidth/2)
        nemoWidth = round(displayWidth/12)
        nemoHeight = (nemoWidth//2)

        Nemo(nemox,nemoy,nemoWidth,nemoHeight,increaseWidth,increaseHeight)

        if nemox > displayWidth:
            nemox = -nemoWidth

        if nemox < -nemoWidth:
            nemox = displayWidth

        if nemoy > displayHeight:
            nemoy = -nemoHeight

        if nemoy < -nemoHeight:
            nemoy = displayHeight

        score += 0.0001

        nemoImg1 = pygame.transform.scale(nemoImg, (nemoWidth,nemoHeight))
        nemoImg1 = nemoImg1.convert_alpha()
        nemoMask = pygame.mask.from_surface(nemoImg1)

        sharkSmartImg1 = pygame.transform.scale(sharkSmartImg, (sharkSmartWidth,sharkSmartHeight))
        sharkSmartImg1 = sharkSmartImg1.convert_alpha()
        sharkSmartMask = pygame.mask.from_surface(sharkSmartImg1)

        offset = (round(nemox - sharkSmartStartx), round(nemoy - sharkSmartStarty) )
        collision = sharkSmartMask.overlap(nemoMask,offset)
        if collision:
            biteSound.play()
            crash(displayWidth, displayHeight)

###############################################################################

        if ((nemox + nemoWidth - goldFishStartx)**(2) + (nemoy + nemoHeight/2 - goldFishStarty - goldFishHeight/2)**(2))**(1/2) <= 150:
            if (goldFishStarty + goldFishHeight/2) >= (nemoy + goldFishHeight/2):
                goldFishStarty += 3
            if (goldFishStarty + goldFishHeight/2) < (nemoy + goldFishHeight/2):
                goldFishStarty -= 3

###############################################################################

        if ((nemox + nemoWidth - sharkSmartStartx)**(2) + (nemoy + nemoHeight/2 - sharkSmartStarty - sharkSmartHeight/2)**(2))**(1/2) <= 400\
           and (sharkSmartStartx + sharkSmartWidth) >= nemox:
            if (sharkSmartStarty + sharkSmartHeight/2) >= (nemoy + nemoHeight/2):
                sharkSmartStarty -= 2
            if (sharkSmartStarty + sharkSmartHeight/2) < (nemoy + nemoHeight/2):
                sharkSmartStarty += 2

###############################################################################

        displayScore(round(score), displayWidth, displayHeight)

        displayCoins(coins, displayWidth, displayHeight)

        goldCoin(displayWidth, displayHeight)

        pygame.display.update()

        clock.tick(60)

##gameIntro(displayWidth, displayHeight)

game_loop(True, displayWidth, displayHeight)

pygame.quit()

quit()
