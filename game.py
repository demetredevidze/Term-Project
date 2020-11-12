import pygame
import random
import time
from pygame import mixer


###############################################################################


pygame.init()


displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.RESIZABLE)
pygame.display.set_caption("Fish Nemo")
clock = pygame.time.Clock()


bg = pygame.image.load("ocean.jpg")
fishImg = pygame.image.load("nemo.png")
shark1Img = pygame.image.load("shark1.png")
shark2Img = pygame.image.load("shark2.png")
shark3Img = pygame.image.load("shark3.png")
shark4Img = pygame.image.load("shark4.png")
sharkSmartImg = pygame.image.load("sharksmart.png")
bubbleLargeImg = pygame.image.load("bubbleLarge.png")
bubbleMediumImg = pygame.image.load("bubbleMedium.png")
bubbleSmallImg = pygame.image.load("bubbleSmall.png")
goldFishImg = pygame.image.load("goldfish.png")
blackFishImg = pygame.image.load("blackfish.png")
redFishImg = pygame.image.load("redfish.png")
yellowFishImg = pygame.image.load("yellowfish.png")
tunaFishImg = pygame.image.load("tunafish.png")
angelFishImg = pygame.image.load("angelfish.png")
buttonImg1 = pygame.image.load("startButton1.png")
buttonImg2 = pygame.image.load("startButton2.png")
mixer.music.load("waterSound.mp3")


###############################################################################


bubbleLargeWidth = 18
bubbleLargeHeight = 18

bubbleMediumWidth = 12
bubbleMediumHeight = 12

bubbleSmallWidth = 6
bubbleSmallHeight = 6

startButtonWidth = 200
startButtonHeight = 50

fishWidth = round(displayWidth/6)
fishHeight = round(displayHeight/9)

goldFishWidth = round(displayWidth/8)
goldFishHeight = round(displayHeight/12)

preyFishWidth = round(displayWidth/11)
preyFishHeight = round(displayHeight/13)


###############################################################################


def shark1(x, y, shark1Width, shark1Height):
    gameDisplay.blit(pygame.transform.scale(shark1Img, (shark1Width, shark1Height)), (x,y))

def shark2(x, y, shark2Width, shark2Height):
    gameDisplay.blit(pygame.transform.scale(shark2Img, (shark2Width, shark2Height)), (x,y))

def shark3(x, y, shark3Width, shark3Height):
    gameDisplay.blit(pygame.transform.scale(shark3Img, (shark3Width, shark3Height)), (x,y))

def shark4(x, y, shark4Width, shark4Height):
    gameDisplay.blit(pygame.transform.scale(shark4Img, (shark4Width, shark4Height)), (x,y))

def sharkSmart(x, y, sharkSmartWidth, sharkSmartHeight):
    gameDisplay.blit(pygame.transform.scale(sharkSmartImg, (sharkSmartWidth, sharkSmartHeight)), (x,y))


###############################################################################


def bubbleLarge(x, y):
    gameDisplay.blit(bubbleLargeImg, (x,y))

def bubbleMedium(x, y):
    gameDisplay.blit(bubbleMediumImg, (x,y))

def bubbleSmall(x, y):
    gameDisplay.blit(bubbleSmallImg, (x,y))


###############################################################################


def fish(x, y, increaseWidth=0, increaseHeight=0):
    gameDisplay.blit(pygame.transform.scale(fishImg, (fishWidth+increaseWidth, fishHeight+increaseHeight)), (x,y))

def goldFish(x, y):
    gameDisplay.blit(pygame.transform.scale(goldFishImg, (goldFishWidth, goldFishHeight)), (x,y))

def blackFish(x, y):
    gameDisplay.blit(pygame.transform.scale(blackFishImg, (preyFishWidth, preyFishHeight)), (x,y))

def redFish(x, y):
    gameDisplay.blit(pygame.transform.scale(redFishImg, (preyFishWidth, preyFishHeight)), (x,y))

def yellowFish(x, y):
    gameDisplay.blit(pygame.transform.scale(yellowFishImg, (preyFishWidth, preyFishHeight)), (x,y))

def angelFish(x, y):
    gameDisplay.blit(pygame.transform.scale(angelFishImg, (preyFishWidth, preyFishHeight)), (x,y))

def tunaFish(x, y):
    gameDisplay.blit(pygame.transform.scale(tunaFishImg, (preyFishWidth, preyFishHeight)), (x,y))




###############################################################################


