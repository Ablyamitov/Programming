import pygame
import os


class Settings():
#класс для хранения всех настроек игры

    def __init__(self):
        
        '''инициализирует статические данные'''
        #экран
        self.game_folder = os.path.dirname(__file__)
        self.image_folder = os.path.join(self.game_folder,'images')

        self.image_desert = pygame.image.load(os.path.join(self.image_folder,'desert.jpg'))
        self.image_desert_rect= self.image_desert.get_rect()
        self.image_desert_rect.x = 0
        self.image_desert_rect.y = 0
 
        self.timer = 15
        self.musics = ["sep.mp3","never.mp3","onepunchman.mp3","Pugacheva.mp3","C_C_Catch.mp3"]         #"sounds/Egor.mp3"
        #self.screen_width = 1536
        #self.screen_height = 871
        self.screen_width = 1200
        self.screen_height = 700
        self.center_x = self.screen_width/2
        self.center_y = self.screen_height/2

        self.background_color = (255, 255, 255)

        #Прямоугольник
        self.image_bottom = pygame.image.load(os.path.join(self.image_folder,'des1.jpg'))
        self.image_bottom_rect = self.image_bottom.get_rect()


        self.bottom_rect_width = self.screen_width
        self.bottom_rect_height = self.screen_height*0.2
        self.bottom_rect_x = 0
        self.bottom_rect_y = self.screen_height - self.bottom_rect_height
        self.bottom_rect_color = (65,25,0)
        

        #Квадрат в середине прямоугольника
        self.obema = pygame.image.load(os.path.join(self.image_folder,'target.jpg'))
        self.bottom_square_height = self.bottom_rect_height
        self.bottom_square_width = self.bottom_square_height

        #self.bottom_square_color = (123,212,78)

        self.bottom_square_x = (self.screen_width/2) - self.bottom_square_width/2
        self.bottom_square_y = self.screen_height - self.bottom_rect_height


        #Прямоугольник статистики
        self.stats_rect_width = 250
        self.stats_rect_height = 25
        self.stats_rect_x = self.screen_width - self.stats_rect_width - 10
        self.stats_rect_y = 60

        #Стрелки
        self.arrow_color = (0,0,0)
        self.arrows_color ={'right':(0,0,0),'up':(255,182,193),'left':(255,255,255), 'down':(138,255,189)}
        self.left_arrow_width = 50
        self.left_arrow_height = 50

        self.arrow_speed_factor = 10

        self.arrow_points_hit = 50
        self.arrow_points_missed = 10
        self.limit_points = 250

        #Кактус
        self.cactus_rect_width = 300
        self.cactus_rect_height = 400
        self.cactus_rect_x = 60
        self.cactus_rect_y = self.bottom_square_y - self.cactus_rect_height - 30
        self.cactus_rect_color = (0,47,31)
        self.image_cactus = pygame.image.load(os.path.join(self.image_folder,'cactuss.png'))


        #Поливка
        self.watering_rect_width = 300
        self.watering_rect_height = 150
        self.watering_rect_x = ((self.cactus_rect_x + self.cactus_rect_width/2)-self.watering_rect_width/2)-75
        self.watering_rect_y = self.cactus_rect_y - int(0.0694 * self.screen_height)
        self.watering_rect_color = (66,170,255)

        self.image_watering = pygame.image.load(os.path.join(self.image_folder,'wat.png'))







        self.image_menu = pygame.image.load(os.path.join(self.image_folder,'new_Menu_bg1.png'))
        self.image_menu_entrance = pygame.image.load(os.path.join(self.image_folder,'new_Menu_bg.png'))
        self.menu_entrance = pygame.transform.scale(self.image_menu_entrance,
                                (self.screen_width,self.screen_height)
                                                            )

        self.menu = pygame.transform.scale(self.image_menu,
                                        (self.screen_width,self.screen_height)
                                        )


        self.image_menu_rect= self.menu.get_rect()
        self.image_menu_rect.x = 0
        self.image_menu_rect.y = 0

        #Кнопка синглплеер
        self.image_singleplayer = pygame.image.load(os.path.join(self.image_folder,'singleplayer1.png'))
        self.singleplayer_rect_width = 300
        self.singleplayer_rect_height = 80
        self.singleplayer_rect_x = 130
        self.singleplayer_rect_y = 170


        #Кнопка мультиплеер
        self.image_multiplayer = pygame.image.load(os.path.join(self.image_folder,'multiplayer2.png'))
        self.multiplayer_rect_width = self.singleplayer_rect_width
        self.multiplayer_rect_height = self.singleplayer_rect_height
        self.multiplayer_rect_x = self.singleplayer_rect_x + 50
        self.multiplayer_rect_y = self.singleplayer_rect_y +self.singleplayer_rect_height+ 50


        #Кнопка магазина

        self.image_shop = pygame.image.load(os.path.join(self.image_folder,'shop3.png'))
        self.shop_rect_width = self.multiplayer_rect_width
        self.shop_rect_height = self.multiplayer_rect_height
        self.shop_rect_x = self.multiplayer_rect_x + 50
        self.shop_rect_y = self.multiplayer_rect_y +self.multiplayer_rect_height+ 50



        self.image_cur = pygame.image.load(os.path.join(self.image_folder,'cur.png'))
        self.image_cur_rect = self.image_cur.get_rect()

        self.mult_bg = pygame.image.load(os.path.join(self.image_folder,'mult.jpg'))
        self.mult_bg_rect = self.mult_bg.get_rect()

        self.scissors = pygame.image.load(os.path.join(self.image_folder,'scissors.png'))
        self.scissors_rect = self.scissors.get_rect()

        self.paper = pygame.image.load(os.path.join(self.image_folder,'paper.png'))

        self.stone = pygame.image.load(os.path.join(self.image_folder,'stone.png'))

        

        self.image_win = pygame.image.load(os.path.join(self.image_folder,'win.jpg'))
        self.image_win_rect = self.image_win.get_rect()

        self.image_draw = pygame.image.load(os.path.join(self.image_folder,'draw.jpg'))
        self.image_draw_rect = self.image_draw.get_rect()

        self.image_lose = pygame.image.load(os.path.join(self.image_folder,'lose.jpg'))
        self.image_lose_rect = self.image_lose.get_rect()

        self.image_registration = pygame.image.load(os.path.join(self.image_folder,'reg.png'))
        self.image_enter = pygame.image.load(os.path.join(self.image_folder,'aut.png'))

        self.image_enter_reg = pygame.image.load(os.path.join(self.image_folder,'enter_reg.png'))

        self.lets_go  = pygame.image.load(os.path.join(self.image_folder,'lets_go.jpg'))

        self.search_button = pygame.image.load(os.path.join(self.image_folder,'search1.png'))

        self.box_cactus = pygame.image.load(os.path.join(self.image_folder,'box.png'))
        self.cowboy_cactus = pygame.image.load(os.path.join(self.image_folder,'cowboy.png'))
        self.cute_cactus = pygame.image.load(os.path.join(self.image_folder,'cute.png'))

        self.shop = pygame.image.load(os.path.join(self.image_folder,'shop.jpg'))

        
    
        self.shop_bg = pygame.transform.scale(self.shop,
                                (self.screen_width,self.screen_height)
                                )
        



