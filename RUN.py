import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import random

pygame.init()

#############
crash_sound = pygame.mixer.Sound("jutut/sireeni.wav")
#############

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

aleksi_width = 80

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Puolivuosipäivä')
clock = pygame.time.Clock()

pause = False

def loadify_alpha(img):
    return pygame.image.load(img).convert_alpha()

def loadify(img):
    return pygame.image.load(img).convert()

aleksiImg = loadify_alpha('jutut/aleksi.png')
budiImg = loadify_alpha('jutut/budi.png')
maijaImg = loadify_alpha('jutut/poliisiauto.png')
gameIcon = pygame.image.load('jutut/budiIcon.png')

pygame.display.set_icon(gameIcon)


# crash = True

def budilaskuri(count):
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Dänkkilaskuri: " + str(round(count,1)) + " g", True, black)
    gameDisplay.blit(text, (1, 2))

    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Dänkkilaskuri: " + str(round(count,1)) + " g", True, green)
    gameDisplay.blit(text, (0, 0))


def maijat(maijax, maijay, maijaw, maijah):
    gameDisplay.blit(maijaImg, [maijax, maijay, maijaw, maijah])

def budit(budix, budiy, budiw, budih):
    gameDisplay.blit(budiImg, [budix, budiy, budiw, budih])


def aleksi(x, y):
    gameDisplay.blit(aleksiImg, (x, y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def crash():
    ####################################
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = text_objects("Ei vittu kytät!", largeText, black)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("Ei vittu kytät!", largeText, bright_green)
    TextRect.center = ((display_width / 2.01), (display_height / 2.01))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Jatka metskausta...", 100, 450, 225, 50, green, bright_green, game_loop)
        button("Kerro tyttöystävälle...", 400, 450, 250, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def crash2():
    ####################################
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = text_objects("Mut ne hatsit...", largeText, black)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("Mut ne hatsit...", largeText, bright_green)
    TextRect.center = ((display_width / 2.01), (display_height / 2.01))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Jatka metskausta...", 100, 450, 225, 50, green, bright_green, game_loop)
        button("Kerro tyttöystävälle...", 400, 450, 250, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)



def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms", 115)

    TextSurf, TextRect = text_objects("Hatsibreikki", largeText, black)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("Hatsibreikki", largeText, green)
    TextRect.center = ((display_width / 2.01), (display_height / 2.01))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Jatka metskausta!", 50, 450, 200, 50, green, bright_green, unpause)
        button("Oot liian pilvessä jatkamaan, ja kerrot tyttöystävälle...", 270, 450, 520, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(loadify('jutut/piritori_bw.png'), (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 110)
        smallText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = text_objects("Puolivuosipäivä", largeText, black)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Puolivuosipäivä", largeText, green)
        TextRect.center = ((display_width / 2.02), (display_height / 5.05))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Voi ei! Sinulla on puolivuosipäivä", smallText, white)
        TextRect.center = ((display_width / 2), (display_height / 2.5))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("tyttöystäväsi kanssa ja", smallText, white)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("olet hiisannut kaikki hatsit!", smallText, white)
        TextRect.center = ((display_width / 2), (display_height / 1.65))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Voi ei! Sinulla on puolivuosipäivä", smallText, black)
        TextRect.center = ((display_width / 2.005), (display_height / 2.505))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("tyttöystäväsi kanssa ja", smallText, black)
        TextRect.center = ((display_width / 2.005), (display_height / 2.005))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("olet hiisannut kaikki hatsit!", smallText, black)
        TextRect.center = ((display_width / 2.005), (display_height / 1.655))
        gameDisplay.blit(TextSurf, TextRect)

        button("Lähde Piritorille metskaamaan!", 25, 450, 325, 50, green, bright_green, game_loop)
        button("Kerro tyttöystävälle, että hiisasit kaiken", 375, 450, 400, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    ############
    pygame.mixer.stop()
    pygame.mixer.music.load('jutut/muumimusa.wav')
    pygame.mixer.music.play(-1)
    ############
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    maija_startx = random.randrange(0, display_width - 50)
    maija_starty = -400
    maija_speed = 4
    maija_width = maijaImg.get_width()
    maija_height = maijaImg.get_height()

    budi_startx = random.randrange(0, display_width - 20)
    budi_starty = -200
    budi_speed = 4
    budi_width = budiImg.get_width()
    budi_height = budiImg.get_height()

    budiCount = 1

    laskuri = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.blit(loadify('jutut/piritori.png'), (0, 0))

        maijat(maija_startx, maija_starty, maija_width, maija_height)
        budit(budi_startx, budi_starty, budi_width, budi_height)

        maija_starty += maija_speed
        budi_starty += budi_speed
        aleksi(x, y)
        budilaskuri(laskuri)

        if x > display_width - aleksi_width or x < 0:
            crash2()

        if maija_starty > display_height:
            maija_starty = 0 - maija_height
            maija_startx = random.randrange(0, display_width - 50)
            maija_speed += 1

        if y < maija_starty + maija_height - 20:

            if x > maija_startx and x < maija_startx + maija_width or x + aleksi_width - 15 > maija_startx and x + aleksi_width < maija_startx + maija_width:
                pygame.mixer.Sound.play(crash_sound)
                crash()

        if budi_starty > display_height:
            budi_starty = 0 - budi_height
            budi_startx = random.randrange(0, display_width - 20)
            budi_speed += 1

        if y < budi_starty + budi_height:

            if x > budi_startx and x < budi_startx + budi_width or x + aleksi_width > budi_startx and x + aleksi_width < budi_startx + budi_width + (aleksi_width - budi_width):
                laskuri += 0.025

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
