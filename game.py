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
displayHeight = 600
<<<<<<< HEAD
FPS = 60
=======
FPS = 50
>>>>>>> 475b4d8 (fix_some_bugs)
score = 0
coins = 0
upgradeSpeed = 0
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight), pygame.RESIZABLE)
pygame.display.set_caption("Nemo")
clock = pygame.time.Clock()

###############################################################################

# loading all the neccesary files at the beginning
nemoImgs = []
for i in range(8):
    filename = "pics/nemo" + str(i+1) + ".png"
    nemoImgs += [pygame.image.load(filename)]
smartSharkImgs = []
for i in range(8):
    fileName = "pics/smartShark" + str(i+1) + ".png"
    smartSharkImgs += [pygame.image.load(fileName)]
goldFishImgs = []
for i in range(8):
    fileName = "pics/goldFish" + str(i+1) + ".png"
    goldFishImgs += [pygame.image.load(fileName)]
<<<<<<< HEAD
bgs = []
for i in range(75):
    fileName = "frame_" + str(i) + "_delay-0.07s.gif"
    bgs += [pygame.image.load(fileName)]
=======

bgImg = pygame.image.load("pics/back.jpg")
>>>>>>> 475b4d8 (fix_some_bugs)
shark1Img = pygame.image.load("pics/shark1.png")
shark2Img = pygame.image.load("pics/shark2.png")
shark3Img = pygame.image.load("pics/shark3.png")
shark4Img = pygame.image.load("pics/shark4.png")
bubbleImg = pygame.image.load("pics/bubble.png")
blackFishImg = pygame.image.load("pics/blackfish.png")
redFishImg = pygame.image.load("pics/redfish.png")
yellowFishImg = pygame.image.load("pics/yellowfish.png")
tunaFishImg = pygame.image.load("pics/tunafish.png")
angelFishImg = pygame.image.load("pics/angelfish.png")
startButtonImg1 = pygame.image.load("pics/startButton1.png")
startButtonImg2 = pygame.image.load("pics/startButton2.png")
exitButtonImg1 = pygame.image.load("pics/exitButton1.png")
exitButtonImg2 = pygame.image.load("pics/exitButton2.png")
continueButtonImg1 = pygame.image.load("pics/continueButton1.png")
continueButtonImg2 = pygame.image.load("pics/continueButton2.png")
restartButtonImg1 = pygame.image.load("pics/restart1.png")
restartButtonImg2 = pygame.image.load("pics/restart2.png")
menuButtonImg1 = pygame.image.load("pics/menu1.png")
menuButtonImg2 = pygame.image.load("pics/menu2.png")
shopButtonImg1 = pygame.image.load("pics/shop1.png")
shopButtonImg2 = pygame.image.load("pics/shop2.png")
instructionsButtonImg1 = pygame.image.load("pics/instructionsButton1.png")
instructionsButtonImg2 = pygame.image.load("pics/instructionsButton2.png")
<<<<<<< HEAD
instructionsImg = pygame.image.load("instructions.png")
=======
instructionsImg = pygame.image.load("pics/instructions.jpg")
>>>>>>> 475b4d8 (fix_some_bugs)
backButtonImg1 = pygame.image.load("pics/backButton1.png")
backButtonImg2 = pygame.image.load("pics/backButton2.png")
upgradeButtonImg1 = pygame.image.load("pics/upgradeButton1.png")
upgradeButtonImg2 = pygame.image.load("pics/upgradeButton2.png")
upgradeButtonImg3 = pygame.image.load("pics/upgradeButton3.png")
goldCoinImg = pygame.image.load("pics/goldcoin.png")
ripImg = pygame.image.load("pics/rip.png")
bubbleSound = mixer.Sound("bubbles.wav")
eatSound = mixer.Sound("eat.wav")
bubbleSound.set_volume(0.02)
biteSound = mixer.Sound("bite.mp3")
mixer.music.load("waterSound.mp3")
pygame.mixer.music.set_volume(0.02)

###############################################################################

class Bubble:

    def __init__(self, displayWidthNew, displayHeightNew):
        self.displayHeight = displayHeightNew
        self.displayWidth = displayWidthNew
        self.reset()

    def bubbleUpdate(self, displayWidthNew, displayHeightNew):
        self.displayHeight = displayHeightNew
        self.displayWidth = displayWidthNew
        gameDisplay.blit(pygame.transform.scale(
            bubbleImg, (self.size, self.size)), (self.x, self.y))
        self.y -= round(self.speed, 2)
        if self.y < 0:
            self.reset()

    def reset(self):
        bubbleSound.play()
        self.y = self.displayHeight + random.randint(0,self.displayHeight)
        self.x = random.randint(0, self.displayWidth)
        self.speed = random.uniform(self.displayWidth/2000, self.displayWidth/285)
        self.size = round(2.5*self.speed)

###############################################################################

