from tkinter import *
from PIL import Image, ImageTk
import random

def starting_game():
    global all_lbl
    global help1, help2, help3
    help1 = random.randint(0,6)
    help2 = random.randint(0,6)
    help3 = random.randint(0,6)
    all_lbl=[]
    lbl_num=0
    for row in range(9):
        for col in range(9):
            lbl = Label(root, image=img_tile, borderwidth=0)
            lbl.row=col
            lbl.col=row
            lbl.tile=lbl_num
            lbl.color=-1
            lbl.used=False
            lbl.bind("<Button-1>", ball_active)
            lbl.place(x=(col*70) + 10,
                      y=(row*70) + 10)
            all_lbl.append(lbl)
            lbl_num+=1

def restarting_game(event):
    global clicked
    global all_lbl
    global lbl_looser
    global img_tile
    lbl_looser=Label(root, text='                                                         ', font=('Arial', 40), bg="#414141")
    lbl_looser.place(x=650, y=600)
    all_lbl.clear()
    starting_game()
    set_balls()
    clicked=False


#def check_lines_diagonal_left_right_1():
#    global all_lbl
#    matrix_lbl=[]
#    index = 0
#    for i in range (9):
#        temp =[]
#        for j in range(9):
#            temp.append(all_lbl[index])
#            index +=1
#        matrix_lbl.append(temp)
#    same_color=[]
#    max_col = 9
#    max_row = 9
#    for row in range (1,max_row):
#        k = row
#        same_color.append(matrix_lbl[0][k])
#        for col in range (max_col): 
#            k = k+1
#            if(matrix_lbl[k][col].color==matrix_lbl[k-1][col-1].color):
#                same_color.append(matrix_lbl[k][col])
#            else:
#                if len(same_color)>4:
#                    for j in range(len(same_color)):
#                        same_color[j].config(image=img_tile)
#                        same_color[j].color = -1
#                        same_color[j].used = False
#                same_color.clear()
#                same_color.append(matrix_lbl[col][col])
#            if(k==8) and (len(same_color)>4):
#                for j in range(len(same_color)):
#                    same_color[j].config(image=img_tile)
#                    same_color[j].color = -1
#                    same_color[j].used = False
#                same_color.clear()
#            if(k == 8):
#                same_color.clear()

#def check_lines_diagonal_left_right_down():
#    global all_lbl
#    matrix_lbl=[]
#    index = 0
#    for i in range (9):
#        temp =[]
#        for j in range(9):
#            temp.append(all_lbl[index])
#            index +=1
#        matrix_lbl.append(temp)
#    same_color=[]
#    for row in range (5):
#        k = row
#        same_color.append(matrix_lbl[0][k])
#        for col in range (6,9): 
#            k = k+1
#            if(matrix_lbl[col][k].color==matrix_lbl[col-1][k-1].color):
#                same_color.append(matrix_lbl[col][k])
#            else:
#                if len(same_color)>4:
#                    for j in range(len(same_color)):
#                        same_color[j].config(image=img_tile)
#                        same_color[j].color = -1
#                        same_color[j].used = False
#                same_color.clear()
#                same_color.append(matrix_lbl[col][k])
#            if(col==8) and (len(same_color)>4):
#                for j in range(len(same_color)):
#                    same_color[j].config(image=img_tile)
#                    same_color[j].color = -1
#                    same_color[j].used = False
#                same_color.clear()
#            if(col == 8):
#                same_color.clear()



#def check_lines_diagonal_right_left_up():          работает область, но не всё
#    global all_lbl
#    matrix_lbl=[]
#    index = 0
#    for i in range (9):
#        temp =[]
#        for j in range(9):
#            temp.append(all_lbl[index])
#            index +=1
#        matrix_lbl.append(temp)
#    same_color=[]
#    for row in range (8,3,-1):
#        k = row
#        same_color.append(matrix_lbl[0][k])
#        for col in range (1,5): 
#            k = k-1
#            if(matrix_lbl[col][k].color==matrix_lbl[col-1][k+1].color):
#                same_color.append(matrix_lbl[col][k])
#            else:
#                if len(same_color)>4:
#                    for j in range(len(same_color)):
#                        same_color[j].config(image=img_tile)
#                        same_color[j].color = -1
#                        same_color[j].used = False
#                same_color.clear()
#                same_color.append(matrix_lbl[col][k])
#            if(col==4) and (len(same_color)>4):
#                for j in range(len(same_color)):
#                    same_color[j].config(image=img_tile)
#                    same_color[j].color = -1
#                    same_color[j].used = False
#                same_color.clear()
#            if(col == 4):
#                same_color.clear()





    
    






