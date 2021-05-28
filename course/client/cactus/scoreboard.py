import pygame.font
from pygame.sprite import Group

class Scoreboard():
    '''Класс для вывода игровой информации'''

    def __init__(self,main):
        '''Инициализирует атрибуты подсчета очков'''
        self.main = main
        self.screen = main.screen
        self.stats = main.stats
        self.screen_rect = self.screen.get_rect()
        self.settings = main.settings
        self.stats = main.stats

        self.instruction = 'Инструкция к игре: снизу экрана располагается прямоугольник, по которому двигаются стрелочки.'
        self.instruction2 = 'Ваша задача: успеть нажать на соответствующую стрелочке клавишу, когда она будет находится внутри выделенного квадрата.'
        self.instruction3 = 'При успешном попадании начисляются 50 очков, при промахе - отнимаются 10 очков.'
        self.instruction4 = 'При достижении 250 очков начинается поливка кактуса, а очки сбрасываются.'
        self.instruction5 = 'Главная цель: как можно больше полить кактус.'
        self.instruction6 = 'Чтобы начать игру, нажмите клавишу SPACE или кликните по прямоугольнику "Play", выход - клавиша ESC.'
        self.countdown = 3

        #Настройка шрифта для вывода счёта.
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.ins_font = pygame.font.SysFont(None,34)

        #Подготовка исходного изображения.
        self.prep_score()



    def prep_score(self):
        '''Преобразует текущий счёт  в графическое изображение.'''
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color)

        #Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        


    def write_instruction(self):
        '''Инструкция в начале игры и её вывод'''
        self.instruction_image = self.ins_font.render(self.instruction,True,self.text_color)
        self.instruction_rect = self.instruction_image.get_rect()
        self.instruction_rect.x = 20
        self.instruction_rect.y = 50
        self.screen.blit(self.instruction_image,self.instruction_rect)

        self.instruction_image2 = self.ins_font.render(self.instruction2,True,self.text_color)
        self.instruction_rect2 = self.instruction_image2.get_rect()
        self.instruction_rect2.x = 20
        self.instruction_rect2.y = self.instruction_rect.y * 2
        self.screen.blit(self.instruction_image2,self.instruction_rect2)

        self.instruction_image3 = self.ins_font.render(self.instruction3,True,self.text_color)
        self.instruction_rect3 = self.instruction_image3.get_rect()
        self.instruction_rect3.x = 20
        self.instruction_rect3.y = self.instruction_rect.y * 3
        self.screen.blit(self.instruction_image3,self.instruction_rect3)

        self.instruction_image4 = self.ins_font.render(self.instruction4,True,self.text_color)
        self.instruction_rect4 = self.instruction_image4.get_rect()
        self.instruction_rect4.x = 20
        self.instruction_rect4.y = self.instruction_rect.y * 4
        self.screen.blit(self.instruction_image4,self.instruction_rect4)

        self.instruction_image5 = self.ins_font.render(self.instruction5,True,self.text_color)
        self.instruction_rect5 = self.instruction_image5.get_rect()
        self.instruction_rect5.x = 20
        self.instruction_rect5.y = self.instruction_rect.y * 5
        self.screen.blit(self.instruction_image5,self.instruction_rect5)

        self.instruction_image6 = self.ins_font.render(self.instruction6,True,self.text_color)
        self.instruction_rect6 = self.instruction_image6.get_rect()
        self.instruction_rect6.x = 20
        self.instruction_rect6.y = self.instruction_rect.y * 6
        self.screen.blit(self.instruction_image6,self.instruction_rect6)


    def show_countdown(self,sec):
        sec_str = str(sec)
        self.countdown_image = self.font.render(sec_str,True,self.text_color)
        self.countdown_rect =  self.countdown_image.get_rect()
        self.countdown_rect.center = self.screen_rect.center
        self.screen.blit(self.countdown_image,self.countdown_rect)


    def show_timer(self,sec):
        if sec > 10:
            text_color = (30,30,30)
        else: 
            text_color = (255, 0, 0)
        sec_str = str(sec)
        timer_str = 'Времени осталось : ' + sec_str
        self.timer_image = self.font.render(timer_str,True,text_color)
        self.timer_rect =  self.timer_image.get_rect()
        self.timer_rect.midtop = self.screen_rect.midtop
        self.timer_rect.y = 5
        self.screen.blit(self.timer_image,self.timer_rect)


    def show_score(self):
        '''Выводит очки на экране.'''
        self.screen.blit(self.score_image,self.score_rect)


    def show_all_score(self):
        all_score_str = 'Всего очков: '+ str(self.stats.all_score)
        self.all_score_image = self.font.render(all_score_str,True,self.text_color)
        self.all_score_rect = self.score_image.get_rect()
        self.all_score_rect.left = self.screen_rect.left + 20
        self.all_score_rect.top = 20
        self.screen.blit(self.all_score_image, self.all_score_rect)

    def end_game(self):
        self.end_image = self.stats.font.render(self.stats.end,True,self.stats.text_color)
        self.end_rect = self.end_image.get_rect()
        self.end_rect.center = self.screen_rect.center
        self.end_rect.x  = self.end_rect.x - (self.end_rect.width/2)
        self.end_rect.y = self.end_rect.y - 100
        self.screen.blit(self.end_image,self.end_rect)
        points_scored = f'Набрано очков: {self.stats.all_score}'
        points_image = self.stats.font.render(points_scored,True,self.stats.text_color)
        points_rect = points_image.get_rect()
        points_rect.x = self.end_rect.x - 25
        points_rect.y = self.end_rect.y + self.end_rect.height + 50
        self.screen.blit(points_image,points_rect)
        watering_count = f'Кактус удалось полить количество раз: {self.stats.wat_count}'
        watering_image = self.stats.font.render(watering_count,True,self.stats.text_color)
        watering_rect = watering_image.get_rect()
        watering_rect.x = points_rect.x - 100
        watering_rect.y = points_rect.y + self.end_rect.height + 50
        self.screen.blit(watering_image,watering_rect)

        back_to_menu = 'Чтобы выйти в меню, нажмите клавишу ESC'
        back_to_menu_image = self.stats.font.render(back_to_menu,True,self.stats.text_color)
        back_to_menu_rect = back_to_menu_image.get_rect()
        back_to_menu_rect.x = watering_rect.x - 100
        back_to_menu_rect.y = self.settings.screen_height - 150
        self.screen.blit(back_to_menu_image,back_to_menu_rect)



    

