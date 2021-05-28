import pygame
import pygame.font
class Menu():
     
   def __init__ (self,main):
      self.screen = main.screen
      self.settings = main.settings
      self.screen_rect = self.screen.get_rect()
      self.singleplayer = pygame.transform.scale(self.settings.image_singleplayer,
               (self.settings.singleplayer_rect_width,self.settings.singleplayer_rect_height)
               )
      
      self.multiplayer = pygame.transform.scale(self.settings.image_multiplayer,
         (self.settings.multiplayer_rect_width,self.settings.multiplayer_rect_height)
         )
      
      self.shop = pygame.transform.scale(self.settings.image_shop,
         (self.settings.shop_rect_width,self.settings.shop_rect_height)
         )
      
      self.singleplayer_rect = pygame.Rect(self.settings.singleplayer_rect_x,
                     self.settings.singleplayer_rect_y,           
                     self.settings.singleplayer_rect_width,       
                     self.settings.singleplayer_rect_height)

      self.multiplayer_rect = pygame.Rect(self.settings.multiplayer_rect_x,
                        self.settings.multiplayer_rect_y,           
                        self.settings.multiplayer_rect_width,       
                        self.settings.multiplayer_rect_height)
   
      self.shop_rect = pygame.Rect(self.settings.shop_rect_x,
               self.settings.shop_rect_y,           
               self.settings.shop_rect_width,       
               self.settings.shop_rect_height)

      self.font = pygame.font.SysFont(None,48,bold = False,italic = True)
      self.text_color = (255,255,255)
      self.text = 'SEE YOU CACTUS COWBOY...'

      ###################УДАЛИТЬ ОТСЮДА
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


      ################ ДО ЭТОГО МОМЕНТА

   def blit_menu(self):
      self.screen.blit(self.singleplayer,self.singleplayer_rect)
      self.screen.blit(self.multiplayer,self.multiplayer_rect)
      self.screen.blit(self.shop,self.shop_rect)


   def show_bebop(self):
      '''See you Cactus cowboy'''
      self.text_image = self.font.render(self.text,True,self.text_color)
      self.text_rect = self.text_image.get_rect()
      self.text_rect.bottomright = self.screen_rect.bottomright
      self.screen.blit(self.text_image,self.text_rect)

      relax_txt = "Магазин в отпуске"
      relax_image = self.font.render(relax_txt,True,self.text_color)
      relax_rect = relax_image.get_rect()
      relax_rect.center = self.screen_rect.center
      self.screen.blit(relax_image,relax_rect)

   

   #############УДАЛИТЬ С ЭТОГО МОМЕНТА
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


      ###################ДО ЭТОГО МОМЕНТА

   def draw_hi(self,login):
      greeting  = f"Приветствую, {login}"
      greeting_image = self.font.render(greeting,True,(0,0,0))
      greeting_rect = greeting_image.get_rect()
      greeting_rect.midtop = self.screen_rect.midtop
      self.screen.blit(greeting_image,greeting_rect)
        