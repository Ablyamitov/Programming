import sys 
import pygame

import random
import time

from settings import Settings
from clicker import Clicker
from arrow import Arrow
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from menu import Menu
from authorization import Authorization
from multiplayer import Multiplayer
from registration import Registration
from shop import Shop
import requests
import json
import os


class Main:
    '''класс для управления ресурсами и поведением игры'''
    
    def __init__(self):
        '''инициализирует игру и создает игровые ресурсы'''

        pygame.init()


        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Cactus evolution")

        self.clicker = Clicker(self)

        self.arrows = pygame.sprite.Group()
        self.game_folder = os.path.dirname(__file__)
        self.sounds_folder = os.path.join(self.game_folder,'sounds')


        self.passed_time = 0
        self.start_game_time = time.time()
        self.clock = pygame.time.Clock()

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.au = Authorization(self)

        self.last = None
        self.in_mission = False

        self.time = None
        self.access = False
        self.random_color = None


        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.current_color = None

        #Создание кнопки Play
        self.play_button = Button(self, "Play")

        self.start_time = None
        self.music_play = False
        self.waiting = True
        self.pause = False

        self.start_countdown = True
        self.timer = False
        #self.timer_h = 1
        self.timer_s = self.settings.timer
        self.timer_tick = None
        self.timer_access = True

        #Меню
        self.menu_access = True
        self.check_start_game = False
        self.menu = Menu(self)
        self.multiplayer_access = False
        self.singleplayer_access = False
        self.shop_access = False
        self.end_access = False

        self.reset_arrows = True
        self.authorization_access = True
        self.user_login = ''
        self.user_password = ''
        self.font = pygame.font.Font(None,32)
        self.text_surface = None

        self.write_access_login = False
        self.write_access_password = False
        self.login = ''
        self.password = ''
        self.bool_resp = None
        self.without_symb = None

        self.multiplayer_timer = 30
        self.multiplayer_ticks = None
        self.mu = Multiplayer(self)
        self.SSP_access = True
        self.step = None

        
        self.reg = Registration(self)
        self.reg_access = False

        #Мультиплеер - инфа о игроках и игре
        self.search_game_access = False
        self.end_round = False
        self.interval = 3
        self.start_room = False
        self.CLIENT_ID = None
        self.enemy_id = None
        self.game_data = {}
        self.game_search_ticks = None
        self.game_search_timer = None

        self.search_button = True
        self.choise = False


        self.my_health_loss = 0
        self.enemy_health_loss = 0
        self.my_health = None
        self.enemy_health = 1000
        self.end_multiplayer_game_access = False
        self.rez = ''

        self.shop = Shop(self)
        self.level = None
        self.next_level_exp = None
        self.exp = None
        self.coins = None
        self.singleplayer_coins = 0
        self.multiplayer_coins = 0
        self.multiplayer_add_coins = False
        self.singleplayer_add_coins = False
        self.singleplayer_exp = 0
        self.multiplayer_exp = 0






    def run_game(self):
        '''запуск основного цикла игры'''

        while True:
            self._check_events()
            if self.authorization_access:
                self._autorization()

            elif self.reg_access:
                self._reg()

            else:
                if not self.menu_access:            
                    if self.singleplayer_access:    
                        self._singleplayer()
                    elif self.end_access:
                        self._end_game()
                    elif self.multiplayer_access:
                        if not self.end_multiplayer_game_access:
                            if self.start_room == False:
                                self._wait_player()
                            else:
                                self._multiplayer()
                        else:
                            self._end_multiplayer_game()
                    elif self.shop_access:
                        self._shop()       
                elif self.menu_access:
                        self._menu()                
            self._update_screen()
            self.clock.tick(60)
    




    def _check_events(self):
        '''обрабатывает нажания клавиш и события мыши'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.multiplayer_access == False and self.menu_access == False:
                    self._check_play_button(mouse_pos)
                self._check_button(mouse_pos)

    def _reg(self):
        self.screen.blit(self.settings.menu_entrance,self.settings.image_menu_rect)
        self.reg.blit_registration()
        self.reg.show_enter_reg_button()
        self.reg.draw_interface()
        self._registration()
        if self.bool_resp == False:
            self.reg.show_resp(False,self.without_symb)

    def _autorization(self):
        self.screen.blit(self.settings.menu_entrance,self.settings.image_menu_rect)
        self.au.blit_autorizhation()
        self.au.show_enter_button()
        self.au.show_reg_button()
        self.au.draw_rect()
        self._authorization()
        if self.bool_resp == False:
            self.au.show_resp(False) 


    def _authorization_access(self):
        self.login =self.user_login
        self.password = self.user_password
        param = {'login': self.login, 'password': self.password}
        res = requests.post("http://localhost:3000/autorizhation", data=json.dumps(param))
        if res.text != "" and res.text!="Пусто":
            res_json = res.json()
            self.CLIENT_ID = res_json["id"]
            self.level = int(res_json["level"])
            self.next_level_exp = int(res_json["next_level_exp"])
            self.exp = int(res_json["exp"])
            self.my_health = int(res_json["health"])
            self.coins = int(res_json["coins"])
        if (bool(res.text)==True):
            self.authorization_access = False
        else:
            self.bool_resp = False
        self.user_login = ""
        self.user_password = ""

    def _registration_access(self):
        self.login =self.user_login
        self.password = self.user_password
        param = {'login': self.login, 'password': self.password}
        res = requests.post("http://localhost:3000/registration", data=json.dumps(param))
        if res.text != "" and res.text!="empty":
            res_json = res.json()
            self.CLIENT_ID = res_json["id"]
            self.level = int(res_json["level"])
            self.next_level_exp = int(res_json["next_level_exp"])
            self.exp = int(res_json["exp"])
            self.my_health = int(res_json["health"])
            self.coins = int(res_json["coins"])

        if (bool(res.text) == True and res.text!="empty"):
            self.reg_access = False                     
        elif res.text == "":
            self.without_symb = False
            self.bool_resp = False
            self.user_login =""
            self.user_password = "" 
        elif res.text == "empty":
            self.without_symb = True
            self.bool_resp = False
            self.user_login =""
            self.user_password = "" 
        self.user_login = ""
        self.user_password = ""



    def _check_button(self,mouse_pos):

        singleplayer = self.menu.singleplayer_rect.collidepoint(mouse_pos)
        multiplayer = self.menu.multiplayer_rect.collidepoint(mouse_pos)
        shop = self.menu.shop_rect.collidepoint(mouse_pos)

        login = self.au.rect.collidepoint(mouse_pos)
        password = self.au.rect_password.collidepoint(mouse_pos)

        scissors = self.mu.scissors_rect.collidepoint(mouse_pos)
        stone = self.mu.stone_rect.collidepoint(mouse_pos)
        paper = self.mu.paper_rect.collidepoint(mouse_pos)

        search_game = self.mu.lets_go_rect.collidepoint(mouse_pos)

        enter = self.au.enter_rect.collidepoint(mouse_pos)
        enter_reg = self.reg.enter_reg_rect.collidepoint(mouse_pos)
        registration = self.au.reg_rect.collidepoint(mouse_pos)

        if not self.authorization_access and self.menu_access and not self.reg_access:
            if singleplayer:
                self.arrows.empty()
                self.stats.reset_other_stats()
                self.menu_access = False
                self.check_start_game = True
                self.start_countdown = True
                self.singleplayer_access = False
                self.stats.reset_stats()
                self.singleplayer_coins = 0
                self.singleplayer_exp = 0
                self.sb.prep_score()
                self.sb.show_score()
                self.sb.show_all_score()
                pygame.display.update(self.sb.score_rect)
                self.multiplayer_access = False
                self.shop_access = False

            if multiplayer:
                self.menu_access = False
                self.multiplayer_access = True
                self.check_start_game = False
                self.singleplayer_access = False
                self.shop_access = False
                self.multiplayer_coins = 0
                self.multiplayer_exp = 0

            if shop:
                self.check_start_game = False
                self.menu_access = False
                self.shop_access = True
                self.multiplayer_access = False
                self.singleplayer_access = False
        if self.authorization_access or self.reg_access:
            if login:
                self.write_access_password = False
                self.write_access_login = True
            elif password:
                self.write_access_login = False
                self.write_access_password = True

        if not self.end_round and self.multiplayer_access and self.choise:
            if scissors:
                self.step = 'scissors'
            elif stone:
                self.step = 'rock'
            elif paper:
                self.step = 'paper'

        if self.authorization_access:
            if registration:
                self.reg_access =True
                self.authorization_access = False
                self.user_login = ""
                self.user_password = ""
            if enter:
                self._authorization_access()

        if self.reg_access:
            if enter_reg:
                self._registration_access()

                

        if self.multiplayer_access and self.search_button:
            if search_game:
                self.search_game_access = True
                self.search_button = False
                self.choise = True

        


        

    def _check_keydown_events(self,event):
        '''Реагирует на нажатие клавиш.'''
        if event.key == pygame.K_ESCAPE:
            if self.singleplayer_access:
                self.singleplayer_access = False
                self.menu_access = True
                self.check_start_game = False
                self.stats.game_active = False
                self.timer_s = self.settings.timer
                pygame.mixer.music.stop()
                self.music_play = False
                self.stats.reset_stats()
                pygame.mouse.set_visible(True)
            elif self.multiplayer_access:


                self.start_room = False
                self.game_search_ticks = None
                self.game_search_timer = None
                self.search_button = True
                self.choise = False

                if self.end_multiplayer_game_access:
                    self.multiplayer_access = False
                    self.menu_access = True,
                    self.end_round = False
                    self.step = ''
                    self.end_multiplayer_game_access = False
                    self.search_button = True

                self.multiplayer_access = False
                self.search_game_access = False
                self.menu_access = True
                self.check_start_game =False
                self.step = ''
                self.rez=''
                self.my_health_loss = 0
                self.enemy_health_loss = 0
                self.my_health = 1000
                self.enemy_health = 1000


                pygame.mouse.set_visible(True)
            elif self.shop_access:
                self.shop_access = False
                self.menu_access = True
                self.check_start_game = False
                pygame.mouse.set_visible(True)
            elif self.end_access:
                self.end_access = False
                self.menu_access = True
                self.check_start_game = False
                pygame.mouse.set_visible(True)
            elif not self.stats.game_active and self.check_start_game :
                self.menu_access = True
                self.check_start_game = False
            else:
                sys.exit()
        if self.singleplayer_access:        
            if event.key == pygame.K_RIGHT:
                self.current_color = self.settings.arrows_color['right']
                self.right = True
                self._remove_arrows()
                self.right = False
            elif event.key == pygame.K_LEFT:
                self.current_color = self.settings.arrows_color['left']
                self.left = True
                self._remove_arrows()
                self.left = False
            elif event.key == pygame.K_UP:
                self.current_color = self.settings.arrows_color['up']
                self.up = True
                self._remove_arrows()
                self.up = False
            elif event.key == pygame.K_DOWN:
                self.current_color = self.settings.arrows_color['down']
                self.down = True
                self._remove_arrows()
                self.down = False

        #if (not self.stats.game_active and self.singleplayer_access):
            #pass  
            #if event.key == pygame.K_SPACE:
                #self._start_game()
        
        if self.authorization_access:

            if event.key == pygame.K_RETURN:
                self._authorization_access()

        elif self.reg_access:
            if event.key == pygame.K_RETURN:
                self._registration_access()
            self._registration()



        if self.write_access_login or self.write_access_password:
            if event.key == pygame.K_BACKSPACE:
                if self.write_access_login:
                    self.user_login = self.user_login[:-1]
                elif self.write_access_password:
                    self.user_password = self.user_password[:-1]
            elif ((event.key>64 and event.key <91) or (event.key>96 and event.key<123) or (event.key>47 and event.key<58)):
                if self.write_access_login:
                    self.user_login+=event.unicode
                elif self.write_access_password:
                    self.user_password +=event.unicode


    

    def _check_play_button(self,mouse_pos):
        '''Запускает новую игру при нажатии кнопки Play.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            #Сброс игровой статистики.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.singleplayer_access = True
            #Указатель мыши скрывается
            pygame.mouse.set_visible(False)


        


    def _create_arrow(self):
        '''создание и добавление стрелочки в группу стрелочек'''
        new_arrow = Arrow(self)
        self.arrows.add(new_arrow)


    def _update_arrows(self):
        '''прорисовка движения стрелочки и её удаление'''
        self.arrows.update()
        for arrow in self.arrows.sprites():
            if arrow.color == self.settings.arrows_color['right']:
                arrow.blit_right_arrow()
            elif arrow.color == self.settings.arrows_color['left']:
                arrow.blit_left_arrow()
            elif arrow.color == self.settings.arrows_color['up']:
                arrow.blit_up_arrow()
            elif arrow.color == self.settings.arrows_color['down']:
                arrow.blit_down_arrow()

        for arrow in self.arrows.copy():
            if arrow.right_rect.left>=self.settings.screen_width:
                self.arrows.remove(arrow)

    def _remove_arrows(self):
        '''Удаление стрелочки, при нажатии клавиши'''
        for arrow in self.arrows.copy():
            ###########################
            if self.clicker.bottom_square.right < arrow.rect.left:
                self.arrows.remove(arrow)
                self._remove_arrows()

            ##########################
            if self.current_color == arrow.color:
                if arrow.rect.left < self.clicker.bottom_square.left or (
                    arrow.rect.left >= self.clicker.bottom_square.left and
                    (arrow.rect.right >= self.clicker.bottom_square.right and
                    arrow.rect.right <= self.clicker.bottom_square.right + arrow.rect.width)
                ):
                    if(self.stats.score > 9):
                        self.stats.score -= self.settings.arrow_points_missed
                        self.stats.all_score -= self.settings.arrow_points_missed
                    self.sb.prep_score()
                    self.arrows.remove(arrow)
                    self.clicker.draw_red_square()
                    pygame.display.update(self.clicker.bottom_square)
                    pygame.time.delay(100)
                    break



                elif ((arrow.rect.left>=self.clicker.bottom_square.left)and
                (arrow.rect.right <= self.clicker.bottom_square.right)):
                    self.stats.score += self.settings.arrow_points_hit
                    self.stats.all_score += self.settings.arrow_points_hit
                    self.sb.prep_score()
                    self.arrows.remove(arrow)
                    self.clicker.draw_green_square()
                    pygame.display.update(self.clicker.bottom_square)
                    pygame.time.delay(100)
                    break
            else:
                if(self.stats.score > 9):
                    self.stats.score -= self.settings.arrow_points_missed
                    self.stats.all_score -= self.settings.arrow_points_missed
                self.sb.prep_score()
                self.arrows.remove(arrow)
                self.clicker.draw_red_square()
                pygame.display.update(self.clicker.bottom_square)
                pygame.time.delay(100)
                break 

    def _check_points(self):
        '''Проверяет очки, а затем поливает(если очки максимум)'''
        if(self.stats.score>=self.settings.limit_points):
            self.stats.wat_count +=1
            self.singleplayer_coins +=1
            self.singleplayer_exp +=100
            self.access = True
            self.stats.reset_stats()
            self.sb.prep_score()
            if (not self.time):
                self.time = pygame.time.get_ticks()

        if (self.access == True and self.time + 3500 >= pygame.time.get_ticks()):
            self.clicker.draw_watering()
        else:
            self.time = None
            self.access = False


    def _authorization(self):
        self.text_surface = self.font.render(self.user_login,True,(255,255,255))
        self.password_text_surface = self.font.render(self.user_password,True,(255,255,255))
        self.screen.blit(self.text_surface,(self.au.rect.x+5,self.au.rect.y + 5))
        self.au.show_enter()
        self.au.rect.w = max(100,self.text_surface.get_width()+10)
        self.screen.blit(self.password_text_surface,(self.au.rect_password.x+5,self.au.rect_password.y + 5))
        self.au.rect_password.w = max(100,self.password_text_surface.get_width()+10)

    def _registration(self):
        self.text_surface = self.font.render(self.user_login,True,(255,255,255))
        self.password_text_surface = self.font.render(self.user_password,True,(255,255,255))
        self.screen.blit(self.text_surface,(self.reg.rect.x+5,self.reg.rect.y + 5))
        self.reg.show_enter()
        self.reg.rect.w = max(100,self.text_surface.get_width()+10)
        self.screen.blit(self.password_text_surface,(self.reg.rect_password.x+5,self.reg.rect_password.y + 5))
        self.reg.rect_password.w = max(100,self.password_text_surface.get_width()+10)

    def _menu(self):
        self.screen.blit(self.settings.menu,self.settings.image_menu_rect)
        self.menu.blit_menu()
        self.menu.blit_coins(self.coins,self.exp,self.level,self.next_level_exp)
        self.menu.draw_hi(self.login)
    
    def _set_and_coins(self):
        param = {'coins': str(self.coins), 'id': str(self.CLIENT_ID)}
        requests.post("http://localhost:3000/set_exp_and_coins", data=json.dumps(param))

    def _set_and_check_exp_and_level(self):
        param = {'exp': str(self.exp), 'id': str(self.CLIENT_ID), 'next_level_exp':str(self.next_level_exp),'level':str(self.level)}
        response = requests.post('http://localhost:3000/set_and_check_exp_and_level', data=json.dumps(param))
        res_json = response.json()
        self.exp = int(res_json["exp"])
        self.next_level_exp = int(res_json["next_level_exp"])
        self.level = int(res_json["level"])


    def _singleplayer(self):
        self.screen.blit(self.settings.image_desert,self.settings.image_desert_rect)
        if self.stats.game_active:
            #Отсчёт
            if self.start_countdown == True:
                self.sb.show_countdown(sec = 3)
                pygame.display.flip()
                pygame.time.delay(1000)
                self.screen.blit(self.settings.image_desert,self.settings.image_desert_rect)
                self.sb.show_countdown(sec = 2)
                pygame.display.flip()
                pygame.time.delay(1000)
                self.screen.blit(self.settings.image_desert,self.settings.image_desert_rect)
                self.sb.show_countdown(sec = 1)
                pygame.display.flip()
                pygame.time.delay(1000)
                self.start_countdown = False
                self.screen.blit(self.settings.image_desert,self.settings.image_desert_rect)
                pygame.display.flip()
            if self.timer_access:
                if not self.music_play:
                    random_music = random.choice(self.settings.musics)
                    
                    pygame.mixer.music.load(os.path.join(self.sounds_folder,random_music))
                    if random_music == "sep.mp3":
                        pygame.mixer.music.play(loops=0, start=28.0, fade_ms = 0)
                    elif random_music == "never.mp3" or random_music == "onepunchman.mp3":
                        pygame.mixer.music.play(loops=0, start=10.0, fade_ms = 0)
                    elif random_music == "Pugacheva.mp3":
                        pygame.mixer.music.play(loops=0, start=48.0, fade_ms = 0)
                    elif random_music == "C_C_Catch.mp3":
                        pygame.mixer.music.play(loops=0, start=41.0, fade_ms = 0)
                    else:
                        pygame.mixer.music.play(loops=0, start=0, fade_ms = 0)
                        
                    self.music_play = True
                self.sb.show_timer(sec = self.timer_s)

                if self.timer_tick == None:
                    self.timer_tick = pygame.time.get_ticks()

                if self.timer_tick + 1000 < pygame.time.get_ticks():
                    self.timer_s -=1
                    self.timer_tick = None

                if self.timer_s == -1:
                    self.timer_s = self.settings.timer
                    self.stats.game_active= False
                    self.singleplayer_access = False
                    self.check_start_game = False
                    self.end_access = True
                    self.singleplayer_add_coins = True
                    pygame.mixer.music.stop()
                    self.music_play = False
                    pygame.mouse.set_visible(True)
                
                self.clicker.draw_cactus()
                self.clicker.draw_stats_rect()
                self.clicker.draw_rect()
                self.sb.show_score()
                self.sb.show_all_score()
                if self.waiting:
                    pygame.display.flip()
                    pygame.time.delay(500)
                    self.waiting=False
                self._check_events()
                if pygame.time.get_ticks() > self.passed_time:
                    self._create_arrow()
                    self.passed_time = pygame.time.get_ticks()+random.randint(800,1150)
                self._check_points()
                self._draw_other()
                self.reset_arrows = False
                pygame.display.flip()


    def _end_game(self):
        self.screen.blit(self.settings.image_desert,self.settings.image_desert_rect)
        self.sb.end_game(self.singleplayer_coins,self.singleplayer_exp)
        if self.singleplayer_add_coins:
            self.coins+=self.singleplayer_coins
            if self.level<5:
                self.exp+=self.singleplayer_exp
                self._set_and_check_exp_and_level()
            self.singleplayer_add_coins = False
            self._set_and_coins()


    def _check_multiplayer_param(self):
        if self.rez == 'WIN':
            self.multiplayer_coins += 10
            self.multiplayer_exp += 100

    def _end_multiplayer_game(self):
        self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
        if self.multiplayer_add_coins:
            self._check_multiplayer_param()
            self.coins+=self.multiplayer_coins
            if self.level<5:
                self.exp += self.multiplayer_exp
                self._set_and_check_exp_and_level()
            self.multiplayer_add_coins = False
            self._set_and_coins()
        self.mu.blit_end_multiplayer_game(self.rez,self.multiplayer_coins,self.multiplayer_exp)
        self.my_health_loss = 0
        self.enemy_health_loss = 0
        self.my_health = 1000
        self.enemy_health = 1000



    def _update_health(self,my = False,enemy = False):
        if my:
            self.my_health_loss+=62.5
            self.my_health-=250                           
        if enemy:
            self.enemy_health_loss+=62.5
            self.enemy_health-=250


    def _blit_elem(self,data):
        if data['user_choice'] == 'rock':
            self.mu.blit_elem(scissors = False, paper = False,rock = True)
        elif data['user_choice'] == 'scissors':
            self.mu.blit_elem(scissors=True, paper = False,rock=False)
        elif data['user_choice'] == 'paper':
            self.mu.blit_elem(scissors=False, paper = True,rock=False)

    def _rez(self,data):
        try:
            response = requests.post('http://localhost:3000/play_game', data)
            resp_json = response.json()
            if resp_json['game_status'] == 'run':
                if resp_json['winner'] == 'I':
                    self._update_health(enemy=True)
                    self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
                    self._blit_elem(data)
                    self.mu.multiplayer_game()
                    self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
                    self.mu.blit_health(self.my_health,self.enemy_health)
                    self.mu.blit_rez('win')
                    self.mu.blit_enemy_elem(self.step,'WIN')
                    self.step = ''
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    # Если финал
                    if self.my_health_loss == 250 or self.enemy_health_loss == 250:
                        self.rez = 'WIN'
                        self.end_multiplayer_game_access = True
                        self.multiplayer_add_coins = True

                    #Блит победы
                elif resp_json['winner'] == 'Other':
                    self._update_health(my=True)
                    self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
                    self._blit_elem(data)
                    self.mu.multiplayer_game()
                    self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
                    self.mu.blit_health(self.my_health,self.enemy_health)
                    self.mu.blit_rez('lose')
                    self.mu.blit_enemy_elem(self.step,'LOSE')
                    self.step = ""
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    if self.my_health_loss == 250 or self.enemy_health_loss == 250:
                        self.rez = 'LOSE'
                        self.end_multiplayer_game_access = True
                    #Блит слива
                elif resp_json['winner'] == 'Draw':
                    self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
                    self._blit_elem(data)
                    self.mu.multiplayer_game()
                    self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
                    self.mu.blit_health(self.my_health,self.enemy_health)
                    self.mu.blit_rez('draw')
                    self.mu.blit_enemy_elem(self.step,'DRAW')
                    self.step = ""
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    #Блит ничьи                  
                self.end_round = True
                return
            else:
                self.mu.blit_act(True)
                #print('waiting enemy choice')
        except Exception as err:
            print(f'{err}')
            return



    def rock(self):
        data={'ID':self.CLIENT_ID, 'game_id':self.game_data['game_id'], 'user_choice': 'rock'}
        self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
        self.mu.multiplayer_game()
        self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
        self.mu.blit_health(self.my_health,self.enemy_health)
        self.mu.blit_elem(scissors = False, paper = False,rock = True)
        self._rez(data)


    def scissors(self):
        data={'ID':self.CLIENT_ID, 'game_id':self.game_data['game_id'], 'user_choice': 'scissors'}
        self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
        self.mu.multiplayer_game()
        self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
        self.mu.blit_health(self.my_health,self.enemy_health)
        self.mu.blit_elem(scissors=True, paper = False,rock=False)


        def check():
            try:
                response = requests.post('http://localhost:3000/play_game', data)
                resp_json = response.json()
                print(resp_json)
                if resp_json['game_status'] == 'run':
                    if resp_json['winner'] == 'I':
                        self.mu.blit_rez('win')
                        print("WIN")
                        self.step = ""
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        #Блит победы
                    elif resp_json['winner'] == 'Other':
                        self.mu.blit_rez('lose')
                        print("LOSE")
                        self.step = ""
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        #Блит слива
                    elif resp_json['winner'] == 'Draw':
                        self.mu.blit_rez('draw')
                        print("DRAW")
                        self.step = ""
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        #Блит ничьи                  
                    self.end_round = False
                    return
                else:
                    print('waiting enemy choice')
            except Exception as err:
                print(f'{err}')
                
                return
        self._rez(data)

    def paper(self):
        data={'ID':self.CLIENT_ID, 'game_id':self.game_data['game_id'], 'user_choice': 'paper'}
        self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
        self.mu.multiplayer_game()
        self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
        self.mu.blit_health(self.my_health,self.enemy_health)
        self.mu.blit_elem(scissors=False, paper = True,rock=False)


        def check():
            try:
                response = requests.post('http://localhost:3000/play_game', data)
                resp_json = response.json()
                print(resp_json)
                if resp_json['game_status'] == 'run':
                    if resp_json['winner'] == 'I':
                        self.mu.blit_rez('win')
                        print("WIN")
                        self.step = ""
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        #Блит победы
                    elif resp_json['winner'] == 'Other':
                        self.mu.blit_rez('lose')
                        print("LOSE")
                        self.step = ""
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        #Блит слива
                    elif resp_json['winner'] == 'Draw':
                        self.mu.blit_rez('draw')
                        print("DRAW")
                        self.step = ""
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        #Блит ничьи                  
                    self.end_round = False
                    return
                else:
                    print('waiting enemy choice')
            except Exception as err:
                print(f'{err}')
                return
        self._rez(data)


    
    def game_search(self):
        data={'ID':self.CLIENT_ID}
        def check_game():
            try:
                response = requests.post('http://localhost:3000/game_search', data)
                resp_json = response.json()
                if resp_json['game_status'] == 'run':
                    self.game_data = resp_json['game_data']
                    self.game_search_timer = False
                    self.game_search_ticks = None
                    self.search_game_access = False
                    self.start_room = True
                    return
                else:
                    pass
            except Exception as err:
                print(f'{err}')
                self.game_search_timer = False
                self.game_search_ticks = None
                self.search_game_access = False
                self.start_room = False
                return
        self.game_search_timer = True
        if not self.game_search_ticks and self.game_search_timer:
            self.game_search_ticks = pygame.time.get_ticks()
        if pygame.time.get_ticks()>self.game_search_ticks+1000:
            check_game()
            self.game_search_ticks = None
                
    def _cool_down(self):
        self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
        self.mu.multiplayer_game()
        self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
        self.mu.blit_health(self.my_health,self.enemy_health)
        self.sb.show_countdown(sec = self.interval)
        self.interval -=1
        pygame.display.flip()
        pygame.time.delay(1000)

    def _mult_timer(self):
        if self.step == 'rock':
            self.rock()
        elif self.step == 'scissors':
            self.scissors()
        elif self.step == 'paper':
            self.paper()
        else:
            self.mu.blit_act(False)
        if self.end_round and not self.end_multiplayer_game_access:
            for i in range(4):
                self._cool_down()
            self.interval = 3
            self.end_round = False
            self.multiplayer_timer = 30



    def _wait_player(self):
        self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
        self.mu.search_player_button()
        if self.search_game_access:
            self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
            self.mu.blit_waiting()
            self.game_search()


    def _multiplayer(self):
        self.screen.blit(self.settings.mult_bg,self.settings.mult_bg_rect)
        self.mu.multiplayer_game()
        self.mu.draw_stats_part_rect(self.my_health_loss,self.enemy_health_loss)
        self.mu.blit_health(self.my_health,self.enemy_health)
        self.mu.blit_elem()
        self._mult_timer()
        

    def _shop(self):
        self.screen.blit(self.settings.shop_bg,self.screen.get_rect())
        if not (self.level ==5):
            self.menu.show_bebop()
        else:
            self.shop.blit_all_cactus()
        

    def _draw_other(self):
        self.clicker.draw_stats_part_rect(self.stats.score)
        self._update_arrows()
        self.sb.show_score()
        self.sb.show_all_score()



    def _update_screen(self):
        if not self.stats.game_active and self.check_start_game :
            self.screen.blit(self.settings.image_desert,self.settings.image_desert_rect)
            self.play_button.draw_button()
            self.sb.write_instruction()
        pygame.display.flip()


    
    
if __name__ == "__main__":
    '''создание экземпляра и запуск игры'''
    m = Main()
    m.run_game()

