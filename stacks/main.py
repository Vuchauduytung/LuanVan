from itertools import cycle
import random
import sys
import pygame
import os
from pygame.locals import *
from modules.SurfaceObject import *
import time
from copy import copy, deepcopy


def main():
    
    path = os.path.abspath(os.path.dirname(__file__))
    images_path = os.path.abspath(os.path.join(path, 'assets', 'sprites'))
    audio_path = os.path.abspath(os.path.join(path, 'assets', 'audio'))
    
    SCREENWIDTH  = 600
    SCREENHEIGHT = 800
    
    transCOLOR = (255, 255, 255)
    SPEED = 0.5

    BLOCK_LIST = [
        images_path + '/block.png'
    ]
    
    BACKGROUNDS_LIST = [
        images_path + '/background.png'
    ]
    
    BOTTOM_LIST = [
        images_path + '/bottom.png'
    ]
    
    IMAGES, SOUNDS = {}, {}
    
    SIZE = {
        'background' : (600, 1600),
        'base' : (600, 100),
        'bottom' : (200, 50),
        'block' : (200, 50),
        'gameover' : (400, 100),
        'message' : (600, 800)
    }
    
    POSITION = {
        'background' : (0, -800),
        'base' : (0, 700),
        'bottom' : (200, 650),
        'block' : (200,600),
        'gameover' : (100, 400),
        'message' : (0, 0)
    }
    
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, 
                                      SCREENHEIGHT))
    pygame.display.set_caption('Stacks')
    
    # game over sprite
    IMAGES['gameover'] = MovableImage(path = images_path + '/wasted.png', 
                                      pos = POSITION['gameover'],
                                      size = SIZE['gameover'],
                                      transCOLOR = transCOLOR)
    
    # message sprite for welcome screen
    IMAGES['message'] = MovableImage(path = images_path + '/message.png', 
                                     pos = POSITION['message'],
                                     size = SIZE['message'],
                                     transCOLOR = transCOLOR)
    
    # base (ground) sprite
    IMAGES['base'] = MovableImage(path = images_path + '/base.png', 
                                  pos = POSITION['base'],
                                  size = SIZE['base'])
    
    SOUNDS['gameover'] = pygame.mixer.Sound(audio_path + '/wasted.mp3')
    
    HIGH_SCORE = 0
    
    while True:
        # select random background sprites
        randBg = random.randint(0, len(BACKGROUNDS_LIST) - 1)
        IMAGES['background'] = MovableImage(path = BACKGROUNDS_LIST[randBg], 
                                            pos = POSITION['background'],
                                            size = SIZE['background'])
        
        # select random block sprites
        randBot = random.randint(0, len(BOTTOM_LIST) - 1)
        IMAGES['bottom'] = MovableImage(path = BOTTOM_LIST[randBot], 
                                        pos = POSITION['bottom'],
                                        size = SIZE['bottom'])
        
        # select random block sprites
        randBlk = random.randint(0, len(BLOCK_LIST) - 1)
        IMAGES['block'] = MovableImage(path = BLOCK_LIST[randBlk], 
                                       pos = POSITION['block'],
                                       size = SIZE['block'],
                                       transCOLOR = transCOLOR)
        
        game_init(SCREEN, IMAGES, POSITION)    
        wait()
        HIGH_SCORE = game_rolling(SCREEN, IMAGES, SPEED, SOUNDS, HIGH_SCORE)
        
def game_init(screen, image, position):
    image['background'].blur(alpha = 255)
    image['base'].blur(alpha = 255)
    image['bottom'].blur(alpha = 255)
    image['message'].blur(alpha = 255)
    image['background'].put(position['background'])
    image['base'].put(position['base'])
    image['bottom'].put(position['bottom'])
    image['message'].put(position['message'])
    screen.blit(image['background'].get_img(), 
                image['background'].get_pos())
    screen.blit(image['base'].get_img(), 
                image['base'].get_pos())
    screen.blit(image['bottom'].get_img(), 
                image['bottom'].get_pos())
    screen.blit(image['message'].get_img(), 
                image['message'].get_pos())
    pygame.display.update()

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
            
