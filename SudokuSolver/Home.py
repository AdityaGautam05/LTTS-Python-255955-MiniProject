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
    solveText = smallfont.render('Solve', True, color)
    solveTextHigh = bigfont.render('Solve', True, (0, 0, 255))
    playText = smallfont.render('Play', True, color)
    playTextHigh = bigfont.render('Play', True, (0, 0, 255))

    # boundaries for button
    # [up_width,lo_width,up_height,lo_height]
    playBound = {
        'up_width': 230,
        'lo_width': 293,
        'up_height': 216,
        'lo_height': 253
    }
    solveBound = {
        'up_width': 218,
        'lo_width': 299,
        'up_height': 294,
        'lo_height': 321
    }

    # Getting logo image
    logo = pygame.image.load("./images/SudokuLogo.png").convert()

    while True:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                print(mouse)
                if playBound['up_width'] <= mouse[0] <= playBound['lo_width'] and playBound['up_height'] <= mouse[1] <= playBound['lo_height']:
                    return 2
                if solveBound['up_width'] <= mouse[0] <= solveBound['lo_width'] and solveBound['up_height'] <= mouse[1] <= solveBound['lo_height']:
                    return 4

        # fills the screen with a color
        screen.fill((40, 40, 40))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # hover over play button
        if playBound['up_width'] <= mouse[0] <= playBound['lo_width'] and playBound['up_height'] <= mouse[1] <= playBound['lo_height']:
            screen.blit(playTextHigh, (232, 217))

        else:
            screen.blit(playText, (232, 217))

        # hover over solve button
        if solveBound['up_width'] <= mouse[0] <= solveBound['lo_width'] and solveBound['up_height'] <= mouse[1] <= solveBound['lo_height']:
            screen.blit(solveTextHigh, (223, 295))

        else:
            screen.blit(solveText, (223, 295))

        # superimposing logo image into screen
        screen.blit(logo, (65, 80))

        # updates the frames of the game
        pygame.display.update()


# print(main())
