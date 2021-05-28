import pygame
from pygame.sprite import Sprite

class Clicker(Sprite):
    '''класс однопользовательской игры - кликера'''

    def __init__(self,main):
        super().__init__()

        self.screen = main.screen
        self.settings = main.settings
        self.screen_rect = main.screen.get_rect()

        #Главный огромный прямоугольник
        self.bottom_rect = pygame.Rect(self.settings.bottom_rect_x,
                            self.settings.bottom_rect_y,
                            self.settings.bottom_rect_width,
                            self.settings.bottom_rect_height)


        #Квадрат в центре прямоугольника
        self.bottom_square = pygame.Rect(self.settings.bottom_square_x,
                                self.settings.bottom_square_y,                                   
                                self.settings.bottom_square_width,                                
                                self.settings.bottom_square_height)

        self.square = (pygame.transform.scale(self.settings.obema,
                          (int(self.settings.bottom_square_width),int(self.settings.bottom_square_height))
                          ))


        #Прямоугольник счёта
        self.stats_rect  =  pygame.Rect(self.settings.stats_rect_x,
                                self.settings.stats_rect_y,                 
                                self.settings.stats_rect_width,             
                                self.settings.stats_rect_height)

        #Часть счёта (сколько очков зароботал - столько и покравает прямоугольник счёта)
        self.stats_part_rect  =  pygame.Rect(self.settings.stats_rect_x,
                        self.settings.stats_rect_y,        
                        self.settings.stats_rect_width,    
                        self.settings.stats_rect_height)


        #Кактус
        self.cactus_rect  =  pygame.Rect(self.settings.cactus_rect_x,
                self.settings.cactus_rect_y,        
                self.settings.cactus_rect_width,    
                self.settings.cactus_rect_height)
        

        self.cactus = pygame.transform.scale(self.settings.image_cactus,
                                                (self.settings.cactus_rect_width,self.settings.cactus_rect_height)
                                                )
        #Поливка
        self.watering_rect = pygame.Rect(self.settings.watering_rect_x,
                                        self.settings.watering_rect_y,        
                                        self.settings.watering_rect_width,    
                                        self.settings.watering_rect_height)

        self.watering = pygame.transform.scale(self.settings.image_watering,
                          (self.settings.watering_rect_width,self.settings.watering_rect_height)
                          )


        #Конец игры
        self.the_end  =  pygame.Rect(self.settings.screen_width/2,
                                self.settings.screen_height/2,        
                                150,    
                                80)



    #Рисуем прямоугольник и квадрат по середине прямоугольника
    def draw_rect(self,color = ((117,187,253))):
        '''Вывод прямоугольника в нижней области.'''
        #self.bottom_rect.midbottom = self.screen_rect.midbottom                           
        #pygame.draw.rect(self.screen,self.settings.bottom_rect_color,self.bottom_rect)
        self.screen.blit(self.settings.image_bottom,self.bottom_rect)

        #self.bottom_square.midbottom = self.screen_rect.midbottom               
        #pygame.draw.rect(self.screen,color,self.bottom_square)
        self.screen.blit(self.square,self.bottom_square)


    #Рисуем зелёный квадратик, если попал
    def draw_green_square(self):
        pygame.draw.rect(self.screen,(76,255,0),self.bottom_square)

    #Рисуем красный квадратик, если промахнулся
    def draw_red_square(self):
        pygame.draw.rect(self.screen,(255,0,0),self.bottom_square)

    #Рисуем прямоугольник статистики
    def draw_stats_rect(self):
        pygame.draw.rect(self.screen,(0,0,0),self.stats_rect)

    #Рисуем набранные очки на прямоугольнике статистике
    def draw_stats_part_rect(self,width = 0):
        self.stats_part_rect.width = width
        pygame.draw.rect(self.screen,(255,255,0),self.stats_part_rect)

    #Рисуем кактус
    def draw_cactus(self):
        #pygame.draw.rect(self.screen,self.settings.cactus_rect_color,self.cactus_rect)
        self.screen.blit(self.cactus,self.cactus_rect)

    #Рисуем поливку
    def draw_watering(self):
        pygame.draw.rect(self.screen,self.settings.watering_rect_color,self.watering_rect)


    def draw_watering(self):
        self.screen.blit(self.watering,self.watering_rect)

    def draw_end(self):
        pygame.draw.rect(self.screen,(0,0,0),self.the_end)


        





    
