import pygame
from pygame.locals import *


class MovableImage(pygame.Surface):
    def __init__(self, image = None, path = None, pos = (0, 0), size = None, transCOLOR = None):
        if image is None:
            image = pygame.image.load(path).convert_alpha()
        if size is not None:
            self.image = pygame.transform.scale(image,
                                                size)
        else:
            self.image = image
        self.image.set_colorkey(transCOLOR)
        self.transCOLOR = transCOLOR
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.width =  self.image.get_width()
        self.height = self.image.get_height()
        self.selected = False
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

    def move(self, d):
        self.xpos += d[0]
        self.ypos += d[1]
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        
    def put(self, pos):
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        
    def get_img(self):
        return self.image
    
    def get_pos(self):
        return (self.xpos, self.ypos)
    
    def get_size(self):
        return (self.width, self.height)
    
    def resize(self, size):
        self.image = pygame.transform.scale(self.image,
                                            size)
        self.width = size[0]
        self.height = size[1]
        self.image.set_colorkey(self.transCOLOR)
        
    def blur(self, alpha):
        self.image.set_alpha(alpha)
    