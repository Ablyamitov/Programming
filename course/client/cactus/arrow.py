import pygame
import random
from pygame.sprite import Sprite
import os
#from clicker import Clicker

class Arrow(Sprite):
    '''Класс, отвечающий за стрелочки'''

    def __init__(self,main):
        super().__init__()
        self.game_folder = os.path.dirname(__file__)
        self.image_folder = os.path.join(self.game_folder,'images')
        self.screen = main.screen
        self.settings  = main.settings
        self.clicker = main.clicker

        self.image_right = pygame.image.load(os.path.join(self.image_folder,'nr.png'))
        self.right_rect = self.image_right.get_rect()
        self.right_rect.midleft = self.clicker.bottom_rect.midleft

        
        self.image_left = pygame.image.load(os.path.join(self.image_folder,'nl.png'))
        self.left_rect = self.image_right.get_rect()
        self.left_rect.midleft = self.clicker.bottom_rect.midleft


        self.image_up = pygame.image.load(os.path.join(self.image_folder,'nu.png'))
        self.up_rect = self.image_right.get_rect()
        self.up_rect.midleft = self.clicker.bottom_rect.midleft


        self.image_down = pygame.image.load(os.path.join(self.image_folder,'nd.png'))
        self.down_rect = self.image_right.get_rect()
        self.down_rect.midleft = self.clicker.bottom_rect.midleft



        self.color = self.settings.arrows_color[random.choice(list(self.settings.arrows_color.keys()))]
        if self.color == self.settings.arrows_color['right']:
            self.rect = self.right_rect
        elif self.color == self.settings.arrows_color['left']:
            self.rect = self.left_rect
        elif self.color == self.settings.arrows_color['up']:
            self.rect = self.up_rect
        elif self.color == self.settings.arrows_color['down']:
            self.rect = self.down_rect
        #self.screen_rect = main.screen.get_rect()
        #self.rect = pygame.Rect(0,0,self.settings.left_arrow_width,self.settings.left_arrow_height)
        #self.rect.midleft = self.clicker.bottom_rect.midleft
        self.x = float(self.rect.x)



    def update(self,reset = False):
        '''Перемещает стрелочку слева на право'''
        #Обновление позиции снаряда в вещественном формате
        self.x += self.settings.arrow_speed_factor
        #Обновление позиции прямоугольника.
        self.rect.x = self.x

        self.right_rect.x = self.x
        self.left_rect.x = self.x
        self.up_rect.x = self.x
        self.down_rect.x = self.x

        



    def blit_right_arrow(self):
        self.screen.blit(self.image_right,self.right_rect)

    def blit_left_arrow(self):
        self.screen.blit(self.image_left,self.left_rect)

    def blit_up_arrow(self):
        self.screen.blit(self.image_up,self.up_rect)

    def blit_down_arrow(self):
        self.screen.blit(self.image_down,self.down_rect)
