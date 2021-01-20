from tkinter import *
from PIL import Image, ImageTk
from random import randint
import math as m
images={
'tileset_png' : "cell-bgr.png",
'blue_png' : "ball-blue.png",
'aqua_png' : "ball-aqua.png",
'green_png' : "ball-green.png",
'pink_png' : "ball-pink.png",
'red_png' : "ball-red.png",
'violet_png' : "ball-violet.png",
'yellow_png' : "ball-yellow.png"
}



def gen_tiles(row,col,lbls,number_tile, number_help):
    
    lbls[number_tile].color = number_help
    lbls[number_tile].row = row
    lbls[number_tile].col = col
    lbls[number_tile].tile = number_tile
    lbls[number_tile].bind("<Button-1>", ball_active)
    lbls[number_tile].place(x=lbls[number_tile].row*70 + 10,y=lbls[number_tile].col*70 + 10)
    return lbls

def gen_tiles_2(row,col,lbls,number_tile, number_help):
    
    lbls[number_tile].color = number_help
    lbls[number_tile].row = row
    lbls[number_tile].col = col
    lbls[number_tile].tile = number_tile
    lbls[number_tile].bind("<Button-1>", ball_active)
    lbls[number_tile].place(x=lbls[number_tile].row*70 + 10,y=lbls[number_tile].col*70 + 10)
    return lbls


def cropping(img):
    x1 = 1
    y1 = 0
    x2 = 67
    y2 = 66
    new_image = ImageTk.PhotoImage(img.crop((x1,y1,x2, y2)))
    return new_image

def cropping_2(img):
    x1 = 1
    y1 = 69
    x2 = 67
    y2 = 135
    new_image = ImageTk.PhotoImage(img.crop((x1,y1,x2, y2)))
    return new_image


def convert(convert_image):
    global tileset_png
    bgr_image = Image.open(tileset_png).convert('RGBA')
    ball_color = Image.open(convert_image).convert('RGBA')
    bgr_image.paste(ball_color,(6,5),ball_color)
    return bgr_image

def convert_2(convert_image):
    global tileset_png
    bgr_image = Image.open(tileset_png).convert('RGBA')
    ball_color = Image.open(convert_image).convert('RGBA')
    bgr_image.paste(ball_color,(6,74),ball_color)
    return bgr_image



def if_game_start():
    global points 
    points = 0
    update_score()
    global lbls
    lbls=[]
    global where_balls
    global help_first_color, help_second_color, help_third_color
    help_first_color = randint(0,6) 
    help_second_color = randint(0,6)
    help_third_color = randint(0,6)
    where_balls=[0]*81
    color_balls = where_balls
    lbl_num=0
    for row in range(9):
        for col in range(9):
            lbl = Label(root, image=img_tileset, borderwidth=0)
            lbl.row=col
            lbl.col=row
            lbl.tile=lbl_num
            lbl.color=-1
            lbl.bind("<Button-1>", ball_active)
            lbl.place(x=(col*70) + 10,
                      y=(row*70) + 10)
            lbls.append(lbl)
            lbl_num+=1

def if_game_restart(event):
    global if_pressed
    global lbls
    global lose_label
    lbls.clear()
    if_game_start()
    gen_balls()
    if_pressed=False
    #lose_label.config(text="")
    lose_label.destroy()



def check_lines_diagonal(k):
    global points
    global img_tileset
    global lbls
    same_color=[]
    i = k
    for i in range(i,81,10):
        if(i < 18):
            k = i
            same_color.append(lbls[i-10])
        if lbls[i].color == lbls[i-10].color:
            same_color.append(lbls[i])
        else:
            if len(same_color)>4:
                for j in range(len(same_color)):
                    if(same_color[j].color != -1):
                        points = points + 2
                        update_score()
                    same_color[j].config(image=img_tileset)
                    same_color[j].color = -1
                    same_color[j].used = False
            same_color.clear()
            same_color.append(lbls[i])
        if(i > 71) and (len(same_color)>4):
            for j in range(len(same_color)):
                if(same_color[j].color != -1):
                    points = points + 2
                    update_score()
                same_color[j].config(image=img_tileset)
                same_color[j].color = -1
                same_color[j].used = False
            same_color.clear()
    if(k < 81):
        check_lines_diagonal(k+1)


