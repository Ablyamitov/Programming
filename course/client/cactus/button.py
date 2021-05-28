import pygame.font

class Button():

    def __init__(self,main,msg):
        '''Инициализирует атрибуты кнопки.'''
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()

        #Назначение размеров и свойств кнопок.
        self.width,self.height = 200,50
        self.button_color = (255,255,0)
        self.tect_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)

        #Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #Сообщение кнопки создает только один раз
        self.prep_msg(msg) 

    def prep_msg(self,msg):
        '''Преобразует msg в прямоугольник и выравнивает текст по центру.'''
        self.msg_image = self.font.render(msg,True,self.tect_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Отображение пустой кнопки и вывод сообщения.
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)