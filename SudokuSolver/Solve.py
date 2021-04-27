# GUI.py
# RUN THIS FILE
import pygame
from solver import solve, valid
import time
from new_board import genGrid
pygame.font.init()


class Grid:

    board = [[0 for i in range(9)] for j in range(9)]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height)
                       for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = self.board
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(
            self.cols)] for i in range(self.rows)]

    def place(self, val):
        print("place called")
        row, col = self.selected
        # if self.cubes[row][col].value == 0:
        self.cubes[row][col].set(val)
        self.update_model()

        if valid(self.model, val, (row, col)) and solve(self.model):
            self.cubes[row][col].set_temp(0)
            self.update_model()
            return True
        else:
            self.cubes[row][col].set(0)
            self.cubes[row][col].set_temp(0)
            self.update_model()
            return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (200, 200, 200), (0, i*gap),
                             (self.width, i*gap), thick)
            pygame.draw.line(win, (200, 200, 200), (i * gap, 0),
                             (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    # ----------------------
    def re_init(self):
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height)
                       for j in range(self.cols)] for i in range(self.rows)]

    def getSol(self):
        print("getSol called")
        self.board = self.model
        solve(self.board)
        for r in self.model:
            print(r)
        self.re_init()


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("corbel", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0:  # and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        if not(self.value == 0):
            text = fnt.render(str(self.value), 1, (200, 200, 200))
            win.blit(text, (x + (gap/2 - text.get_width()/2),
                     y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_window(win, board, time, strikes):
    win.fill((40, 40, 40))
    # Draw time
    # fnt = pygame.font.SysFont("corbel", 40)
    # text = fnt.render("Time: " + format_time(time), 1, (0, 0, 0))
    # win.blit(text, (540 - 160, 560))

    # Draw Strikes
    # text = fnt.render("X " * strikes, 1, (255, 0, 0))
    # win.blit(text, (20, 560))

    # Draw grid and board
    board.draw(win)


def format_time(secs):
    sec = secs % 60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0

    # defining a font
    font = pygame.font.SysFont('Corbel', 25, True)

    # buttons
    solveText = font.render('Solve', True, (200, 200, 200))
    solveTextHigh = font.render('Solve', True, (0, 0, 255))
    backText = font.render('Back', True, (200, 200, 200))
    backTextHigh = font.render('Back', True, (0, 0, 255))

    # boundaries for button
    # [up_width,lo_width,up_height,lo_height]
    solveBound = {
        'up_width': 16,
        'lo_width': 78,
        'up_height': 561,
        'lo_height': 585
    }
    backBound = {
        'up_width': 469,
        'lo_width': 525,
        'up_height': 561,
        'lo_height': 585
    }

    while run:
        pos = pygame.mouse.get_pos()
        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # run = False
                return 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.getSol()
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                # print(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None
                elif backBound['up_width'] <= pos[0] <= backBound['lo_width'] and backBound['up_height'] <= pos[1] <= backBound['lo_height']:
                    print('go back to homeScreen')
                    return 1
                elif solveBound['up_width'] <= pos[0] <= solveBound['lo_width'] and solveBound['up_height'] <= pos[1] <= solveBound['lo_height']:
                    board.getSol()

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)

        # hover over back button
        if backBound['up_width'] <= pos[0] <= backBound['lo_width'] and backBound['up_height'] <= pos[1] <= backBound['lo_height']:
            win.blit(backTextHigh, (470, 561))

        else:
            win.blit(backText, (470, 561))

        # hover over solve button
        if solveBound['up_width'] <= pos[0] <= solveBound['lo_width'] and solveBound['up_height'] <= pos[1] <= solveBound['lo_height']:
            win.blit(solveTextHigh, (17, 561))

        else:
            win.blit(solveText, (17, 561))

        pygame.display.update()
