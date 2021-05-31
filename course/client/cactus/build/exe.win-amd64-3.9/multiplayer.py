import pygame
import copy

class Multiplayer():

    def __init__(self,main):
        self.screen = main.screen
        self.settings = main.settings
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (0,0,0)
        self.button_color = (255,255,255)

        self.scissors = pygame.transform.scale(self.settings.scissors,
                                        (200,200))
        self.scissors_rect = self.scissors.get_rect()
        self.scissors_rect.x,self.scissors_rect.y = 400,100

        self.paper = pygame.transform.scale(self.settings.paper,
                                (200,200))
        self.paper_rect = self.paper.get_rect()
        self.paper_rect.topleft = self.scissors_rect.bottomleft

        self.stone = pygame.transform.scale(self.settings.stone,
                        (200,200))
        self.stone_rect = self.stone.get_rect()
        self.stone_rect.topleft = self.paper_rect.bottomleft 

        self.search_player_rect = pygame.Rect(0,0,250,150)
        self.search_player_rect.center = self.screen_rect.center

        self.win = pygame.transform.scale(self.settings.image_win,
                                            (200,100))
        self.win_rect = self.win.get_rect()
        self.win_rect.midtop = self.screen_rect.midtop

        self.draw = pygame.transform.scale(self.settings.image_draw,
                                    (200,100))
        self.draw_rect = self.draw.get_rect()
        self.draw_rect.midtop = self.screen_rect.midtop

        self.lose = pygame.transform.scale(self.settings.image_lose,
                                    (200,100))                                   
        self.lose_rect = self.lose.get_rect()
        self.lose_rect.midtop = self.screen_rect.midtop

        self.cactus_rect  =  pygame.Rect(self.settings.cactus_rect_x,
                           self.settings.cactus_rect_y,      
                        self.settings.cactus_rect_width,    
                           self.settings.cactus_rect_height)
        self.cactus_rect.y = self.screen.get_height() - self.cactus_rect.height - 10
        self.cactus_en_rect  =  pygame.Rect(self.settings.cactus_rect_x,
                             self.settings.cactus_rect_y,     
                          self.settings.cactus_rect_width,    
                             self.settings.cactus_rect_height)
        self.cactus_en_rect.y = self.cactus_rect.y
        self.cactus_en_rect.x = self.screen.get_width() - self.cactus_en_rect.width - 50
        self.stats_rect  =  pygame.Rect(self.cactus_rect.x,
              self.cactus_rect.y - 25,         
              self.settings.stats_rect_width,     
              self.settings.stats_rect_height)
        self.stats_en_rect  =  pygame.Rect(self.cactus_en_rect.x,
                    self.stats_rect.y,         
                    self.settings.stats_rect_width, 
                    self.settings.stats_rect_height)
                                            
        self.lets_go = self.settings.lets_go
        self.lets_go_rect  = self.lets_go.get_rect()
        self.lets_go_rect.center = self.screen_rect.center

        
    
    def blit_elem(self,scissors = True,paper = True,rock = True):
        if scissors:
            self.screen.blit(self.scissors,self.scissors_rect)
        if paper:
            self.screen.blit(self.paper,self.paper_rect)
        if rock:
            self.screen.blit(self.stone,self.stone_rect)


    def blit_waiting(self):
        search_button  =self.settings.search_button
        search_button_rect = search_button.get_rect()
        search_button_rect.center = self.screen_rect.center
        self.screen.blit(search_button,search_button_rect)

    def search_player_button(self):
        search_text = "Нажмите на кнопку 'В бой!' и ожидайте противника"
        search_image = self.font.render(search_text,True,self.text_color)
        search_text_rect = search_image.get_rect()
        search_text_rect.centerx = self.screen_rect.centerx
        self.screen.blit(search_image,search_text_rect)
        self.screen.blit(self.lets_go,self.lets_go_rect)

        inst = 'Инструкция: '
        inst_image = self.font.render(inst,True,self.text_color)
        inst_rect = inst_image.get_rect()
        inst_rect.x = search_text_rect.x 
        inst_rect.y = search_text_rect.y +search_text_rect.height+75
        self.screen.blit(inst_image,inst_rect)

        inst1 = "Выиграл раунд - отнялись у противника 250 хп"
        inst1_image = self.font.render(inst1,True,self.text_color)
        inst1_rect = inst1_image.get_rect()
        inst1_rect.x = inst_rect.x 
        inst1_rect.y = inst_rect.y +inst_rect.height+10
        self.screen.blit(inst1_image,inst1_rect)

        inst2 = "Проиграл раунд - отнялись у себя 250 хп"
        inst2_image = self.font.render(inst2,True,self.text_color)
        inst2_rect = inst2_image.get_rect()
        inst2_rect.x = inst1_rect.x 
        inst2_rect.y = inst1_rect.y +inst2_rect.height+10
        self.screen.blit(inst2_image,inst2_rect)

        inst3 = 'Победа в игре - у противника 0 хп, тебе: +10 монет и + 150 exp'
        inst3_image = self.font.render(inst3,True,self.text_color)
        inst3_rect = inst3_image.get_rect()
        inst3_rect.x = inst2_rect.x 
        inst3_rect.y = inst2_rect.y +inst2_rect.height+10
        self.screen.blit(inst3_image,inst3_rect)

        inst4 = 'Поражение в игре - у себя 0 хп'
        inst4_image = self.font.render(inst4,True,self.text_color)
        inst4_rect = inst4_image.get_rect()
        inst4_rect.x = inst3_rect.x 
        inst4_rect.y = inst3_rect.y +inst3_rect.height+10
        self.screen.blit(inst4_image,inst4_rect)



    def blit_enemy_elem(self,my_elem,rez):

        enemy_rock_rect = copy.deepcopy(self.stone_rect)
        enemy_rock_rect.x =  self.screen_rect.width - (enemy_rock_rect.x + enemy_rock_rect.width)

        enemy_paper_rect = copy.deepcopy(self.paper_rect)
        enemy_paper_rect.x = self.screen_rect.width - (enemy_paper_rect.x + enemy_paper_rect.width)

        enemy_scissors_rect = copy.deepcopy(self.scissors_rect)
        enemy_scissors_rect.x = self.screen_rect.width - (enemy_scissors_rect.x  +enemy_scissors_rect.width)

        if rez == "WIN":
            if my_elem == "rock":
                self.screen.blit(self.scissors,enemy_scissors_rect)
            elif my_elem == "paper":
                self.screen.blit(self.stone,enemy_rock_rect)
            elif my_elem == "scissors":
                self.screen.blit(self.paper,enemy_paper_rect)

        elif rez == "LOSE":
            if my_elem == "rock":
                self.screen.blit(self.paper,enemy_paper_rect)
            elif my_elem == "paper":
                self.screen.blit(self.scissors,enemy_scissors_rect)
            elif my_elem == "scissors":
                self.screen.blit(self.stone,enemy_rock_rect)

        elif rez == "DRAW":
            if my_elem == "rock":
                self.screen.blit(self.stone,enemy_rock_rect)
            elif my_elem == "paper":
                self.screen.blit(self.paper,enemy_paper_rect)
            elif my_elem == "scissors":
                self.screen.blit(self.scissors,enemy_scissors_rect)


    def blit_rez(self,rez):
        if rez == 'win':
            self.screen.blit(self.win,self.win_rect)
        elif rez == 'draw':
            self.screen.blit(self.draw,self.draw_rect)
        elif rez == 'lose':
            self.screen.blit(self.lose,self.lose_rect)


    def blit_end_multiplayer_game(self,rez,coins,exp):
        if rez == 'WIN':
            end_game_text = 'Подзравляю, ты победил!'
        elif rez == 'LOSE':
            end_game_text = 'К сожалению, ты проиграл'
        end_game_text_image = self.font.render(end_game_text,True,(255,255,255))
        end_game_text_rect = end_game_text_image.get_rect()
        end_game_text_rect.midtop = self.screen_rect.midtop
        self.screen.blit(end_game_text_image,end_game_text_rect)

        exit_text = 'Нажми ESC, чтобы выйти в меню'
        exit_text_image = self.font.render(exit_text,True,(255,255,255))
        exit_text_rect = exit_text_image.get_rect()
        exit_text_rect.midbottom = self.screen_rect.midbottom
        self.screen.blit(exit_text_image,exit_text_rect)

        coins_text = "Заработано монет: "+str(coins)
        coins_text_image = self.font.render(coins_text,True,(255,255,255))
        coins_text_rect = coins_text_image.get_rect()
        coins_text_rect.centerx = self.screen_rect.centerx
        coins_text_rect.y = end_game_text_rect.y + end_game_text_rect.height + int(self.screen_rect.height*0.0065)
        self.screen.blit(coins_text_image,coins_text_rect)

        exp_text = "Заработано опыта: "+ str(exp)
        exp_text_image = self.font.render(exp_text,True,(255,255,255))
        exp_text_rect = exp_text_image.get_rect()
        exp_text_rect.centerx = self.screen_rect.centerx
        exp_text_rect.y = coins_text_rect.y + coins_text_rect.height + int(self.screen_rect.height*0.0065)
        self.screen.blit(exp_text_image,exp_text_rect)



    def blit_act(self,my_choice):
        if not my_choice:
            choice_text ='Выберите элемент:'
        else:
            choice_text ='Ожидайте ход противника'
        choice_image = self.font.render(choice_text,True,self.text_color)
        choice_text_rect = choice_image.get_rect()
        choice_text_rect.x = self.scissors_rect.x - 10
        choice_text_rect.y = self.scissors_rect.y-choice_text_rect.height - 15
        self.screen.blit(choice_image,choice_text_rect)



    def blit_health(self,my_health = 1000,enemy_health = 1000):
        my_health_text = "ХП осталось: " + str(my_health)
        my_health_image = self.font.render(my_health_text,True,self.text_color)
        my_health_text_rect = my_health_image.get_rect()

        my_health_text_rect.x = self.stats_rect.x
        my_health_text_rect.y = self.stats_rect.y - my_health_text_rect.height -10
        self.screen.blit(my_health_image,my_health_text_rect)

        enemy_health_text = "ХП осталось: " + str(enemy_health)
        enemy_health_image = self.font.render(enemy_health_text,True,self.text_color)
        enemy_health_text_rect = enemy_health_image.get_rect()
        enemy_health_text_rect.x = self.stats_en_rect.x
        enemy_health_text_rect.y = self.stats_en_rect.y - enemy_health_text_rect.height -10
        self.screen.blit(enemy_health_image,enemy_health_text_rect)


    def multiplayer_game(self):
        cactus = pygame.transform.scale(self.settings.image_cactus,
                                          (self.settings.cactus_rect_width,self.settings.cactus_rect_height)
                                          )
        self.screen.blit(cactus,self.cactus_rect)
        self.screen.blit(cactus,self.cactus_en_rect)
        pygame.draw.rect(self.screen,(0,255,0),self.stats_rect)
        pygame.draw.rect(self.screen,(0,255,0),self.stats_en_rect)


    def draw_stats_part_rect(self,width = 0,en_width = 0):
        stats_part_rect  =  pygame.Rect(self.cactus_rect.x,
                 self.stats_rect.y,        
                 self.settings.stats_rect_width,    
                 self.settings.stats_rect_height)
        stats_en_part_rect  =  pygame.Rect(self.cactus_en_rect.x,
           self.stats_rect.y,        
           self.settings.stats_rect_width,    
           self.settings.stats_rect_height)
        stats_part_rect.width = width
        stats_en_part_rect.width = en_width
        pygame.draw.rect(self.screen,(255, 0, 0),stats_part_rect)
        pygame.draw.rect(self.screen,(255, 0, 0),stats_en_part_rect)      

