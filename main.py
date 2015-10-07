from pygame import *
from chessGame import *

font.init()

mb = 0
cursor = (0, 0)

def fps(screen, clock, color, backgroundColor, location): # finds the frames per second of the program and displays it
    frames = clock.get_fps()
    print(frames)
    clock.tick()

screen = display.set_mode((1920, 1080), FULLSCREEN)
clock = time.Clock()
chess = chessGame()
screen.blit(image.load("Images/yosemite.jpg"), (0, 0))
chess.start(screen, cursor, mb)

running = True
while running:
    myClock = clock.tick()
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
        	if e.key == K_ESCAPE:
        		running = False 
        if e.type == MOUSEBUTTONDOWN:
            mb = mouse.get_pressed()[0]
            cursor = mouse.get_pos()
            chess.main(screen, mb, cursor)
    # fps(screen, clock, (255, 255, 255), (0, 0, 0), (1820, 1050))

    display.flip()
quit()
