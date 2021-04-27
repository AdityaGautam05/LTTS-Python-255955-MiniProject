import pygame
import sys
import os


def main():
    # initializing the constructor
    pygame.init()

    # screen resolution
    res = (540, 600)

    # opens up a window
    screen = pygame.display.set_mode(res)

    # white color
    color = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)

    # stores the width of the
    # screen into a variable
    width = screen.get_width()

    # stores the height of the
    # screen into a variable
    height = screen.get_height()

    # defining a font
    smallfont = pygame.font.SysFont('Corbel', 35)
    bigfont = pygame.font.SysFont('Corbel', 35, True)

    # rendering a text written in
    # this font
    levelOneText = smallfont.render('Easy', True, color)
    levelOneTextHigh = bigfont.render('Easy', True, (0, 0, 255))
    levelTwoText = smallfont.render('Medium', True, color)
    levelTwoTextHigh = bigfont.render('Medium', True, (0, 0, 255))
    levelThreeText = smallfont.render('Hard', True, color)
    levelThreeTextHigh = bigfont.render('Hard', True, (0, 0, 255))

    # boundaries for button
    # [up_width,lo_width,up_height,lo_height]
    levelOneBound = {
        'up_width': 230,
        'lo_width': 336,
        'up_height': 50,
        'lo_height': 100
    }
    levelTwoBound = {
        'up_width': 230,
        'lo_width': 336,
        'up_height': 135,
        'lo_height': 185
    }
    levelThreeBound = {
        'up_width': 230,
        'lo_width': 336,
        'up_height': 210,
        'lo_height': 260
    }

    while True:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                return 5

             # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                print(mouse)
                if levelOneBound['up_width'] <= mouse[0] <= levelOneBound['lo_width'] and levelOneBound['up_height'] <= mouse[1] <= levelOneBound['lo_height']:
                    return 2
                if levelTwoBound['up_width'] <= mouse[0] <= levelTwoBound['lo_width'] and levelTwoBound['up_height'] <= mouse[1] <= levelTwoBound['lo_height']:
                    return 8
                if levelThreeBound['up_width'] <= mouse[0] <= levelThreeBound['lo_width'] and levelThreeBound['up_height'] <= mouse[1] <= levelThreeBound['lo_height']:
                    return 15

        # fills the screen with a color
        screen.fill((40, 40, 40))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # hover over play button
        if levelOneBound['up_width'] <= mouse[0] <= levelOneBound['lo_width'] and levelOneBound['up_height'] <= mouse[1] <= levelOneBound['lo_height']:
            screen.blit(levelOneTextHigh, (232, 66))

        else:
            screen.blit(levelOneText, (232, 66))

        # hover over solve button
        if levelTwoBound['up_width'] <= mouse[0] <= levelTwoBound['lo_width'] and levelTwoBound['up_height'] <= mouse[1] <= levelTwoBound['lo_height']:
            screen.blit(levelTwoTextHigh, (232, 146))

        else:
            screen.blit(levelTwoText, (232, 146))

        if levelThreeBound['up_width'] <= mouse[0] <= levelThreeBound['lo_width'] and levelThreeBound['up_height'] <= mouse[1] <= levelThreeBound['lo_height']:
            screen.blit(levelThreeTextHigh, (232, 236))

        else:
            screen.blit(levelThreeText, (232, 236))

        # updates the frames of the game
        pygame.display.update()


# print(main())
