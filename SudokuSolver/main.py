import Home
import Solve
import Levels
import Play

# default screen is Home
screen = 1

while screen <= 4:

    if screen == 1:
        screen = Home.main()
    elif screen == 2:
        lvl = Levels.main()
        if lvl == 5:
            break
        screen = Play.main(lvl)
    elif screen == 4:
        screen = Solve.main()
