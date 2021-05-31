import pygame
import copy

class Authorization():
    
    def __init__(self,main):
        self.screen = main.screen
        self.settings = main.settings
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255,255,255)
        self.button_color = (255,255,0)
        self.font = pygame.font.SysFont(None,48)
        self.color = pygame.Color('lightskyblue3')
        self.rect = pygame.Rect(self.settings.center_x-50,self.settings.center_y - self.settings.center_y/12,100,32)
        self.rect_password = pygame.Rect(self.rect.x,self.settings.center_y/12 + self.settings.center_y,100,32)
        

        self.image_cur = pygame.transform.scale(self.settings.image_cur,
                          (self.settings.image_cur_rect.width,30)
                          )
        self.image_reg = pygame.transform.scale(self.settings.image_registration,
                            (int(self.screen_rect.width*0.25) ,int(self.screen_rect.height*0.1))
                            )

        self.reg_rect = self.image_reg.get_rect()
        self.reg_rect.midbottom = self.screen_rect.midbottom

        self.image_enter = self.settings.image_enter
        self.enter_rect  =self.image_enter.get_rect()
        self.enter_rect.centerx = self.screen_rect.centerx
        self.enter_rect.y = self.rect_password.y +self.rect_password.height+ int(self.screen_rect.height *0.011)


    def draw_rect(self):
        
        pygame.draw.rect(self.screen,self.color,self.rect,2)
        pygame.draw.rect(self.screen,self.color,self.rect_password,2)

    def show_enter(self):
        '''Выводит перед вводом логина и пароля 'Дай мне свой логин или пароль соответственно'''
        enter_login = 'Введите логин:'
        enter_login_image = self.font.render(enter_login,True,self.text_color)
        enter_login_rect = enter_login_image.get_rect()
        enter_login_rect.midright = self.rect.midleft
        enter_login_rect.x -=15
        self.screen.blit(enter_login_image,enter_login_rect)

        enter_password = 'Введите пароль:'
        enter_password_image = self.font.render(enter_password,True,self.text_color)
        enter_password_rect = enter_password_image.get_rect()
        enter_password_rect.midright = self.rect_password.midleft
        enter_password_rect.x -=15
        self.screen.blit(enter_password_image,enter_password_rect)


    def show_resp(self,access):
        if access == True:
            resp = 'Такой пользователь существует'
        else:
            resp = 'Такого пользователя нет'
        resp_image = self.font.render(resp,True,(self.text_color))
        resp_rect = resp_image.get_rect()
        resp_rect.centerx = self.screen_rect.centerx
        resp_rect.y = self.enter_rect.y + self.enter_rect.width + 10
        self.screen.blit(resp_image,resp_rect)



    def blit_autorizhation(self):
        font = pygame.font.SysFont(None,72)
        authorization_text = "Авторизация"
        authorization_image = font.render(authorization_text,True,self.text_color)
        authorization_rect = authorization_image.get_rect()
        authorization_rect.midtop = self.screen_rect.midtop
        self.screen.blit(authorization_image,authorization_rect)

    def show_reg_button(self):
        self.screen.blit(self.image_reg,self.reg_rect)

    def show_enter_button(self):
        self.screen.blit(self.image_enter,self.enter_rect)
    
        