def check_lines_diagonal_back(k):
    global points
    global img_tileset
    global lbls
    same_color=[]
    i = k
    for i in range(i,-1,-8):
        if(i > 62 and i!=63):
            k = i
            same_color.append(lbls[i+8])
        #if(i % 9 ==0):
        #    continue
        if lbls[i].color == lbls[i+8].color:
            same_color.append(lbls[i])
        else:
            if len(same_color)>4:
                for j in range(len(same_color)):
                    if(same_color[j].color != -1):
                        points = points + 2
                        update_score()
                    same_color[j].config(image=img_tileset)
                    same_color[j].color = -1
                    same_color[j].used = False
            same_color.clear()
            same_color.append(lbls[i])
        if(i < 9) and (len(same_color)>4):
            for j in range(len(same_color)):
                if(same_color[j].color != -1):
                    points = points + 2
                    update_score()
                same_color[j].config(image=img_tileset)
                same_color[j].color = -1
                same_color[j].used = False
            same_color.clear()
        if(i % 9 ==8)and (len(same_color)>4):
            for j in range(len(same_color)):
                if(same_color[j].color != -1):
                    points = points + 2
                    update_score()
                same_color[j].config(image=img_tileset)
                same_color[j].color = -1
                same_color[j].used = False
            same_color.clear()
        if(i%9 == 8):
            break
    if(k > -1):
        check_lines_diagonal_back(k-1) 


def check_lines_horizontal():
    global points
    global score
    global img_tileset
    global lbls
    same_color=[]
    same_color.append(lbls[0])
    for i in range(1,81):
        if (i%9==0) and (i!=0):
            if len(same_color)>4:
                for j in range(len(same_color)):
                    if(same_color[j].color != -1):
                        points = points + 2
                        update_score()
                    same_color[j].config(image=img_tileset)
                    same_color[j].color = -1
                    same_color[j].used = False
                    
            same_color.clear()
            same_color.append(lbls[i])
        if lbls[i].color == lbls[i-1].color:
            same_color.append(lbls[i])
        else:
            if len(same_color)>4:
                for j in range(len(same_color)):
                    if(same_color[j].color != -1):
                        points = points + 2
                        update_score()
                    same_color[j].config(image=img_tileset)
                    same_color[j].color = -1
                    same_color[j].used = False
            same_color.clear()
            same_color.append(lbls[i])
        if(i == 80) and (len(same_color)>4):
            for j in range(len(same_color)):
                if(same_color[j].color != -1):
                    points = points + 2
                    update_score()
                same_color[j].config(image=img_tileset)
                same_color[j].color = -1
                same_color[j].used = False
            same_color.clear()


def check_lines_vertical():
    global points
    global lbls
    global img_tileset
    matrix_lbl=[]
    index = 0
    for i in range (9):
        temp =[]
        for j in range(9):
            temp.append(lbls[index])
            index +=1
        matrix_lbl.append(temp)
    same_color=[]
    for row in range (9):
        same_color.append(matrix_lbl[0][row])
        for col in range (1,9):
            #if (col==1) :
            #    if len(same_color)>4:
            #        for j in range(len(same_color)):
            #            same_color[j].config(image=img_tile)
            #            same_color[j].color = -1
            #            same_color[j].used = False
                    
            #    same_color.clear()
            #    same_color.append(matrix_lbl[col][row])
            #elif len(same_color)>4:
            #    same_color.clear()
            #    same_color.append(matrix_lbl[col][row])

            if(matrix_lbl[col][row].color==matrix_lbl[col-1][row].color):
                same_color.append(matrix_lbl[col][row])
            else:
                if len(same_color)>4:
                    for j in range(len(same_color)):
                        if(same_color[j].color != -1):
                            points = points + 2
                            update_score()
                        same_color[j].config(image=img_tileset)
                        same_color[j].color = -1
                        same_color[j].used = False
                same_color.clear()
                same_color.append(matrix_lbl[col][row])
            if(col==8) and (len(same_color)>4):
                for j in range(len(same_color)):
                    if(same_color[j].color != -1):
                        points = points + 2
                        update_score()
                    same_color[j].config(image=img_tileset)
                    same_color[j].color = -1
                    same_color[j].used = False
                same_color.clear()
            if(col == 8):
                same_color.clear()
    

