import pygame
import random
import time
from pygame import mixer

###################################################################################


pygame.init()


displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Fish")
clock = pygame.time.Clock()


bg = pygame.image.load("ocean.jpg")
fishImg = pygame.image.load("nemofish.png")
shark1Size1Img = pygame.image.load("shark1size1.png")
shark2Size1Img = pygame.image.load("shark2size1.png")
shark3Size1Img = pygame.image.load("shark3size1.png")
shark4Size1Img = pygame.image.load("shark4size1.png")
shark5Size1Img = pygame.image.load("shark5size1.png")
bubbleLargeImg = pygame.image.load("bubbleLarge.png")
bubbleMediumImg = pygame.image.load("bubbleMedium.png")
bubbleSmallImg = pygame.image.load("bubbleSmall.png")
buttonImg1 = pygame.image.load("startButton1.png")
buttonImg2 = pygame.image.load("startButton2.png")
waterSound = mixer.music.load("waterSound.mp3")

###################################################################################


shark1Size1Width = 300
shark1Size1Height = 130

shark2Size1Width = 300
shark2Size1Height = 136

shark3Size1Width = 300
shark3Size1Height = 122

shark4Size1Width = 300
shark4Size1Height = 122

shark5Size1Width = 300
shark5Size1Height = 145

bubbleLargeWidth = 18
bubbleLargeHeight = 18

bubbleMediumWidth = 12
bubbleMediumHeight = 12

bubbleSmallWidth = 6
bubbleSmallHeight = 6

startButtonWidth = 200
startButtonHeight = 50

fishWidth = 170
fishHeight = 94


###################################################################################


def shark1Size1(x, y):
    gameDisplay.blit(shark1Size1Img, (x,y))

def shark2Size1(x, y):
    gameDisplay.blit(shark2Size1Img, (x,y))

def shark3Size1(x, y):
    gameDisplay.blit(shark3Size1Img, (x,y))

def shark4Size1(x, y):
    gameDisplay.blit(shark4Size1Img, (x,y))

def shark5Size1(x, y):
    gameDisplay.blit(shark5Size1Img, (x,y))


###################################################################################


def bubbleLarge(x, y):
    gameDisplay.blit(bubbleLargeImg, (x,y))

def bubbleMedium(x, y):
    gameDisplay.blit(bubbleMediumImg, (x,y))

def bubbleSmall(x, y):
    gameDisplay.blit(bubbleSmallImg, (x,y))


###################################################################################


def fish(x, y):
    gameDisplay.blit(fishImg,(x,y))


###################################################################################


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
        TextSurf, TextRect = text_objects("Welcome to Save Nemo", largeText)
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


###################################################################################


def game_loop():

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


###################################################################################


    shark1Size1Starty = random.randint(0, displayHeight)
    shark1Size1Speed = random.randint(3,10)
    shark1Size1Startx = displayWidth + shark1Size1Width

    shark2Size1Starty = random.randint(0, displayHeight)
    shark2Size1Speed = random.randint(3,10)
    shark2Size1Startx = displayWidth + shark2Size1Width

    shark3Size1Starty = random.randint(0, displayHeight)
    shark3Size1Speed = random.randint(3,10)
    shark3Size1Startx = displayWidth + shark3Size1Width

    shark4Size1Starty = random.randint(0, displayHeight)
    shark4Size1Speed = random.randint(3,10)
    shark4Size1Startx = displayWidth + shark4Size1Width

    shark5Size1Starty = random.randint(0, displayHeight)
    shark5Size1Speed = random.randint(3,10)
    shark5Size1Startx = displayWidth + shark5Size1Width


###################################################################################

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

        gameDisplay.blit(bg, (0, 0))


