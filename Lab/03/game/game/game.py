from tkinter import *
from PIL import Image, ImageTk
import random

tileset_png = "cell-bgr.png"
blue_png = "ball-blue.png"
aqua_png = "ball-aqua.png"
green_png = "ball-green.png"
pink_png = "ball-pink.png"
red_png = "ball-red.png"
violet_png = "ball-violet.png"
yellow_png = "ball-yellow.png"

def make_tiles(x,y,lbls,number_tile, number_help):
    
    lbls[number_tile].color = number_help
    lbls[number_tile].row = x
    lbls[number_tile].col = y
    lbls[number_tile].tile = number_tile
    lbls[number_tile].bind("<Button-1>", ball_active)
    lbls[number_tile].place(x=lbls[number_tile].row*70 + 10,y=lbls[number_tile].col*70 + 10)
    return lbls

def clipping(img):
    x1 = 1
    y1 = 0
    x2 = 67
    y2 = 66
    new_image = ImageTk.PhotoImage(img.crop((x1,y1,x2, y2)))
    return new_image

def clipping2(img):
    x1 = 1
    y1 = 69
    x2 = 67
    y2 = 135
    new_image = ImageTk.PhotoImage(img.crop((x1,y1,x2, y2)))
    return new_image


def convert(convert_image):
    global tileset_png;
    bgr_image = Image.open(tileset_png).convert('RGBA')
    ball_color = Image.open(convert_image).convert('RGBA')
    bgr_image.paste(ball_color,(6,5),ball_color)
    return bgr_image

def convert2(convert_image):
    global tileset_png;
    bgr_image = Image.open(tileset_png).convert('RGBA')
    ball_color = Image.open(convert_image).convert('RGBA')
    bgr_image.paste(ball_color,(6,74),ball_color)
    return bgr_image



def if_game_start():
    global lbls
    lbls=[]
    global close_tiles
    global first_color, second_color, third_color
    first_color = random.randint(0,6)
    second_color = random.randint(0,6)
    third_color = random.randint(0,6)
    close_tiles=[0]*81
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
    global clicked
    global lbls
    lbls.clear()
    if_game_start()
    set_balls()
    clicked=False

def if_new_game(event):
    global clicked
    global lbls
    global lbl_looser
    lbl_looser.destroy()
    lbls.clear()
    if_game_start()
    set_balls()
    clicked=False

def check_lines_horizontal():
    global lbls

clicked=False
def ball_active(event):
    global clicked
    global close_tiles
    global number_ball_to_move
    global img_tileset
    global lbls
    global active_tile_num
    global ball_active_color
    global active_balls
    global balls
    if clicked==False:
        if event.widget.color != -1:
            event.widget.config(image=active_balls[event.widget.color])
            active_tile_num = event.widget.tile
            ball_active_color = event.widget.color
            clicked = True
    if clicked==True:
        if event.widget.color == -1:
            close_tiles[event.widget.tile] = 1
            close_tiles[active_tile_num] = 0
            event.widget.config(image=balls[ball_active_color])
            event.widget.color=ball_active_color
            lbls[active_tile_num].config(image=img_tileset)
            lbls[active_tile_num].color = -1
            clicked=False
            set_balls()
        else:
            if event.widget.tile != active_tile_num:
                lbls[active_tile_num].config(image=balls[ball_active_color])
                event.widget.config(image=active_balls[event.widget.color])
                active_tile_num = event.widget.tile
                ball_active_color = event.widget.color
def if_click(event):
    set_balls()
    
def set_img_tileset_2(event):
    event.widget.config(image=img_tileset_2)
    global points
    points += 1
    update_score()
    
def update_score():
    global score, points
    score.config(text=points)
    