def check_lines_vertical():
    global all_lbl
    matrix_lbl=[]
    index = 0
    for i in range (9):
        temp =[]
        for j in range(9):
            temp.append(all_lbl[index])
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
                        same_color[j].config(image=img_tile)
                        same_color[j].color = -1
                        same_color[j].used = False
                same_color.clear()
                same_color.append(matrix_lbl[col][row])
            if(col==8) and (len(same_color)>4):
                for j in range(len(same_color)):
                    same_color[j].config(image=img_tile)
                    same_color[j].color = -1
                    same_color[j].used = False
                same_color.clear()
            if(col == 8):
                same_color.clear()

        








    
def check_lines_horizontal():
    global all_lbl
    same_color=[]
    same_color.append(all_lbl[0])
    for i in range(1,81):
        if (i%9==0) and (i!=0):
            if len(same_color)>4:
                for j in range(len(same_color)):
                    same_color[j].config(image=img_tile)
                    same_color[j].color = -1
                    same_color[j].used = False
                    
            same_color.clear()
            same_color.append(all_lbl[i])
        if all_lbl[i].color == all_lbl[i-1].color:
            same_color.append(all_lbl[i])
        else:
            if len(same_color)>4:
                for j in range(len(same_color)):
                    same_color[j].config(image=img_tile)
                    same_color[j].color = -1
                    same_color[j].used = False
            same_color.clear()
            same_color.append(all_lbl[i])
        if(i == 80) and (len(same_color)>4):
            for j in range(len(same_color)):
                    same_color[j].config(image=img_tile)
                    same_color[j].color = -1
                    same_color[j].used = False
            same_color.clear()


clicked=False
def ball_active(event):
    global clicked
    global img_tile
    global all_lbl
    global active_tile_num
    global ball_active_color
    global img_blue_active, img_aqua_active, img_green_active, img_pink_active, img_red_active, img_violet_active, img_yellow_active
    ball_active=[img_blue_active,img_aqua_active,img_green_active,img_pink_active,img_red_active,img_violet_active,img_yellow_active]
    global img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow
    balls = [img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow]
    if clicked==False:
        if event.widget.color != -1:
            event.widget.config(image=ball_active[event.widget.color])
            active_tile_num = event.widget.tile
            ball_active_color = event.widget.color
            clicked = True
    if clicked==True:
        if event.widget.color == -1:
            event.widget.used = True
            all_lbl[active_tile_num].used = False
            event.widget.config(image=balls[ball_active_color])
            event.widget.color=ball_active_color
            all_lbl[active_tile_num].config(image=img_tile)
            all_lbl[active_tile_num].color = -1
            clicked=False
            set_balls()
        else:
            if event.widget.tile != active_tile_num:
                all_lbl[active_tile_num].config(image=balls[ball_active_color])
                event.widget.config(image=ball_active[event.widget.color])
                active_tile_num = event.widget.tile
                ball_active_color = event.widget.color
                
def next_move(event):
    set_balls()
    
def set_img_tile_active(event):
    event.widget.config(image=img_tile_active)
    global x_score
    x_score += 1
    update_score()
    
def update_score():
    global score, x_score
    score.config(text=x_score)
    
