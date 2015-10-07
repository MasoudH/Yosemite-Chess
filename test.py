from pygame import *

screen = display.set_mode((1920, 1080))

buttonImage = image.load("Images/button.png") # Button Image

def gameover():
	cover = Surface((880, 880), SRCALPHA)
	draw.rect(cover, (0, 0, 0, 230), (0, 0, 880, 880))
	screen.blit(cover, (520, 100))



running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    gameover()
    
    display.flip()
quit()