close_tiles=[0]*81
def set_balls():
    global close_tiles
    global lbls
    global first_color, second_color, third_color
    global lbl_looser
    global balls
    random_color1, random_color2, random_color3 = random.randint(0,6),random.randint(0,6),random.randint(0,6)
    while(True):
        first_tile = random.randint(0,80)
        second_tile = random.randint(0,80)
        third_tile = random.randint(0,80)
        if (close_tiles[first_tile]==0) and (close_tiles[second_tile]==0) and (close_tiles[third_tile]==0) and (first_tile!=second_tile) and (first_tile!=third_tile) and (second_tile!=third_tile):
            break

    x_1 = lbls[first_tile].row
    y_1 = lbls[first_tile].col
    x_2 = lbls[second_tile].row
    y_2 = lbls[second_tile].col
    x_3 = lbls[third_tile].row
    y_3 = lbls[third_tile].col

    lbls[first_tile] = Label(root, image=balls[first_color], borderwidth=0)
    lbls = make_tiles(x_1,y_1,lbls,first_tile,first_color)

    lbls[second_tile] = Label(root, image=balls[second_color], borderwidth=0)
    lbls = make_tiles(x_2,y_2,lbls,second_tile,second_color)

    lbls[third_tile] = Label(root, image=balls[third_color], borderwidth=0)
    lbls = make_tiles(x_3,y_3,lbls,third_tile,third_color) 

    close_tiles[first_tile]=1
    close_tiles[second_tile]=1
    close_tiles[third_tile]=1
    #print(first_tile,lbls[first_tile].row, lbls[first_tile].col)
    first_color,second_color,third_color=random.randint(0,6),random.randint(0,6),random.randint(0,6)
    first_color_lbl=Label(root,image=balls[first_color], borderwidth=0)
    first_color_lbl.place(x=650, y=290)
    second_color_lbl=Label(root,image=balls[second_color], borderwidth=0)
    second_color_lbl.place(x=730, y=290)
    third_color_lbl=Label(root,image=balls[third_color], borderwidth=0)
    third_color_lbl.place(x=810, y=290)
    sum=0
    for i in range(81):
        sum+=close_tiles[i]
        if sum >= 80:
            lbl_looser=Label(root, text="4el, ti...", font=("Arial", 26), bg="#414141", fg="white")
            lbl_looser.bind("<Button-1>", if_new_game)
            lbl_looser.place(x=650,y=600)


root = Tk()
root.configure(bg="#2F4F4F")
root.geometry("940x720")

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
next_move_label.bind("<Button-1>", if_click)

name.place(x=650, y=25)
point.place(x=650, y=90)
help.place(x=650, y=250)
score.place(x=750, y=90)
new_game_label.place(x=650, y=370)
next_move_label.place(x=650, y=440)

tileset = Image.open(tileset_png)
img_tileset = clipping(tileset)
img_tileset_2 = clipping2(tileset)


balls = []
active_balls = []
#РАБОТАЕМ С КАРТИНКАМИ
bgr_blue = convert(blue_png)
img_blue = clipping(bgr_blue)
balls.append(img_blue)
bgr_blue_active = convert2(blue_png)
img_blue_active = clipping2(bgr_blue_active)
active_balls.append(img_blue_active)

bgr_aqua = convert(aqua_png)
img_aqua = clipping(bgr_aqua)
balls.append(img_aqua)
bgr_aqua_active = convert2(aqua_png)
img_aqua_active = clipping2(bgr_aqua_active)
active_balls.append(img_aqua_active)

bgr_green = convert(green_png)
img_green = clipping(bgr_green)
balls.append(img_green)
bgr_green_active = convert2(green_png)
img_green_active = clipping2(bgr_green_active)
active_balls.append(img_green_active)

bgr_pink = convert(pink_png)
img_pink =clipping(bgr_pink)
balls.append(img_pink)
bgr_pink_active = convert2(pink_png)
img_pink_active = clipping2(bgr_pink_active)
active_balls.append(img_pink_active)

bgr_red = convert(red_png)
img_red = clipping(bgr_red)
balls.append(img_red)
bgr_red_active = convert2(red_png)
img_red_active = clipping2(bgr_red_active)
active_balls.append(img_red_active)

bgr_violet = convert(violet_png)
img_violet = clipping(bgr_violet)
balls.append(img_violet)
bgr_violet_active = convert2(violet_png)
img_violet_active = clipping2(bgr_violet_active)
active_balls.append(img_violet_active)

bgr_yellow = convert(yellow_png)
img_yellow = clipping(bgr_yellow)
balls.append(img_yellow)
bgr_yellow_active = convert(yellow_png)
img_yellow_active = clipping2(bgr_yellow_active)
active_balls.append(img_yellow_active)

if_game_start()
set_balls()
root.mainloop()