def set_balls():
    global all_lbl
    global help1, help2, help3
    global lbl_looser
    global img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow
    balls = [img_blue, img_aqua, img_green, img_pink, img_red, img_violet, img_yellow]
    bool=True
    while(bool):
        random_tile1 = random.randint(0,80)
        random_tile2 = random.randint(0,80)
        random_tile3 = random.randint(0,80)
        if (all_lbl[random_tile1].used==False) and (all_lbl[random_tile2].used==False) and (all_lbl[random_tile3].used==False) and (random_tile1!=random_tile2) and (random_tile1!=random_tile3) and (random_tile2!=random_tile3):
            bool=False
    x1 = all_lbl[random_tile1].row
    y1 = all_lbl[random_tile1].col
    x2 = all_lbl[random_tile2].row
    y2 = all_lbl[random_tile2].col
    x3 = all_lbl[random_tile3].row
    y3 = all_lbl[random_tile3].col
    all_lbl[random_tile1] = Label(root, image=balls[help1], borderwidth=0)
    all_lbl[random_tile1].color = help1
    all_lbl[random_tile1].row = x1
    all_lbl[random_tile1].col = y1
    all_lbl[random_tile1].tile = random_tile1
    all_lbl[random_tile1].used = True
    all_lbl[random_tile1].bind("<Button-1>", ball_active)
    all_lbl[random_tile1].place(x=all_lbl[random_tile1].row*70 + 10,y=all_lbl[random_tile1].col*70 + 10)
    all_lbl[random_tile2] = Label(root, image=balls[help2], borderwidth=0)
    all_lbl[random_tile2].color = help2
    all_lbl[random_tile2].row = x2
    all_lbl[random_tile2].col = y2
    all_lbl[random_tile2].tile = random_tile2
    all_lbl[random_tile2].used = True
    all_lbl[random_tile2].bind("<Button-1>", ball_active)
    all_lbl[random_tile2].place(x=all_lbl[random_tile2].row*70 + 10,y=all_lbl[random_tile2].col*70 + 10)
    all_lbl[random_tile3] = Label(root, image=balls[help3], borderwidth=0)
    all_lbl[random_tile3].color = help3
    all_lbl[random_tile3].row = x3
    all_lbl[random_tile3].col = y3
    all_lbl[random_tile3].tile = random_tile3
    all_lbl[random_tile3].used = True
    all_lbl[random_tile3].bind("<Button-1>", ball_active)
    all_lbl[random_tile3].place(x=all_lbl[random_tile3].row*70 + 10,y=all_lbl[random_tile3].col*70 + 10)
    print( random_tile1,all_lbl[random_tile1].row, all_lbl[random_tile1].col)
    help1,help2,help3=random.randint(0,6),random.randint(0,6),random.randint(0,6)
    help1_lbl=Label(root,image=balls[help1], borderwidth=0)
    help1_lbl.place(x=650, y=290)
    help2_lbl=Label(root,image=balls[help2], borderwidth=0)
    help2_lbl.place(x=730, y=290)
    help3_lbl=Label(root,image=balls[help3], borderwidth=0)
    help3_lbl.place(x=810, y=290)
    check_lines_horizontal()        #по горизонтали
    check_lines_vertical()          #по вертикали
    #check_lines_diagonal_left_right_1()
    #check_lines_diagonal_right_left_up()
    #check_lines_diagonal_left_right_down()
    sum=0
    for i in range(81):
        if all_lbl[i].used==True:
            sum+=1
            if sum > 80:
                lbl_looser=Label(root, text="Вы проиграли", font=("Arial", 26), bg="#414141", fg="white")
                lbl_looser.place(x=650,y=600)

root = Tk()
root.configure(bg="#414141")
root.geometry("900x646")

tileset = Image.open("cell-bgr.png")
img_tile = ImageTk.PhotoImage(tileset.crop((1, 0, 67, 66)))
img_tile_active = ImageTk.PhotoImage(tileset.crop((1, 69, 67, 135)))

lbl_name=Label(root, text="Бачаны 2", font=("Arial", 26), bg="#414141", fg="white")
lbl_name.place(x=650, y=25)
lbl_score=Label(root, text="Счёт: ", font=("Arial", 26), bg="#414141", fg="white")
lbl_score.place(x=650, y=90)
lbl_help=Label(root, text="Подсказка: ", font=("Arial", 16), bg="#414141", fg="white")
lbl_help.place(x=650, y=250)

x_score=0
score=Label(root, text=x_score, font=("Arial", 26), bg="#414141", fg="white")
score.place(x=750, y=90)

bgr_blue = Image.open("cell-bgr.png").convert('RGBA')
ball_blue = Image.open("ball-blue.png").convert('RGBA')
bgr_blue.paste(ball_blue,(6,5),ball_blue)
img_blue = ImageTk.PhotoImage(bgr_blue.crop((1, 0, 67, 66)))

bgr_aqua = Image.open("cell-bgr.png").convert('RGBA')
ball_aqua = Image.open("ball-aqua.png").convert('RGBA')
bgr_aqua.paste(ball_aqua,(6,5),ball_aqua)
img_aqua = ImageTk.PhotoImage(bgr_aqua.crop((1, 0, 67, 66)))

bgr_green = Image.open("cell-bgr.png").convert('RGBA')
ball_green = Image.open("ball-green.png").convert('RGBA')
bgr_green.paste(ball_green,(6,5),ball_green)
img_green = ImageTk.PhotoImage(bgr_green.crop((1, 0, 67, 66)))