class SmartShark:

    def __init__(self, displayWidthNew, displayHeightNew, c):
        self.displayHeight = displayHeightNew
        self.displayWidth = displayWidthNew
        self.c = c
        self.reset()

    def smartSharkUpdate(self, displayWidthNew, displayHeightNew):
        self.displayHeight = displayHeightNew
        self.displayWidth = displayWidthNew
        if self.randSide == 0:
            gameDisplay.blit(pygame.transform.scale(
                smartSharkImgs[(self.c%60)//8], (self.smartSharkWidth,
                    self.smartSharkHeight)), (self.x, self.y))
        if self.randSide == 1:
            smartSharkImgs1 = pygame.transform.scale(
                smartSharkImgs[(self.c%60)//8],
                    (self.smartSharkWidth, self.smartSharkHeight))
            gameDisplay.blit(pygame.transform.flip(smartSharkImgs1, True, False),
                (self.x, self.y))
        if self.randSide == 0:
            self.x -= self.speed
        if self.randSide == 1:
            self.x += self.speed
        if self.x < -self.smartSharkWidth and self.randSide == 0:
            self.reset()
        if self.x > self.displayWidth and self.randSide == 1:
            self.reset()

    def reset(self):
        self.randSide = random.randint(0,1)
        self.smartSharkWidth = random.randint(self.displayWidth//5, self.displayWidth//4)
        self.smartSharkHeight = round(self.smartSharkWidth//2)
        self.y = random.randint(-self.smartSharkHeight, self.displayHeight)
        if self.randSide == 0:
            self.x = self.displayWidth + random.randint(self.displayWidth,self.displayWidth*2)
        if self.randSide == 1:
            self.x = -random.randint(self.displayWidth//2,self.displayWidth)
        self.speed = random.uniform(self.displayWidth/333, self.displayWidth/125)

###############################################################################

class GoldFish:

    def __init__(self, eat, displayWidthNew, displayHeightNew, c):
        self.displayHeight = displayHeightNew
        self.displayWidth = displayWidthNew
        self.eat = eat
        self.c = c
        self.reset()

    def goldFishUpdate(self, displayWidthNew, displayHeightNew):
        self.displayHeight = displayHeightNew
        self.displayWidth = displayWidthNew
        if self.eat == False and self.randSide == 0:
            gameDisplay.blit(pygame.transform.scale(goldFishImgs[(self.c%60)//8],
                (self.goldFishWidth, self.goldFishHeight)), (self.x, self.y))
        if self.eat == False and self.randSide == 1:
            goldFishImg1 = pygame.transform.scale(goldFishImgs[(self.c%60)//8],
                (self.goldFishWidth, self.goldFishHeight))
            gameDisplay.blit(pygame.transform.flip(goldFishImg1, True, False),
                (self.x, self.y))
        if self.randSide == 0:
            self.x -= self.speed
        if self.randSide == 1:
            self.x += self.speed
        if self.x < -self.goldFishWidth and self.randSide == 0:
            self.eat = False
            self.reset()
        if self.x > self.displayWidth and self.randSide == 1:
            self.eat = False
            self.reset()

    def reset(self):
        self.randSide = random.randint(0,1)
        self.goldFishWidth = round(self.displayWidth/12)
        self.goldFishHeight = round(self.goldFishWidth/2)
        self.speed = random.uniform(self.displayWidth/200, self.displayWidth/143)
        if self.randSide == 0:
            self.x = self.displayWidth + random.randint(0,self.displayWidth)
        if self.randSide == 1:
            self.x = -random.randint(self.displayWidth//2,self.displayWidth)
        self.y = random.randint(-self.goldFishHeight, self.displayHeight)

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
        if self.caught == False and self.randSide == 0:
            gameDisplay.blit(pygame.transform.scale(
        self.sharksImg, (self.sharksWidth, self.sharksHeight)),
            (self.x, self.y))
        if self.caught == False and self.randSide == 1:
            sharksImg1 = pygame.transform.scale(self.sharksImg,
                (self.sharksWidth, self.sharksHeight))
            gameDisplay.blit(pygame.transform.flip(sharksImg1, True, False),
                (self.x, self.y))
        if self.x < -self.sharksWidth and self.randSide == 0:
            self.reset()
        if self.x > self.displayWidth and self.randSide == 1:
            self.reset()
        if self.randSide == 0:
            self.x -= round(self.speed,2)
        if self.randSide == 1:
            self.x += round(self.speed,2)

    def reset(self):
        self.randSide = random.randint(0,1)
        self.sharksWidth = random.randint(self.displayWidth//5, self.displayWidth//4)
        self.sharksHeight = self.sharksWidth//2
        self.speed = random.uniform(self.displayWidth/333, self.displayWidth/125)
        if self.randSide == 0:
            self.x = self.displayWidth + random.randint(0,self.displayWidth)
        if self.randSide == 1:
            self.x = -random.randint(self.displayWidth//2,self.displayWidth)
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
        if self.eatPreys == False and self.randSide == 0:
            gameDisplay.blit(pygame.transform.scale(self.preysImg,
                (self.preyFishWidth, self.preyFishHeight)), (self.x, self.y))
        if self.eatPreys == False and self.randSide == 1:
            preysImg1 = pygame.transform.scale(self.preysImg,
                (self.preyFishWidth, self.preyFishHeight))
            gameDisplay.blit(pygame.transform.flip(preysImg1, True, False),
                (self.x, self.y))
        if self.x < - self.preyFishWidth and self.randSide == 0:
            self.eatPreys = False
            self.reset()
        if self.x > self.displayWidth and self.randSide == 1:
            self.eatPreys = False
            self.reset()
        if self.randSide == 0:
            self.x -= round(self.speed,2)
        if self.randSide == 1:
            self.x += round(self.speed,2)

    def reset(self):
        self.randSide = random.randint(0,1)
        self.preyFishWidth = random.randint(self.displayWidth//40, self.displayWidth//20)
        self.preyFishHeight = self.preyFishWidth//2
        self.speed = random.uniform(self.displayWidth/333, self.displayWidth/125)
        if self.randSide == 0:
            self.x = self.displayWidth + random.randint(0,self.displayWidth)
        if self.randSide == 1:
            self.x = -random.randint(self.displayWidth//2,self.displayWidth)
        self.y = random.randint(-self.preyFishHeight, self.displayHeight)

###############################################################################

def Nemo(nemox, nemoy, nemoWidth, nemoHeight, flip, c):
    nemoImg1 = pygame.transform.scale(nemoImgs[(c%60)//8], (nemoWidth, nemoHeight))
    gameDisplay.blit(pygame.transform.flip(nemoImg1, flip, False), (nemox, nemoy))

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

def gameIntro(displayWidth, displayHeight, c, coins, intro, upgradeSpeed):

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    time.sleep(0.1)
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    time.sleep(0.1)
                    intro = False
                if event.key == pygame.K_i:
                    time.sleep(0.1)
                    gameInstructions(displayWidth, displayHeight, coins, c, upgradeSpeed)
            elif event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        mouse = pygame.mouse.get_pos()

        instructionsButtonWidth = displayWidth//5
        startButtonWidth = displayWidth//5
        buttonHeight = displayHeight//12
        exitButtonWidth = displayWidth//10
        continueButtonWidth = displayWidth//8
        shopButtonWidth = displayWidth//8

        exitStart = displayWidth - displayWidth//4
        startStart = displayWidth//4 - exitButtonWidth
        buttonsY = displayHeight//1.6
        shopStart = displayWidth//2

        # bgs[(c%75)//25] in this expression c is used for animations
        # c stands for count and tracks how many frames have been passed
        # so to display each shot of animation for a specific number of frames
        gameDisplay.blit(pygame.transform.scale(
<<<<<<< HEAD
            bgs[(c%75)//25], (displayWidth, displayHeight)), (0, 0))
=======
            bgImg, (displayWidth, displayHeight)), (0, 0))
>>>>>>> 475b4d8 (fix_some_bugs)
        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("Welcome to Nemo", largeText)
        TextRect.center = ((displayWidth//2), (displayHeight//2.5))
        gameDisplay.blit(TextSurf, TextRect)
        displayCoins(round(coins), displayWidth, displayHeight)

        click = pygame.mouse.get_pressed()
        c += 1

        if startStart <= mouse[0] <= (startStart+startButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg2, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg1, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                instructionsButtonImg1, (instructionsButtonWidth, buttonHeight)), (0, 0))
            time.sleep(0.01)
            pygame.display.update()
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(False, displayWidth, displayHeight, score, coins, upgradeSpeed)

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg2, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg1, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg1, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                instructionsButtonImg1, (instructionsButtonWidth, buttonHeight)), (0, 0))
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
            gameDisplay.blit(pygame.transform.scale(
                instructionsButtonImg1, (instructionsButtonWidth, buttonHeight)), (0, 0))
            if click[0] == 1:
                time.sleep(0.2)
                gameShop(displayWidth, displayHeight, coins, c, upgradeSpeed)

        elif 0 <= mouse[0] <= instructionsButtonWidth and 0 <= mouse[1] <= buttonHeight:
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg1, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg1, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                instructionsButtonImg2, (instructionsButtonWidth, buttonHeight)), (0, 0))
            if click[0] == 1:
                time.sleep(0.1)
                gameInstructions(displayWidth, displayHeight, coins, c, upgradeSpeed)

        else:
            gameDisplay.blit(pygame.transform.scale(
                startButtonImg1, (startButtonWidth, buttonHeight)), (startStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                shopButtonImg1, (shopButtonWidth, buttonHeight)), (shopStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                instructionsButtonImg1, (instructionsButtonWidth, buttonHeight)), (0, 0))

        pygame.display.update()
        clock.tick(FPS)

###############################################################################

def gamePause(displayWidth, displayHeight, score, coins, c, upgradeSpeed):

    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                if event.key == pygame.K_m:
                    time.sleep(0.1)
                    game_loop(True, displayWidth, displayHeight, score, coins, upgradeSpeed)
                if event.key == pygame.K_e:
                    pygame.quit()
                    quit()
            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        mouse = pygame.mouse.get_pos()

        startButtonWidth = displayWidth//5
        buttonHeight = displayHeight//12
        exitButtonWidth = displayWidth//10
        continueButtonWidth = displayWidth//8
        menuButtonWidth = displayWidth//8

        exitStart = displayWidth - displayWidth//4
        continueStart = displayWidth//4 - exitButtonWidth
        buttonsY = displayHeight//1.6
        menuStart = displayWidth//2 - menuButtonWidth//2

        gameDisplay.blit(pygame.transform.scale(
<<<<<<< HEAD
            bgs[(c%75)//25], (displayWidth, displayHeight)), (0, 0))
=======
            bgImg, (displayWidth, displayHeight)), (0, 0))
>>>>>>> 475b4d8 (fix_some_bugs)

        displayScore(round(score), displayWidth, displayHeight)
        displayCoins(round(coins), displayWidth, displayHeight)

        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("Paused", largeText)
        TextRect.center = ((displayWidth//2), (displayHeight//2))
        gameDisplay.blit(TextSurf, TextRect)
        c += 1

        click = pygame.mouse.get_pressed()
        if continueStart <= mouse[0] <= (continueStart+continueButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg2, (continueButtonWidth, buttonHeight)),
                    (continueStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(False, displayWidth, displayHeight, score, coins, upgradeSpeed)

        elif exitStart <= mouse[0] <= (exitStart+exitButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg2, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg1, (continueButtonWidth, buttonHeight)),
                    (continueStart, buttonsY))
            if click[0] == 1:
                pygame.quit()
                quit()

        elif menuStart <= mouse[0] <= (menuStart+menuButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg1, (continueButtonWidth, buttonHeight)),
                    (continueStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg2, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(True, displayWidth, displayHeight, score, coins, upgradeSpeed)

        else:
            gameDisplay.blit(pygame.transform.scale(
                continueButtonImg1, (continueButtonWidth, buttonHeight)),
                    (continueStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))

        pygame.display.update()
        clock.tick(FPS)

###############################################################################

def crash(displayWidth, displayHeight, score, coins, c, upgradeSpeed):

    crash = True

    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    time.sleep(0.1)
                    game_loop(False, displayWidth, displayHeight,0, coins, upgradeSpeed)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    time.sleep(0.1)
                    game_loop(True, displayWidth, displayHeight,0, coins, upgradeSpeed)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    time.sleep(0.1)
                    pygame.quit()
                    quit()
            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        mouse = pygame.mouse.get_pos()

        buttonHeight = displayHeight//12
        exitButtonWidth = displayWidth//10
        restartButtonWidth = displayWidth//8
        menuButtonWidth = displayWidth//8

        exitStart = displayWidth - displayWidth//4
        restartStart = displayWidth//4 - exitButtonWidth
        buttonsY = displayHeight//1.6
        menuStart = displayWidth//2 - menuButtonWidth//2

        gameDisplay.blit(pygame.transform.scale(
<<<<<<< HEAD
            bgs[(c%75)//25], (displayWidth, displayHeight)), (0, 0))
=======
            bgImg, (displayWidth, displayHeight)), (0, 0))
>>>>>>> 475b4d8 (fix_some_bugs)

        displayScore(round(score), displayWidth, displayHeight)
        displayCoins(round(coins), displayWidth, displayHeight)

        largeText = pygame.font.Font("freesansbold.ttf", displayWidth//20)
        TextSurf, TextRect = textObjects("You got eaten by a shark", largeText)
        TextRect.center = ((displayWidth//2), (displayHeight//2))
        gameDisplay.blit(TextSurf, TextRect)

        gameDisplay.blit(pygame.transform.scale(ripImg, (displayWidth//4, displayWidth//4)),
                         (displayWidth//2-(displayWidth//4)//2, displayHeight//15))

        click = pygame.mouse.get_pressed()
        c += 1

        if restartStart <= mouse[0] <= (restartStart+restartButtonWidth) and buttonsY <= mouse[1] <= (buttonsY+buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                restartButtonImg2, (restartButtonWidth, buttonHeight)), (restartStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(False, displayWidth, displayHeight, 0, coins, upgradeSpeed)

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
                restartButtonImg1, (restartButtonWidth, buttonHeight)),
                    (restartStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg2, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(True, displayWidth, displayHeight, 0, coins, upgradeSpeed)

        else:
            gameDisplay.blit(pygame.transform.scale(
                restartButtonImg1, (restartButtonWidth, buttonHeight)),
                    (restartStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                exitButtonImg1, (exitButtonWidth, buttonHeight)), (exitStart, buttonsY))
            gameDisplay.blit(pygame.transform.scale(
                menuButtonImg1, (menuButtonWidth, buttonHeight)), (menuStart, buttonsY))

        pygame.display.update()
        clock.tick(FPS)

###############################################################################

def gameInstructions(displayWidth, displayHeight, coins, c, upgradeSpeed):

    instructions = True

    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    time.sleep(0.1)
                    game_loop(True, displayWidth, displayHeight, 0, coins, upgradeSpeed)
            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        goldFishWidth = displayWidth//10
        goldFishHeight = goldFishWidth//2
<<<<<<< HEAD
        fishx = displayWidth - round(displayWidth/4)
        fishy = displayHeight - round(displayHeight/2.5)

        sharkWidth = displayWidth//5
        sharkHeight = sharkWidth//2
        sharkx = displayWidth - round(displayWidth/1.9)
        sharky = displayHeight - round(displayHeight/1.5)

        nemoWidth = displayWidth//10
        nemoHeight = nemoWidth//2
        nemox = displayWidth - round(displayWidth/2)
        nemoy = displayHeight - round(displayHeight/4.8)
=======
        fishx = displayWidth - round(displayWidth/4.3)
        fishy = displayHeight - round(displayHeight/2.25)

        sharkWidth = displayWidth//5
        sharkHeight = sharkWidth//2
        sharkx = displayWidth - round(displayWidth/1.7)
        sharky = displayHeight - round(displayHeight/1.52)

        nemoWidth = displayWidth//10
        nemoHeight = nemoWidth//2
        nemox = displayWidth - round(displayWidth/2.9)
        nemoy = displayHeight - round(displayHeight/3.5)
>>>>>>> 475b4d8 (fix_some_bugs)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        c += 1

        gameDisplay.blit(pygame.transform.scale(
            instructionsImg, (displayWidth, displayHeight)), (0, 0))

        gameDisplay.blit(pygame.transform.scale(goldFishImgs[(c%60)//8],
                (goldFishWidth, goldFishHeight)), (fishx, fishy))

        gameDisplay.blit(pygame.transform.scale(smartSharkImgs[(c%60)//8],
                (sharkWidth, sharkHeight)), (sharkx, sharky))

        nemoImg = pygame.transform.flip(nemoImgs[(c%60)//8], True, False)
        gameDisplay.blit(pygame.transform.scale(nemoImg,
                (nemoWidth, nemoHeight)), (nemox, nemoy))

        displayCoins(round(coins), displayWidth, displayHeight)

        buttonWidth = displayWidth//8
        buttonHeight = displayHeight//12

        if 0 <= mouse[0] <= buttonWidth and 0 <= mouse[1] <= buttonHeight:
            gameDisplay.blit(pygame.transform.scale(
                backButtonImg2, (buttonWidth, buttonHeight)), (0, 0))
            if click[0] == 1:
                time.sleep(0.1)
                game_loop(True, displayWidth, displayHeight, 0, coins, upgradeSpeed)

        else:
            gameDisplay.blit(pygame.transform.scale(
                backButtonImg1, (buttonWidth, buttonHeight)), (0, 0))

        pygame.display.update()
        clock.tick(FPS)

###############################################################################

def gameShop(displayWidth, displayHeight, coins, c, upgradeSpeed):

    shop = True

    while shop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    time.sleep(0.1)
                    game_loop(True, displayWidth, displayHeight, 0, coins, upgradeSpeed)
            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

        gameDisplay.blit(pygame.transform.scale(
<<<<<<< HEAD
            bgs[(c%75)//25], (displayWidth, displayHeight)), (0, 0))
=======
            bgImg, (displayWidth, displayHeight)), (0, 0))
>>>>>>> 475b4d8 (fix_some_bugs)

        displayCoins(round(coins), displayWidth, displayHeight)

        nemoWidth = displayWidth//4
        nemoHeight = nemoWidth//2
        nemox = displayWidth//2 - nemoWidth//2
        nemoy = displayHeight//3

        buttonWidth = displayWidth//8
        buttonHeight = displayHeight//12
        upgradeButtonWidth = round(displayWidth/3.8)
        upgradex = displayWidth//2 - upgradeButtonWidth//2
        upgradey = round(displayHeight/1.5)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        c += 1

        gameDisplay.blit(pygame.transform.scale(nemoImgs[(c%60)//8],
                (nemoWidth, nemoHeight)), (nemox, nemoy))

        if 0 <= mouse[0] <= buttonWidth and 0 <= mouse[1] <= buttonHeight:
            gameDisplay.blit(pygame.transform.scale(
                backButtonImg2, (buttonWidth, buttonHeight)), (0, 0))
            if coins >= 1000:
                gameDisplay.blit(pygame.transform.scale(
                    upgradeButtonImg1, (upgradeButtonWidth, buttonHeight)),
                        (upgradex, upgradey))
            if coins < 1000:
                gameDisplay.blit(pygame.transform.scale(
                    upgradeButtonImg3, (upgradeButtonWidth, buttonHeight)),
                        (upgradex, upgradey))
            if click[0] == 1:
                time.sleep(0.2)
                game_loop(True, displayWidth, displayHeight, 0, coins, upgradeSpeed)

        elif upgradex <= mouse[0] <= (upgradex + upgradeButtonWidth) and upgradey <= mouse[1] <= (upgradey + buttonHeight):
            gameDisplay.blit(pygame.transform.scale(
                backButtonImg1, (buttonWidth, buttonHeight)), (0, 0))
            if coins >= 1000:
                gameDisplay.blit(pygame.transform.scale(
                    upgradeButtonImg2, (upgradeButtonWidth, buttonHeight)),
                        (upgradex, upgradey))
            if coins < 1000:
                gameDisplay.blit(pygame.transform.scale(
                    upgradeButtonImg3, (upgradeButtonWidth, buttonHeight)),
                        (upgradex, upgradey))
            if click[0] == 1 and coins >= 1000:
                time.sleep(0.2)
                coins -= 1000
                upgradeSpeed += 1
                c += 10

        else:
            gameDisplay.blit(pygame.transform.scale(
                backButtonImg1, (buttonWidth, buttonHeight)), (0, 0))
            if coins >= 1000:
                gameDisplay.blit(pygame.transform.scale(
                    upgradeButtonImg1, (upgradeButtonWidth, buttonHeight)),
                        (upgradex, upgradey))
            if coins < 1000:
                gameDisplay.blit(pygame.transform.scale(
                    upgradeButtonImg3, (upgradeButtonWidth, buttonHeight)),
                        (upgradex, upgradey))


        pygame.display.update()
        clock.tick(FPS)

###############################################################################

def game_loop(intro, displayWidth, displayHeight, score, coins, upgradeSpeed):

    pygame.mixer.music.play(-1)

    c = 0 # this parameter is for animated objects which stands for count

###############################################################################

    # creating 15 objects of Bubble class
    bubbles = []
    for i in range(15):
        bubbles += [Bubble(displayWidth,displayHeight)]

###############################################################################

    preysImg = [blackFishImg, redFishImg,yellowFishImg, tunaFishImg, angelFishImg]*2
    eatPreys = [False]*10
    # creating 10 objects of PreyFish class
    preyFish = []
    for i in range(10):
        preyFish += [PreyFish(displayWidth,displayHeight,preysImg[i],eatPreys[i])]

###############################################################################

    caught = [False]*8
    sharksImg = [shark1Img, shark2Img, shark3Img, shark4Img]*2
    # creating 8 objects of Sharks class
    sharks = []
    for i in range(8):
        sharks += [Sharks(displayWidth,displayHeight,sharksImg[i],caught[i])]

###############################################################################

    # creating objects of SmartShark and GoldFish classes, one each
    goldFish = GoldFish(False,displayWidth,displayHeight,c)
    smartShark = SmartShark(displayWidth,displayHeight,c)

###############################################################################

    # initializing parameters for out charahcter Nemo
    nemoWidth = round(displayWidth/12)
    nemoHeight = round(nemoWidth/2)
    nemox = (displayWidth * (0.5))
    nemoy = (displayHeight * (0.5))
    nemoMovex = 0
    nemoMovey = 0
    viscosity = 0
    momentumx = 0
    momentumy = 0
    moveUp = False
    moveLeft = False
    flip = False
    gameExit = False

    gameIntro(displayWidth, displayHeight, c,  coins, intro, upgradeSpeed)

    while not gameExit:

        # calulating speed of Nemo based on water viscosity, displayWidth and speed upgrade
        nemoSpeed = displayWidth/200 - viscosity + upgradeSpeed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.VIDEORESIZE:
                displayWidth = event.w
                displayHeight = event.h

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    nemoMovex = -nemoSpeed
                    flip = True
                elif event.key == pygame.K_RIGHT:
                    nemoMovex = nemoSpeed
                    flip = False
                elif event.key == pygame.K_UP:
                    nemoMovey = -nemoSpeed
                elif event.key == pygame.K_DOWN:
                    nemoMovey = nemoSpeed
                elif event.key == pygame.K_p:
                    gamePause(displayWidth, displayHeight, score,
                        coins, c, upgradeSpeed)
                elif event.key == pygame.K_q:
                    score += 100
                    coins += 100
                elif event.key == pygame.K_w:
                    score -= 100

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    nemoMovex = 0
                    momentumx = -nemoSpeed/1.5
                    moveLeft = True
                if event.key == pygame.K_RIGHT:
                    nemoMovex = 0
                    momentumx = nemoSpeed/1.5
                    moveLeft = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    nemoMovey = 0
                    momentumy = -nemoSpeed/1.5
                    moveUp = True
                if event.key == pygame.K_DOWN:
                    nemoMovey = 0
                    momentumy = nemoSpeed/1.5
                    moveUp = False

        nemox += (nemoMovex)
        nemoy += (nemoMovey)


        # objects in real life dont come to rest instantly they gradually slow down
        if moveLeft == False:
            nemox += momentumx
        if moveUp == False:
            nemoy += momentumy
        if moveLeft == True:
            nemox += momentumx
        if moveUp == True:
            nemoy += momentumy

        if momentumx > 0 and moveLeft == False:
            momentumx -= 0.1
        if momentumy > 0 and moveUp == False:
            momentumy -= 0.1
        if momentumx < 0 and moveLeft == True:
            momentumx += 0.1
        if momentumy < 0 and moveUp == True:
            momentumy += 0.1

        score += 0.01

<<<<<<< HEAD
        gameDisplay.blit(pygame.transform.scale(bgs[(c%75)//25],
=======
        gameDisplay.blit(pygame.transform.scale(bgImg,
>>>>>>> 475b4d8 (fix_some_bugs)
            (displayWidth, displayHeight)), (0, 0))

###############################################################################

        for i in range(15):
            bubbles[i].bubbleUpdate(displayWidth,displayHeight)

###############################################################################

        for i in range(10):
            preyFish[i].preysUpdate(displayWidth,displayHeight,eatPreys[i])
            eatPreys[i] = preyFish[i].eatPreys

###############################################################################

        for i in range(8):
            sharks[i].sharksUpdate(displayWidth,displayHeight)

##############################################################################

        smartShark.smartSharkUpdate(displayWidth, displayHeight)
        goldFish.goldFishUpdate(displayWidth,displayHeight)

###############################################################################

        # Nemo gains score as it eats other fish so his size gradient is the function of score
        increaseWidth = round(score//10)
        increaseHeight = round(increaseWidth/2)
        nemoWidth = round(displayWidth/12) + increaseWidth
        nemoHeight = round(displayWidth/12)//2 + increaseHeight
        # as size increases viscosity increases
        viscosity = increaseWidth/50

        Nemo(nemox, nemoy, nemoWidth, nemoHeight, flip, c)

        if nemox > displayWidth:
            nemox = -nemoWidth

        if nemox < -nemoWidth:
            nemox = displayWidth

        if nemoy > displayHeight:
            nemoy = -nemoHeight

        if nemoy < -nemoHeight:
            nemoy = displayHeight

###############################################################################

        # goldfish AI, which tracks the distance between itself and nemo
        # if nemo is close, goldfish adjusts its y location accordingly to escape
        if ((nemox + nemoWidth - goldFish.x)**(2) + (nemoy + nemoHeight/2 - goldFish.y -
            goldFish.goldFishHeight/2)**(2))**(1/2) <= displayWidth//4:
            if (goldFish.y + goldFish.goldFishHeight/2) >= (nemoy + goldFish.goldFishHeight/2):
                goldFish.y += (round(displayHeight/150, 2) + upgradeSpeed)
                goldFish.x -= round(displayWidth/1000, 2)
            else:
                goldFish.y -= (round(displayHeight/150, 2) + upgradeSpeed)
                goldFish.x -= round(displayWidth/1000, 2)

###############################################################################

        # smartshark AI, which tracks the distance between itself and nemo
        # if nemo is close, smartshark adjusts its y location accordingly to chase nemo
        if ((nemox + nemoWidth - smartShark.x)**(2) + (nemoy + nemoHeight/2 - smartShark.y -
            smartShark.smartSharkHeight/2)**(2))**(1/2) <= displayWidth//2:
            if (smartShark.y + smartShark.smartSharkHeight/2) >= (nemoy + nemoHeight/2):
                smartShark.y -= (round(displayHeight/240, 2) + upgradeSpeed)
            else:
                smartShark.y += (round(displayHeight/240, 2) + upgradeSpeed)

###############################################################################

        displayScore(round(score), displayWidth, displayHeight)

        displayCoins(round(coins), displayWidth, displayHeight)

        pygame.display.update()

        c += 1

        smartShark.c = c
        goldFish.c = c

        clock.tick(FPS)

###############################################################################

        # converting images into combinations of zeros and ones
        # 1 stands for color 0 stands for no color(transparent)
        # in other words we create masks of each object
        # that way we can have pixel perfect collisions
        if flip == False:
            nemoImg1 = pygame.transform.scale(nemoImgs[(c%60)//8], (nemoWidth, nemoHeight))
            nemoImg2 = nemoImg1.convert_alpha()
            nemoMask = pygame.mask.from_surface(nemoImg2)
<<<<<<< HEAD

        if flip == True:
=======
        else:
>>>>>>> 475b4d8 (fix_some_bugs)
            nemoImg0 = pygame.transform.flip(nemoImgs[(c%60)//8], True, False)
            nemoImg1 = pygame.transform.scale(nemoImg0, (nemoWidth, nemoHeight))
            nemoImg2 = nemoImg1.convert_alpha()
            nemoMask = pygame.mask.from_surface(nemoImg2)

        smartSharkImg1 = pygame.transform.scale(smartSharkImgs[(c%60)//8],
            (smartShark.smartSharkWidth, smartShark.smartSharkHeight))
        smartSharkImg2 = smartSharkImg1.convert_alpha()
        smartSharkMask = pygame.mask.from_surface(smartSharkImg2)

        goldFishImg1 = pygame.transform.scale(goldFishImgs[(c%60)//8],
            (goldFish.goldFishWidth,goldFish.goldFishHeight))
        goldFishImg2 = goldFishImg1.convert_alpha()
<<<<<<< HEAD
        goldFishMask = nemoMask = pygame.mask.from_surface(goldFishImg2)
=======
        goldFishMask = pygame.mask.from_surface(goldFishImg2)
>>>>>>> 475b4d8 (fix_some_bugs)

###############################################################################

        # offsets are basically checking if rectangles of objects overlap
        # if so they we start checking for pixels
<<<<<<< HEAD
        offset1 = (round(nemox + increaseWidth - smartShark.x),round(nemoy +
            increaseHeight - smartShark.y))
=======
        offset1 = (round(nemox - smartShark.x),round(nemoy - smartShark.y))

>>>>>>> 475b4d8 (fix_some_bugs)
        collision1 = smartSharkMask.overlap(nemoMask, offset1)

        if collision1:
            eatSound.play()
            crash(displayWidth, displayHeight, score, coins, c, upgradeSpeed)

<<<<<<< HEAD
        offset2 = (round(nemox + increaseWidth - goldFish.x),round(nemoy +
            increaseHeight - goldFish.y))
=======
        offset2 = (round(nemox - goldFish.x),round(nemoy - goldFish.y))
>>>>>>> 475b4d8 (fix_some_bugs)
        collision2 = goldFishMask.overlap(nemoMask, offset2)

        if goldFish.eat == False:
            if collision2:
                eatSound.play()
                coins += 100
                score += 100
                goldFish.eat = True

###############################################################################

        preysImg1 = []
        preysMasks = []
        offset3 = []
        collision3 = []

        sharksImg1 = []
        sharksMasks = []
        offsetSharks = []
        sharkCollisions = []

        for preyImg in preysImg:
            i = 0
            preysImg1 += [pygame.transform.scale(preyImg,
                (preyFish[i].preyFishWidth, preyFish[i].preyFishHeight))]
            if preyFish[i].randSide == 0:
                preysImg1[i] = preysImg1[i].convert_alpha()
            if  preyFish[i].randSide == 1:
                preysImg1[i] = pygame.transform.flip(preysImg1[i], True, False)
                preysImg1[i] = preysImg1[i].convert_alpha()
            preysMasks += [pygame.mask.from_surface(preysImg1[i])]
            i += 1

        for i in range(10):
            offset3 += [(round(nemox  - preyFish[i].x),
                         round(nemoy  - preyFish[i].y))]
            collision3 += [preysMasks[i].overlap(nemoMask, offset3[i])]

        for i in range(10):
            if collision3[i] != None and eatPreys[i] == False:
                biteSound.play()
                eatPreys[i] = True
                score += preyFish[i].preyFishWidth/15
                coins += 1

<<<<<<< HEAD
        for sharkImg in sharksImg:
            i = 0
=======
        for i, sharkImg in enumerate(sharksImg):
>>>>>>> 475b4d8 (fix_some_bugs)
            sharksImg1 += [pygame.transform.scale(
                sharkImg, (sharks[i].sharksWidth, sharks[i].sharksHeight))]
            if sharks[i].randSide == 0:
                sharksImg1[i] = sharksImg1[i].convert_alpha()
            if sharks[i].randSide == 1:
                sharksImg1[i] = pygame.transform.flip(sharksImg1[i], True, False)
                sharksImg1[i] = sharksImg1[i].convert_alpha()
            sharksMasks += [pygame.mask.from_surface(sharksImg1[i])]
<<<<<<< HEAD
            i += 1

        for i in range(8):
            offsetSharks += [(round(nemox + increaseWidth - sharks[i].x),
                              round(nemoy + increaseHeight - sharks[i].y))]
=======

        for i in range(8):
            offsetSharks += [(round(nemox - sharks[i].x),
                              round(nemoy + - sharks[i].y))]
>>>>>>> 475b4d8 (fix_some_bugs)
            sharkCollisions += [sharksMasks[i]
                                .overlap(nemoMask, offsetSharks[i])]

        for i in range(8):
            if sharkCollisions[i] and caught[i] == False:
                eatSound.play()
                crash(displayWidth, displayHeight, score, coins, c, upgradeSpeed)
<<<<<<< HEAD
=======
        
        pygame.display.update()
>>>>>>> 475b4d8 (fix_some_bugs)

###############################################################################

game_loop(True, displayWidth, displayHeight, score, coins, upgradeSpeed)

pygame.quit()

quit()