def gameIntro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()

        gameDisplay.blit(bg, (0,0))
        largeText = pygame.font.Font("freesansbold.ttf", 50)
        TextSurf, TextRect = text_objects("Welcome to Fish Nemo", largeText)
        TextRect.center = ((displayWidth//2),(displayHeight//2))
        gameDisplay.blit(TextSurf, TextRect)

        click = pygame.mouse.get_pressed()


        if 300 <= mouse[0] <= (300+startButtonWidth) and 400 <= mouse[1] <= (400+startButtonHeight):
            gameDisplay.blit(buttonImg2, (300,400))
            if click[0] == 1:
                game_loop()
        else:
            gameDisplay.blit(buttonImg1, (300,400))




        pygame.display.update()
        clock.tick(60)


def displayScore(score):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Your Score : " +str(score), True, white)
    gameDisplay.blit(text, (20,15))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("Arial", 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width//2)(display_height//2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display("You Crashed")


###############################################################################


def game_loop():

    shark1Width = random.randint(280,320)
    shark1Height = round(shark1Width/2)

    shark2Width = random.randint(280,320)
    shark2Height = round(shark2Width/2)

    shark3Width = random.randint(280,320)
    shark3Height = round(shark3Width/2)

    shark4Width = random.randint(280,320)
    shark4Height = round(shark4Width/2)

    sharkSmartWidth = random.randint(280,320)
    sharkSmartHeight = round(sharkSmartWidth/2)

    pygame.mixer.music.play(-1)


###############################################################################


    bubble1LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
    bubble1LargeStarty = displayHeight+bubbleLargeHeight
    bubble1LargeSpeed = random.randint(3,4)

    bubble2LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
    bubble2LargeStarty = displayHeight+bubbleLargeHeight
    bubble2LargeSpeed = random.randint(3,4)

    bubble3LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
    bubble3LargeStarty = displayHeight+bubbleLargeHeight
    bubble3LargeSpeed = random.randint(3,4)


    bubble1MediumStartx = random.randint(0, displayWidth-bubbleMediumWidth)
    bubble1MediumStarty = displayHeight+bubbleMediumHeight
    bubble1MediumSpeed = random.randint(2,3)

    bubble2MediumStartx = random.randint(0, displayWidth-bubbleMediumWidth)
    bubble2MediumStarty = displayHeight+bubbleMediumHeight
    bubble2MediumSpeed = random.randint(2,3)

    bubble3MediumStartx = random.randint(0, displayWidth-bubbleMediumWidth)
    bubble3MediumStarty = displayHeight+bubbleMediumHeight
    bubble3MediumSpeed = random.randint(2,3)


    bubble1SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
    bubble1SmallStarty = displayHeight+bubbleSmallHeight
    bubble1SmallSpeed = random.randint(1,2)

    bubble2SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
    bubble2SmallStarty = displayHeight+bubbleSmallHeight
    bubble2SmallSpeed = random.randint(1,2)

    bubble3SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
    bubble3SmallStarty = displayHeight+bubbleSmallHeight
    bubble3SmallSpeed = random.randint(1,2)


###############################################################################


    shark1Starty = random.randint(-shark1Height, displayHeight)
    shark1Speed = random.randint(3,10)
    shark1Startx = displayWidth + shark1Width

    shark2Starty = random.randint(-shark2Height, displayHeight)
    shark2Speed = random.randint(3,10)
    shark2Startx = displayWidth + shark2Width

    shark3Starty = random.randint(-shark3Height, displayHeight)
    shark3Speed = random.randint(3,10)
    shark3Startx = displayWidth + shark3Width

    shark4Starty = random.randint(-shark4Height, displayHeight)
    shark4Speed = random.randint(3,10)
    shark4Startx = displayWidth + shark4Width

    sharkSmartStarty = random.randint(-sharkSmartHeight, displayHeight)
    sharkSmartSpeed = random.randint(3,8)
    sharkSmartStartx = displayWidth + sharkSmartWidth


###############################################################################


    goldFishStarty = random.randint(-goldFishHeight, displayHeight)
    goldFishSpeed = random.randint(8,12)
    goldFishStartx = displayWidth + goldFishWidth


    blackFishStarty = random.randint(-preyFishHeight, displayHeight)
    blackFishSpeed = random.randint(4,10)
    blackFishStartx = displayWidth + preyFishWidth


    redFishStarty = random.randint(-preyFishHeight, displayHeight)
    redFishSpeed = random.randint(4,10)
    redFishStartx = displayWidth + preyFishWidth


    yellowFishStarty = random.randint(-preyFishHeight, displayHeight)
    yellowFishSpeed = random.randint(4,10)
    yellowFishStartx = displayWidth + preyFishWidth


    angelFishStarty = random.randint(-preyFishHeight, displayHeight)
    angelFishSpeed = random.randint(4,10)
    angelFishStartx = displayWidth + preyFishWidth

    tunaFishStarty = random.randint(-preyFishHeight, displayHeight)
    tunaFishSpeed = random.randint(4,10)
    tunaFishStartx = displayWidth + preyFishWidth


###############################################################################


    x = (displayWidth * (0.5))
    y = (displayHeight * (0.5))

    xMove = 0
    yMove = 0

    score = 0

    gameExit = False

    while not gameExit:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xMove = -5
                elif event.key == pygame.K_RIGHT:
                    xMove = 5
                elif event.key == pygame.K_UP:
                    yMove = -5
                elif event.key == pygame.K_DOWN:
                    yMove = 5

            if event.type == pygame.KEYUP:
               if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   xMove = 0

            if event.type == pygame.KEYUP:
               if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                   yMove = 0


        x += xMove
        y += yMove

        gameDisplay.blit(pygame.transform.scale(bg, (displayWidth, displayHeight)), (0,0))


###############################################################################


        bubbleLarge(bubble1LargeStartx, bubble1LargeStarty)
        bubble1LargeStarty -= bubble1LargeSpeed

        bubbleLarge(bubble2LargeStartx, bubble2LargeStarty)
        bubble2LargeStarty -= bubble2LargeSpeed

        bubbleLarge(bubble3LargeStartx, bubble3LargeStarty)
        bubble3LargeStarty -= bubble3LargeSpeed


        if bubble1LargeStarty < -bubbleLargeHeight:
            bubble1LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
            bubble1LargeStarty = displayHeight+bubbleLargeHeight
            bubble1LargeSpeed = random.randint(3,4)

        if bubble2LargeStarty < -bubbleLargeHeight:
            bubble2LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
            bubble2LargeStarty = displayHeight+bubbleLargeHeight
            bubble2LargeSpeed = random.randint(3,4)

        if bubble3LargeStarty < -bubbleLargeHeight:
            bubble3LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
            bubble3LargeStarty = displayHeight+bubbleLargeHeight
            bubble3LargeSpeed = random.randint(3,4)


        bubbleMedium(bubble1MediumStartx, bubble1MediumStarty)
        bubble1MediumStarty -= bubble1MediumSpeed

        bubbleMedium(bubble2MediumStartx, bubble2MediumStarty)
        bubble2MediumStarty -= bubble2MediumSpeed

        bubbleMedium(bubble3MediumStartx, bubble3MediumStarty)
        bubble3MediumStarty -= bubble3MediumSpeed


        if bubble1MediumStarty < -bubbleMediumHeight:
            bubble1MediumStartx = random.randint(0, displayWidth-bubbleLargeWidth)
            bubble1MediumStarty = displayHeight+bubbleLargeHeight
            bubble1MediumSpeed = random.randint(2,3)

        if bubble2MediumStarty < -bubbleMediumHeight:
            bubble2MediumStartx = random.randint(0, displayWidth-bubbleMediumWidth)
            bubble2MediumStarty = displayHeight+bubbleMediumHeight
            bubble2MediumSpeed = random.randint(2,3)

        if bubble3MediumStarty < -bubbleMediumHeight:
            bubble3MediumStartx = random.randint(0, displayWidth-bubbleMediumWidth)
            bubble3MediumStarty = displayHeight+bubbleMediumHeight
            bubble3MediumSpeed = random.randint(2,3)


        bubbleSmall(bubble1SmallStartx, bubble1SmallStarty)
        bubble1SmallStarty -= bubble1SmallSpeed

        bubbleSmall(bubble2SmallStartx, bubble2SmallStarty)
        bubble2SmallStarty -= bubble2SmallSpeed

        bubbleSmall(bubble3SmallStartx, bubble3SmallStarty)
        bubble3SmallStarty -= bubble3SmallSpeed


        if bubble1SmallStarty < -bubbleSmallHeight:
            bubble1SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
            bubble1SmallStarty = displayHeight+bubbleSmallHeight
            bubble1SmallSpeed = random.randint(1,2)

        if bubble2SmallStarty < -bubbleSmallHeight:
            bubble2SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
            bubble2SmallStarty = displayHeight+bubbleSmallHeight
            bubble2SmallSpeed = random.randint(1,2)

        if bubble3SmallStarty < -bubbleSmallHeight:
            bubble3SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
            bubble3SmallStarty = displayHeight+bubbleSmallHeight
            bubble3SmallSpeed = random.randint(1,2)


###############################################################################


        shark1(shark1Startx, shark1Starty, shark1Width, shark1Height)
        shark1Startx -= shark1Speed

        shark2(shark2Startx, shark2Starty, shark2Width, shark2Height)
        shark2Startx -= shark2Speed

        shark3(shark3Startx, shark3Starty, shark3Width, shark3Height)
        shark3Startx -= shark3Speed

        shark4(shark4Startx, shark4Starty, shark4Width, shark4Height)
        shark4Startx -= shark4Speed


        if shark1Startx < -shark1Width:
            shark1Starty = random.randint(-shark1Height, displayHeight)
            shark1Speed = random.randint(3,10)
            shark1Startx = displayWidth + shark1Width


        if shark2Startx < -shark2Width:
            shark2Starty = random.randint(-shark2Height, displayHeight)
            shark2Speed = random.randint(3,10)
            shark2Startx = displayWidth + shark2Width


        if shark3Startx < -shark3Width:
            shark3Starty = random.randint(-shark3Height, displayHeight)
            shark3Speed = random.randint(3,10)
            shark3Startx = displayWidth + shark3Width


        if shark4Startx < -shark4Width:
            shark4Starty = random.randint(-shark4Height, displayHeight)
            shark4Speed = random.randint(3,10)
            shark4Startx = displayWidth + shark4Width


###############################################################################


        sharkSmart(sharkSmartStartx, sharkSmartStarty, sharkSmartWidth, sharkSmartHeight)
        sharkSmartStartx -= sharkSmartSpeed

        if sharkSmartStartx < -sharkSmartWidth:
            sharkSmartStarty = random.randint(-sharkSmartHeight, displayHeight)
            sharkSmartSpeed = random.randint(3,8)
            sharkSmartStartx = displayWidth + sharkSmartWidth


###############################################################################


        goldFish(goldFishStartx, goldFishStarty)
        goldFishStartx -= goldFishSpeed

        if goldFishStartx < -goldFishWidth:
            goldFishStarty = random.randint(-goldFishHeight, displayHeight)
            goldFishSpeed = random.randint(8,12)
            goldFishStartx = displayWidth + goldFishWidth

        if goldFishStarty > displayHeight:
            goldFishStarty = -goldFishHeight

        if goldFishStarty < -goldFishHeight:
            goldFishStarty = displayHeight


###############################################################################


        blackFish(blackFishStartx, blackFishStarty)
        blackFishStartx -= blackFishSpeed

        if blackFishStartx < -preyFishWidth:
            blackFishStarty = random.randint(0, displayHeight)
            blackFishSpeed = random.randint(4,10)
            blackFishStartx = displayWidth + preyFishWidth


        yellowFish(yellowFishStartx, yellowFishStarty)
        yellowFishStartx -= yellowFishSpeed

        if yellowFishStartx < -preyFishWidth:
            yellowFishStarty = random.randint(0, displayHeight)
            yellowFishSpeed = random.randint(4,10)
            yellowFishStartx = displayWidth + preyFishWidth


        redFish(redFishStartx, redFishStarty)
        redFishStartx -= redFishSpeed

        if redFishStartx < -preyFishWidth:
            redFishStarty = random.randint(0, displayHeight)
            redFishSpeed = random.randint(4,10)
            redFishStartx = displayWidth + preyFishWidth


        angelFish(angelFishStartx, angelFishStarty)
        angelFishStartx -= angelFishSpeed

        if angelFishStartx < -preyFishWidth:
            angelFishStarty = random.randint(0, displayHeight)
            angelFishSpeed = random.randint(4,10)
            angelFishStartx = displayWidth + preyFishWidth


        tunaFish(tunaFishStartx, tunaFishStarty)
        tunaFishStartx -= tunaFishSpeed

        if tunaFishStartx < -preyFishWidth:
            tunaFishStarty = random.randint(0, displayHeight)
            tunaFishSpeed = random.randint(4,10)
            tunaFishStartx = displayWidth + preyFishWidth


###############################################################################


        increaseWidth = round(score//10)
        increaseHeight = round(increaseWidth/2)

        fish(x,y,increaseWidth,increaseHeight)

        if x > displayWidth:
            x = -fishWidth

        if x < -fishWidth:
            x = displayWidth

        if y > displayHeight:
            y = -fishHeight

        if y < -fishHeight:
            y = displayHeight

        score += 0.05


###############################################################################


        if ((x + fishWidth - goldFishStartx)**(2) + (y + fishHeight/2 - goldFishStarty - goldFishHeight/2)**(2))**(1/2) <= 300:
            if (goldFishStarty + goldFishHeight/2) >= (y + goldFishHeight/2):
                goldFishStarty += 4
            if (goldFishStarty + goldFishHeight/2) < (y + goldFishHeight/2):
                goldFishStarty -= 4


###############################################################################


        if ((x + fishWidth - sharkSmartStartx)**(2) + (y + fishHeight/2 - sharkSmartStarty - sharkSmartHeight/2)**(2))**(1/2) <= 700 and (sharkSmartStartx + sharkSmartWidth) >= x:
            if (sharkSmartStarty + sharkSmartHeight/2) >= (y + fishHeight/2):
                sharkSmartStarty -= 2
            if (sharkSmartStarty + sharkSmartHeight/2) < (y + fishHeight/2):
                sharkSmartStarty += 2


###############################################################################


        displayScore(round(score))

        pygame.display.update()

        clock.tick(60)


gameIntro()

game_loop()

pygame.quit()

quit()