bgr_pink = Image.open("cell-bgr.png").convert('RGBA')
ball_pink = Image.open("ball-pink.png").convert('RGBA')
bgr_pink.paste(ball_pink,(6,5),ball_pink)
img_pink = ImageTk.PhotoImage(bgr_pink.crop((1, 0, 67, 66)))

bgr_red = Image.open("cell-bgr.png").convert('RGBA')    
ball_red = Image.open("ball-red.png").convert('RGBA')
bgr_red.paste(ball_red,(6,5),ball_red)
img_red = ImageTk.PhotoImage(bgr_red.crop((1, 0, 67, 66)))

bgr_violet = Image.open("cell-bgr.png").convert('RGBA')
ball_violet = Image.open("ball-violet.png").convert('RGBA')
bgr_violet.paste(ball_violet,(6,5),ball_violet)
img_violet = ImageTk.PhotoImage(bgr_violet.crop((1, 0, 67, 66)))

bgr_yellow = Image.open("cell-bgr.png").convert('RGBA')
ball_yellow = Image.open("ball-yellow.png").convert('RGBA')
bgr_yellow.paste(ball_yellow,(6,5),ball_yellow)
img_yellow = ImageTk.PhotoImage(bgr_yellow.crop((1, 0, 67, 66)))

bgr_blue_active = Image.open("cell-bgr.png").convert('RGBA')
ball_blue_active = Image.open("ball-blue.png").convert('RGBA')
bgr_blue_active.paste(ball_blue_active,(6,74),ball_blue_active)
img_blue_active = ImageTk.PhotoImage(bgr_blue_active.crop((1, 69, 67, 135)))

bgr_aqua_active = Image.open("cell-bgr.png").convert('RGBA')
ball_aqua_active = Image.open("ball-aqua.png").convert('RGBA')
bgr_aqua_active.paste(ball_aqua_active,(6,74),ball_aqua_active)
img_aqua_active = ImageTk.PhotoImage(bgr_aqua_active.crop((1, 69, 67, 135)))

bgr_green_active = Image.open("cell-bgr.png").convert('RGBA')
ball_green_active = Image.open("ball-green.png").convert('RGBA')
bgr_green_active.paste(ball_green_active,(6,74),ball_green_active)
img_green_active = ImageTk.PhotoImage(bgr_green_active.crop((1, 69, 67, 135)))

bgr_pink_active = Image.open("cell-bgr.png").convert('RGBA')
ball_pink_active = Image.open("ball-pink.png").convert('RGBA')
bgr_pink_active.paste(ball_pink_active,(6,74),ball_pink_active)
img_pink_active = ImageTk.PhotoImage(bgr_pink_active.crop((1, 69, 67, 135)))

bgr_red_active = Image.open("cell-bgr.png").convert('RGBA')    
ball_red_active = Image.open("ball-red.png").convert('RGBA')
bgr_red_active.paste(ball_red_active,(6,74),ball_red_active)
img_red_active = ImageTk.PhotoImage(bgr_red_active.crop((1, 69, 67, 135)))

bgr_violet_active = Image.open("cell-bgr.png").convert('RGBA')
ball_violet_active = Image.open("ball-violet.png").convert('RGBA')
bgr_violet_active.paste(ball_violet_active,(6,74),ball_violet_active)
img_violet_active = ImageTk.PhotoImage(bgr_violet_active.crop((1, 69, 67, 135)))

bgr_yellow_active = Image.open("cell-bgr.png").convert('RGBA')
ball_yellow_active = Image.open("ball-yellow.png").convert('RGBA')
bgr_yellow_active.paste(ball_yellow_active,(6,74),ball_yellow_active)
img_yellow_active = ImageTk.PhotoImage(bgr_yellow_active.crop((1, 69, 67, 135)))

lbl_new_game = Label(root,text="Новая игра", font=("Arial", 26), bg="#414141", fg="white")
lbl_new_game.bind("<Button-1>", restarting_game)
lbl_new_game.place(x=650, y=370)

lbl_next_move=Label(root,text="Сделать ход", font=("Arial", 24), bg="#414141", fg="white")
lbl_next_move.bind("<Button-1>", next_move)
lbl_next_move.place(x=650, y=440)

starting_game()
set_balls()
root.mainloop()