if_pressed=False
def ball_active(event):
    global if_pressed
    global where_balls
    global number_ball_to_move
    global img_tileset
    global lbls
    global active_tile_num
    global ball_active_color
    global active_balls
    global balls
    if if_pressed==False:
        if event.widget.color != -1:
            event.widget.config(image=active_balls[event.widget.color])
            active_tile_num = event.widget.tile
            ball_active_color = event.widget.color
            if_pressed = True
    if if_pressed==True:
        if event.widget.color == -1:
            where_balls[event.widget.tile] = 1
            where_balls[active_tile_num] = 0
            event.widget.config(image=balls[ball_active_color])
            event.widget.color=ball_active_color
            lbls[active_tile_num].config(image=img_tileset)
            lbls[active_tile_num].color = -1
            if_pressed=False
            gen_balls()
        else:
            if event.widget.tile != active_tile_num:
                lbls[active_tile_num].config(image=balls[ball_active_color])
                event.widget.config(image=active_balls[event.widget.color])
                active_tile_num = event.widget.tile
                ball_active_color = event.widget.color
def press(event):
    gen_balls()
    
def set_img_tileset_2(event):
    event.widget.config(image=img_tileset_2)
    global points
    points += 1
    update_score()
    
def update_score():
    global score, points
    score.config(text=points)
    
where_balls=[0]*81
color_balls = where_balls
def gen_balls():
    global color_balls
    global where_balls
    global lbls
    global help_first_color, help_second_color, help_third_color
    global lose_label
    global balls

    while(True):
        first_tile = randint(0,80)
        second_tile = randint(0,80)
        third_tile = randint(0,80)
        if (where_balls[first_tile]==0) and (where_balls[second_tile]==0) and (where_balls[third_tile]==0) and (first_tile!=second_tile) and (first_tile!=third_tile) and (second_tile!=third_tile):
            break
    row_1 = lbls[first_tile].row
    col_1 = lbls[first_tile].col
    row_2 = lbls[second_tile].row
    col_2 = lbls[second_tile].col
    row_3 = lbls[third_tile].row
    col_3 = lbls[third_tile].col

    lbls[first_tile] = Label(root, image=balls[help_first_color], borderwidth=0)
    lbls = gen_tiles(row_1,col_1,lbls,first_tile,help_first_color)

    lbls[second_tile] = Label(root, image=balls[help_second_color], borderwidth=0)
    lbls = gen_tiles(row_2,col_2,lbls,second_tile,help_second_color)

    lbls[third_tile] = Label(root, image=balls[help_third_color], borderwidth=0)
    lbls = gen_tiles(row_3,col_3,lbls,third_tile,help_third_color) 

    where_balls[first_tile]=1
    where_balls[second_tile]=1
    where_balls[third_tile]=1

    color_balls[first_tile] = help_first_color
    color_balls[second_tile] = help_second_color
    color_balls[third_tile] = help_third_color

    check_lines_horizontal()
    check_lines_vertical()
    check_lines_diagonal(9)
    check_lines_diagonal_back(70)


    #print(first_tile,lbls[first_tile].row, lbls[first_tile].col)
    help_first_color,help_second_color,help_third_color=randint(0,6),randint(0,6),randint(0,6)
    help_first_color_lbl=Label(root,image=balls[help_first_color], borderwidth=0)
    help_first_color_lbl.place(x=650, y=290)
    help_second_color_lbl=Label(root,image=balls[help_second_color], borderwidth=0)
    help_second_color_lbl.place(x=730, y=290)
    help_third_color_lbl=Label(root,image=balls[help_third_color], borderwidth=0)
    help_third_color_lbl.place(x=810, y=290)
    busy=0
    for i in range(81):
        if(lbls[i].color == -1):
            busy+=1
            if busy > 78:
                lose_label=Label(root, text="Вы проиграли", font=("Arial", 20), bg="#414141", fg="white")
                lose_label.place(x=650,y=600)
    


