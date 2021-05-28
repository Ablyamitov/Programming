import pygame

class Registration():

    def __init__(self,main):
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = main.settings
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        self.color = pygame.Color('lightskyblue3')
        self.rect = pygame.Rect(self.settings.center_x-50,self.settings.center_y - self.settings.center_y/12,100,32)
        self.rect_password = pygame.Rect(self.rect.x,self.settings.center_y/12 + self.settings.center_y,100,32)
        self.image_cur = pygame.transform.scale(self.settings.image_cur,
                  (self.settings.image_cur_rect.width,30)
                  )

        self.image_enter_reg = self.settings.image_enter_reg
        self.enter_reg_rect  =self.image_enter_reg.get_rect()
        self.enter_reg_rect.centerx = self.screen_rect.centerx
        self.enter_reg_rect.y = self.rect_password.y +self.rect_password.height+ int(self.screen_rect.height *0.011)



    def draw_interface(self):
        pygame.draw.rect(self.screen,self.color,self.rect,2)
        pygame.draw.rect(self.screen,self.color,self.rect_password,2)

    def show_enter(self):
        '''Выводит перед вводом логина и пароля 'Дай мне свой логин или пароль соответственно'''
        enter_login = 'Придумайте логин:'
        enter_login_image = self.font.render(enter_login,True,self.text_color)
        enter_login_rect = enter_login_image.get_rect()
        enter_login_rect.midright = self.rect.midleft
        enter_login_rect.x -=15
        self.screen.blit(enter_login_image,enter_login_rect)
        enter_password = 'Придумайте пароль:'
        enter_password_image = self.font.render(enter_password,True,self.text_color)
        enter_password_rect = enter_password_image.get_rect()
        enter_password_rect.midright = self.rect_password.midleft
        enter_password_rect.x -=15
        self.screen.blit(enter_password_image,enter_password_rect)

    def show_resp(self,access):
        if access == False:
            resp = 'Такой пользователь уже есть'
            resp_image = self.font.render(resp,True,(self.text_color))
            resp_rect = resp_image.get_rect()
            resp_rect.midbottom = self.screen_rect.midbottom
            self.screen.blit(resp_image,resp_rect)

    def blit_registration(self):
        font = pygame.font.SysFont(None,72)
        registration_text = "Регистрация"
        registration_image = font.render(registration_text,True,self.text_color)
        registration_rect = registration_image.get_rect()
        registration_rect.midtop = self.screen_rect.midtop
        self.screen.blit(registration_image,registration_rect)


    def show_enter_reg_button(self):
        self.screen.blit(self.image_enter_reg,self.enter_reg_rect)

        