# 1 - Import library
import os
import pygame
from pygame.locals import *

path = os.path.abspath(os.path.dirname(__file__))
start_img_path = os.path.abspath(os.path.join(path, 'resources/images', 'start.jpg'))

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load(r'E:\RPI\simple-game\Pygame\game-XO\resources\images\sub.png')
sub = pygame.image.load(r'E:\RPI\simple-game\Pygame\game-XO\resources\images\start.jpg')

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (0,0))
    # screen.blit(sub, (50,50))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 