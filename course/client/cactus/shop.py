import pygame

class Shop():

    def __init__(self,main):

        self.screen = main.screen
        self.settings = main.settings
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (255,255,255)
        self.button_color = (0,0,0)

        self.box_cactus = pygame.transform.scale(self.settings.box_cactus,
                          (self.settings.cactus_rect_width,self.settings.cactus_rect_height))

        self.cowboy_cactus = pygame.transform.scale(self.settings.cowboy_cactus,
                                          (self.settings.cactus_rect_width,self.settings.cactus_rect_height)) 

        self.cute_cactus = pygame.transform.scale(self.settings.cute_cactus,
            (self.settings.cactus_rect_width,self.settings.cactus_rect_height))             


        self.cactus_rect  =  pygame.Rect(self.settings.cactus_rect_x,
                                        self.settings.cactus_rect_y,        
                                        self.settings.cactus_rect_width,    
                                        self.settings.cactus_rect_height)

        self.box_cactus_rect = self.box_cactus.get_rect()
        self.box_cactus_rect.center = self.screen_rect.center
        self.box_cactus_rect.x =  int(self.screen_rect.width * 0.05)
        self.box_cactus_rect.y = self.box_cactus_rect.y - int(self.screen_rect.height*0.1114)

        self.cowboy_cactus_rect = self.cowboy_cactus.get_rect()
        self.cowboy_cactus_rect.center = self.screen_rect.center
        self.cowboy_cactus_rect.y = self.cowboy_cactus_rect.y + int(self.screen_rect.height*0.0357)
        #self.cowboy_cactus_rect.x =  self.box_cactus_rect.x + self.box_cactus_rect.width + int(0.1 * self.screen_rect.width)

        self.cute_cactus_rect = self.cute_cactus.get_rect()
        self.cute_cactus_rect.center = self.screen_rect.center
        self.cute_cactus_rect.x =  int(self.screen_rect.width/1.065) - self.cute_cactus_rect.width
        self.cute_cactus_rect.y =  self.cute_cactus_rect.y - int(self.screen_rect.height*0.1429)




    def blit_all_cactus(self):
        self.screen.blit(self.box_cactus,self.box_cactus_rect)
        box_name = "Боксёр"
        box_name_image = self.font.render(box_name,True,(255,255,255))
        box_rect= box_name_image.get_rect()
        box_rect.midbottom = self.box_cactus_rect.midtop
        box_rect.y = box_rect.y + int(self.screen_rect.height * 0.0714)
        self.screen.blit(box_name_image,box_rect)
        box_cost = "Стоимость: 100 монет"
        box_cost_image = self.font.render(box_cost,True,(255,255,255))
        box_cost_rect = box_cost_image.get_rect()
        box_cost_rect.midtop = self.box_cactus_rect.midbottom
        box_cost_rect.y = box_cost_rect.y - int(self.screen_rect.height*0.0357)
        self.screen.blit(box_cost_image,box_cost_rect)

        self.screen.blit(self.cowboy_cactus,self.cowboy_cactus_rect)
        cowboy_name = "Эль Примо"
        cowboy_name_image = self.font.render(cowboy_name,True,(255,255,255))
        cowboy_rect= cowboy_name_image.get_rect()
        cowboy_rect.midbottom = self.cowboy_cactus_rect.midtop
        self.screen.blit(cowboy_name_image,cowboy_rect)
        cowboy_cost = "Стоимость: 300 монет"
        cowboy_cost_image = self.font.render(cowboy_cost,True,(255,255,255))
        cowboy_cost_rect = cowboy_cost_image.get_rect()
        cowboy_cost_rect.midtop = self.cowboy_cactus_rect.midbottom
        self.screen.blit(cowboy_cost_image,cowboy_cost_rect)

        self.screen.blit(self.cute_cactus,self.cute_cactus_rect)
        cute_name = "Милашка"
        cute_name_image = self.font.render(cute_name,True,(255,255,255))
        cute_rect= cute_name_image.get_rect()
        cute_rect.midbottom = self.cute_cactus_rect.midtop
        self.screen.blit(cute_name_image,cute_rect)
        cute_cost = "Стоимость: 200 монет"
        cute_cost_image = self.font.render(cute_cost,True,(255,255,255))
        cute_cost_rect = cute_cost_image.get_rect()
        cute_cost_rect.midtop = self.cute_cactus_rect.midbottom
        self.screen.blit(cute_cost_image,cute_cost_rect)

        buy = "Купить"
        buy_image = self.font.render(buy,True,(255,255,255),self.button_color)
        buy_box_rect = buy_image.get_rect()
        buy_cowboy_rect = buy_image.get_rect()
        buy_cute_rect = buy_image.get_rect()
        buy_box_rect.midtop = box_cost_rect.midbottom
        buy_cowboy_rect.midtop = cowboy_cost_rect.midbottom
        buy_cute_rect.midtop = cute_cost_rect.midbottom
        buy_box_rect.y = buy_box_rect.y + int(self.screen_rect.height * 0.0286)
        buy_cowboy_rect.y = buy_cowboy_rect.y + int(self.screen_rect.height * 0.0286)
        buy_cute_rect.y = buy_cute_rect.y+int(self.screen_rect.height * 0.0286)
        self.screen.blit(buy_image,buy_box_rect)
        self.screen.blit(buy_image,buy_cowboy_rect)
        self.screen.blit(buy_image,buy_cute_rect)