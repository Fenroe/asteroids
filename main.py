# this allows us to use code from
# the open-source pygame library
# throughout this file
from pygame import init, display, event, QUIT
from constants import *

def main():
    init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for e in event.get():
            if e.type == QUIT:
                return
        screen.fill("black")
        display.flip()

if __name__ == "__main__":
    main()