root = Tk()
root.configure(bg="#2F4F4F")
root.geometry("900x646")

points=0
name=Label(root, text="Шарики", font=("Arial", 26), bg="#414141", fg="white")
point=Label(root, text="Счёт: ", font=("Arial", 26), bg="#414141", fg="white")
help=Label(root, text="Подсказка: ", font=("Arial", 16), bg="#414141", fg="white")
new_game_label = Label(root,text="Новая игра", font=("Arial", 26), bg="#414141", fg="white")
next_move_label=Label(root,text="Сделать ход", font=("Arial", 24), bg="#414141", fg="white")
score=Label(root, text=points, font=("Arial", 26), bg="#414141", fg="white")
new_game_label = Label(root,text="Новая игра", font=("Arial", 26), bg="#414141", fg="white")
next_move_label=Label(root,text="Сделать ход", font=("Arial", 24), bg="#414141", fg="white")
new_game_label.bind("<Button-1>", if_game_restart)
next_move_label.bind("<Button-1>", press)

name.place(x=650, y=25)
point.place(x=650, y=90)
help.place(x=650, y=250)
score.place(x=750, y=90)
new_game_label.place(x=650, y=370)
next_move_label.place(x=650, y=440)

tileset_png = images['tileset_png']
tileset = Image.open(images['tileset_png'])
img_tileset = cropping(tileset)
img_tileset_2 = cropping_2(tileset)



balls = []
active_balls = []
#РАБОТАЕМ С КАРТИНКАМИ
bgr_blue = convert(images['blue_png'])
img_blue = cropping(bgr_blue)
balls.append(img_blue)
bgr_blue_2 = convert_2(images['blue_png'])
img_blue_2 = cropping_2(bgr_blue_2)
active_balls.append(img_blue_2)

bgr_aqua = convert(images['aqua_png'])
img_aqua = cropping(bgr_aqua)
balls.append(img_aqua)
bgr_aqua_2 = convert_2(images['aqua_png'])
img_aqua_2 = cropping_2(bgr_aqua_2)
active_balls.append(img_aqua_2)

bgr_green = convert(images['green_png'])
img_green = cropping(bgr_green)
balls.append(img_green)
bgr_green_2 = convert_2(images['green_png'])
img_green_2 = cropping_2(bgr_green_2)
active_balls.append(img_green_2)

bgr_pink = convert(images['pink_png'])
img_pink =cropping(bgr_pink)
balls.append(img_pink)
bgr_pink_2 = convert_2(images['pink_png'])
img_pink_2 = cropping_2(bgr_pink_2)
active_balls.append(img_pink_2)

bgr_red = convert(images['red_png'])
img_red = cropping(bgr_red)
balls.append(img_red)
bgr_red_2 = convert_2(images['red_png'])
img_red_2 = cropping_2(bgr_red_2)
active_balls.append(img_red_2)

bgr_violet = convert(images['violet_png'])
img_violet = cropping(bgr_violet)
balls.append(img_violet)
bgr_violet_2 = convert_2(images['violet_png'])
img_violet_2 = cropping_2(bgr_violet_2)
active_balls.append(img_violet_2)

bgr_yellow = convert(images['yellow_png'])
img_yellow = cropping(bgr_yellow)
balls.append(img_yellow)
bgr_yellow_2 = convert(images['yellow_png'])
img_yellow_2 = cropping_2(bgr_yellow_2)
active_balls.append(img_yellow_2)

if_game_start()
gen_balls()
root.mainloop()
