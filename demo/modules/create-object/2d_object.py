import pygame
import numpy as np
from tkinter import *


class Image:
    
    
    def __init__(self, path):
        self.img = self.load_img(path = path)
        
    def load_img(self, path):
        img = pygame.image.load(path)
        return img    
    
    def rotate(self, deg = 0, chg = False):
        new_img = pygame.transform.rotate(self.img, deg)  
        if chg:
            self.img = new_img
        return new_img 
    
    