def game_rolling(screen, image, speed, sound, high_score):
    V_MAX = 2
    x_ver = V_MAX*speed
    block_list = []
    border = {
        'left' : image['bottom'].get_pos()[0],
        'right' : image['bottom'].get_pos()[0] + image['bottom'].get_size()[0]
    }
    SCORE = 0
    HIGH_SCORE = high_score
    while True:
        x_block, y_block = image['block'].get_pos()
        if x_block >= screen.get_width() - image['block'].get_size()[0]:
            x_ver = -V_MAX*speed
        elif x_block <= 0:
            x_ver = V_MAX*speed
        image['block'].put((x_block + x_ver*speed, y_block))
        # pygame.time.wait(1)
        screen.blit(image['background'].get_img(), 
                    image['background'].get_pos())
        screen.blit(image['base'].get_img(), 
                    image['base'].get_pos())
        screen.blit(image['bottom'].get_img(), 
                    image['bottom'].get_pos())
        screen.blit(image['block'].get_img(), 
                    image['block'].get_pos())
        for block in block_list:
            screen.blit(block.get_img(), 
                        block.get_pos())
        print_score(screen, SCORE, HIGH_SCORE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                if border['left'] > image['block'].get_pos()[0]:
                    border['right'] = image['block'].get_pos()[0] + image['block'].get_size()[0]
                elif border['right'] < image['block'].get_pos()[0] + image['block'].get_size()[0]:
                    border['left'] = image['block'].get_pos()[0]
                if image['block'].get_pos()[0] + image['block'].get_size()[0] < border['left'] \
                    or image['block'].get_pos()[0] > border['right']:
                        game_over(screen, image, sound)
                        return HIGH_SCORE
                SCORE += 10
                if SCORE > HIGH_SCORE:
                    HIGH_SCORE = SCORE
                speed *= 1.05
                x = border['left']
                w = border['right'] - x
                pos = (x, image['block'].get_pos()[1])
                size = (round(w), image['block'].get_size()[1])
                new_block = MovableImage(image = image['block'].get_img(), 
                                         pos = pos,
                                         size = size,
                                         transCOLOR = (255, 255, 255))
                block_list.append(new_block)
                if image['block'].get_pos()[1] <= screen.get_height()/4:
                    move_up_sceen(image = image, 
                                  dy = image['block'].get_size()[1])
                    move_up_block_list(block_list = block_list,
                                       dy = image['block'].get_size()[1])
                image['block'].move(d = (0, -image['block'].get_size()[1]))
                image['block'].resize(size)

def move_up_sceen(image, dy):
    for img in image.values():
        if img != image['gameover']:
            img.move(d = (0, dy))                    

def move_up_block_list(block_list, dy):
    for block in block_list:
        block.move(d = (0, dy)) 
        
def game_over(screen, image, sound):
    blur_game(image)
    screen.blit(image['background'].get_img(), 
                image['background'].get_pos())
    screen.blit(image['base'].get_img(), 
                image['base'].get_pos())
    screen.blit(image['bottom'].get_img(), 
                image['bottom'].get_pos())
    screen.blit(image['gameover'].get_img(), 
                image['gameover'].get_pos())
    pygame.display.update()
    sound['gameover'].play()
    wait()
    
def blur_game(image):
    for img in image.values():
        if img != image['gameover']:
            img.blur(alpha = 120)

def print_score(screen, score, high_score):
    string1 = 'High Score: ' + str(high_score)
    string2 = 'Score: ' + str(score)
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    txt_surf1 = myfont.render(string1,False,(100,200,50))
    txt_surf2 = myfont.render(string2,False,(50,100,50))
    screen.blit(txt_surf1,(230, 50))
    screen.blit(txt_surf2,(230, 100))
    pygame.display.update()

if __name__ == "__main__":
    main()