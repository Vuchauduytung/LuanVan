import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
FPS = 60

class MovableImage(pygame.Surface):
    def __init__(self, image, xpos=0, ypos=0):
        self.image = image
        self.xpos = xpos
        self.ypos = ypos
        self.width =  image.get_width()
        self.height = image.get_height()
        self.selected = False
        self.rect = pygame.Rect(xpos, ypos, image.get_width(), image.get_height())

    def move(self, move):
        self.xpos += move[0]
        self.ypos += move[1]
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

def Transformation(element):
    element = pygame.transform.scale(element,(50,75))

def init():
    global ImageList
    fire = pygame.Surface((50,50))
    fire.fill((255,0,0))
    #fire = pygame.image.load("ElementIcon/fire.png").convert_alpha()
    #Transformation(fire)
    #fire.set_colorkey(BLACK)
    #fire_rect = fire.get_rect()

    earth = pygame.Surface((50,50))
    earth.fill((255,255,0))
    #earth = pygame.image.load("ElementIcon/earth.png").convert_alpha()
    #Transformation(earth)
    #earth.set_colorkey(BLACK)
    #earth_rect = earth.get_rect()

    fire_obj = MovableImage(fire, 408, 450)
    earth_obj = MovableImage(earth, 419,350)

    ImageList =[]
    ImageList.append(fire_obj)
    ImageList.append(earth_obj)

def run():

    global done
    done = False
    while not done:
        check_events()
        update()
        clock.tick(60)      

def check_events():
    global done
    global ImageList

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
            print("User quits the game :(")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                print("Game stopped early by user :( ")

        if event.type == pygame.MOUSEBUTTONDOWN:
            for im in ImageList:
                if im.rect.collidepoint(mouse_pos):
                    im.selected = not im.selected

        if event.type == pygame.MOUSEBUTTONUP:
            for im in ImageList:
                if im.rect.collidepoint(mouse_pos):
                    im.selected = False

        if event.type == pygame.MOUSEMOTION:
            for im in ImageList:
                if im.rect.collidepoint(mouse_pos) and im.selected:
                    xmv = event.rel[0]
                    ymv = event.rel[1]

                    if event.buttons[0]:
                        if xmv < 0:
                            if im.xpos > 0:
                                im.move((xmv,0))

                        elif event.rel[0] > 0:
                            if im.xpos < screen.get_width():
                                im.move((xmv,0))

                        elif event.rel[1] < 0:
                            if im.ypos > 0:
                                im.move((0,ymv))

                        elif event.rel[1] > 0:
                            if im.ypos < screen.get_height():
                                im.move((0,ymv))

def update():
    global ImageList
    screen.fill((255, 255, 255)) #WHITE)

    #Update the screen with drawings
    for im in ImageList:
        screen.blit(im.image, (im.xpos, im.ypos))

    pygame.display.update() 

if __name__=="__main__":
    init()
    run()