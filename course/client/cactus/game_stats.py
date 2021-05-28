import pygame
import pygame.font
class GameStats():

    def __init__(self,main):
        '''Инициализирует статистику'''
        self.main = main
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = main.settings
        self.reset_stats()
        self.game_active = False

        #Конец игры
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        self.end = 'Игра окончена!'

    def reset_other_stats(self):
        self.wat_count = 0
        self.all_score = 0


    def reset_stats(self):
        '''Инициализирует статистику, изменяющуюся в ходе игры.'''
        self.score = 0
        self.damage = 0 