#######################################################################################################


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
            score += random.randint(1,2)

        if bubble2LargeStarty < -bubbleLargeHeight:
            bubble2LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
            bubble2LargeStarty = displayHeight+bubbleLargeHeight
            bubble2LargeSpeed = random.randint(3,4)
            score += random.randint(1,2)

        if bubble3LargeStarty < -bubbleLargeHeight:
            bubble3LargeStartx = random.randint(0, displayWidth-bubbleLargeWidth)
            bubble3LargeStarty = displayHeight+bubbleLargeHeight
            bubble3LargeSpeed = random.randint(3,4)
            score += random.randint(1,2)


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
            score += random.randint(2,3)

        if bubble2MediumStarty < -bubbleMediumHeight:
            bubble2MediumStartx = random.randint(0, displayWidth-bubbleMediumWidth)
            bubble2MediumStarty = displayHeight+bubbleMediumHeight
            bubble2MediumSpeed = random.randint(2,3)
            score += random.randint(2,3)

        if bubble3MediumStarty < -bubbleMediumHeight:
            bubble3MediumStartx = random.randint(0, displayWidth-bubbleMediumWidth)
            bubble3MediumStarty = displayHeight+bubbleMediumHeight
            bubble3MediumSpeed = random.randint(2,3)
            score += random.randint(2,3)


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
            score += random.randint(3,4)

        if bubble2SmallStarty < -bubbleSmallHeight:
            bubble2SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
            bubble2SmallStarty = displayHeight+bubbleSmallHeight
            bubble2SmallSpeed = random.randint(1,2)
            score += random.randint(3,4)

        if bubble3SmallStarty < -bubbleSmallHeight:
            bubble3SmallStartx = random.randint(0, displayWidth-bubbleSmallWidth)
            bubble3SmallStarty = displayHeight+bubbleSmallHeight
            bubble3SmallSpeed = random.randint(1,2)
            score += random.randint(3,4)


##############################################################################################


        shark1Size1(shark1Size1Startx, shark1Size1Starty)
        shark1Size1Startx -= shark1Size1Speed

        shark2Size1(shark2Size1Startx, shark2Size1Starty)
        shark2Size1Startx -= shark2Size1Speed

        shark3Size1(shark3Size1Startx, shark3Size1Starty)
        shark3Size1Startx -= shark3Size1Speed

        shark4Size1(shark4Size1Startx, shark4Size1Starty)
        shark4Size1Startx -= shark4Size1Speed

        shark5Size1(shark5Size1Startx, shark5Size1Starty)
        shark5Size1Startx -= shark5Size1Speed


        if shark1Size1Startx < -shark1Size1Width:
            shark1Size1Starty = random.randint(0, displayHeight)
            shark1Size1Speed = random.randint(3,10)
            shark1Size1Startx = displayWidth + shark1Size1Width
            score += 10


        if shark2Size1Startx < -shark2Size1Width:
            shark2Size1Starty = random.randint(0, displayHeight)
            shark2Size1Speed = random.randint(3,10)
            shark2Size1Startx = displayWidth + shark2Size1Width
            score += 10

        if shark3Size1Startx < -shark3Size1Width:
            shark3Size1Starty = random.randint(0, displayHeight)
            shark3Size1Speed = random.randint(3,10)
            shark3Size1Startx = displayWidth + shark3Size1Width
            score += 10

        if shark4Size1Startx < -shark4Size1Width:
            shark4Size1Starty = random.randint(0, displayHeight)
            shark4Size1Speed = random.randint(4,10)
            shark4Size1Startx = displayWidth + shark4Size1Width
            score += 10

        if shark5Size1Startx < -shark3Size1Width:
            shark5Size1Starty = random.randint(0, displayHeight)
            shark5Size1Speed = random.randint(4,10)
            shark5Size1Startx = displayWidth + shark5Size1Width
            score += 10

###################################################################################


        fish(x,y)

        if x > displayWidth:
            x = -fishWidth

        if x < -fishWidth:
            x = displayWidth

        if y > displayHeight:
            y = -fishHeight

        if y < -fishHeight:
            y = displayHeight

        score += 0.05


###################################################################################
        displayScore(round(score))

        pygame.display.update()

        clock.tick(60)



gameIntro()

game_loop()

pygame.quit()

quit()
