from tkinter import *
import random
import copy
from PIL import ImageTk, Image

frame = Tk()

actual_game = [[0 for i in range(9)] for j in range(9)]

class Mark(Label):
    def _init_(self, row, col):
        Label._init_(self, master = frame)
        self.row = row
        self.col = col
        self.coltype = "ntg"
        self.if_has = False

frame["bg"] = "#660099"
frame.title("Я каменьщик")

red_t = Image.open("ball-red.png").convert('RGBA')
vio_t = Image.open("ball-violet.png").convert('RGBA')
blue_t = Image.open("ball-blue.png").convert('RGBA')
aqua_t = Image.open("ball-aqua.png").convert('RGBA')
yellow_t = Image.open("bal-yellow.png").convert('RGBA')
green_t = Image.open("ball-green.png").convert('RGBA')
pink_t = Image.open("ball-pink.png").convert('RGBA')

balls = {"red": red_t, "vio": vio_t, "blue": blue_t, "aqua": aqua_t, "yellow": yellow_t, "green": green_t, "pink": pink_t}

def send():
    global click
    click = ()
send()

frame.geometry("1000x700")
frame.resizable(w = False, h = False)

tile = Image.open("cell-bgr.png")
img = ImageTk.PhotoImage(tile.crop((1, 0, 67, 66)))
img2 = ImageTk.PhotoImage(tile.crop((1, 69, 67, 135)))
balls_a = {}

for i in ["red", "vio", "blue", "aqua", "yellow", "green", "pink"]:
    if_click_tile = ImageTk.PhotoImage(tile.crop((1, 0, 67, 66)))
    if_not_click_tile = ImageTk.PhotoImage(tile.crop((1, 69, 67, 135)))
    if_click_tile.paste(balls[i], (1, 1))
    if_not_click_tile.paste(balls[i], (1, 1))
    balls_a[i] = (if_not_click_tile, if_click_tile)

result = 0
located = []
ball_on = {"red": [], "vio": [], "blue": [], "aqua": [], "yellow": [], "green": [], "pink": []}

def scores():
    global result
    score = Label(frame, text = "Счёт: %d" % result, font = ("Times New Roman", "20"), fg = "white", bg = "660099", padx = 5, pady = 5)
    score.grid()(row = 1, column = 10, padx = 10)

def check():
    global result
    global free_tile
    global game_end
    free_tile = []
    for j in range(9):
        if not actual_game[j][k].if_has:
            free_tile.append((j,k))
        else:
            def check_01(i, r):
                if_same = True
                while if_same:
                    try:
                        if not (actual_game[j+i][k+r].coltype == actual_game[j][k].coltype):
                            if_same = False
                        else:
                            if i != r:
                                if i > r:
                                    if i > 0:
                                        i = i+1
                                    else:
                                        i = i-1
                                else:
                                    if r > 0:
                                        r = r+1
                                    else:
                                        r = r-1
                            else:
                                if i > 0:
                                    i = i+1
                                    r = r+1
                                elif i == 0:
                                    i = i+1
                                    r = r-1
                                else:
                                    i = i-1
                                    r = r-1
                    except IndexError:
                        if_same = False
                return (i, r)
            c = [check_01(i, r) for i, r in [(0,0), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]]
            for i, r in c:
                if max(abs(i), abs(r)) >= 5:
                    result = result + max(abs(i), abs(r)) * 2
                    for u in range(max(abs(i), abs(r))):
                        if max(abs(i), abs(r)) == abs(i) and i != r:
                            actual_game[j+u][k].config(image = img)
                            actual_game[j+u][k].coltype = "ntg"
                            actual_game[j+u][k].if_has = False
                        elif max(abs(i), abs(r)) == abs(r) and i != r:
                            actual_game[j][k+u].config(image=img)
                            actual_game[j][k+u].coltype = "ntg"
                            actual_game[j][k+u].if_has = False
                        else:
                            actual_game[j][k+u].config(image=img)
                            actual_game[j][k+u].coltype = "ntg"
                            actual_game[j][k+u].if_has = False
    if not free_tile:
        game_end = Label(master = frame, text = "Вы dead", font = ("Times New Roman", "36"), borderwidth = 0)
        game_end. place(x = 300, y = 300)
def move():
    global t_t
    global free_tile
    global game_end

    gener = ["red", "vio", "blue", "aqua", "yellow", "green", "pink", "ntg"]
    xy = [(random.randrange(0, 8), rand.randrange(0, 8))]

    check()

    for i in range(3):
        b = random.randrange(0, 7)
        try:
            xprob, yprob = random.choice(free_tile)
        except IndexError:
            game_end = Label(master = frame, text = "Вы Lose.", font =("Times New Roman", "36"))
            game_end.place(x = 300, y = 300)

        try:
            xy.append((xprob, yprob))
            ball_on[gener[b]].append(xy[i])
            if not actual_game[xy[i][0]][xy[i][1]].if_has:
                actual_game[xy[i][0]][xy[i][1]].config(image = balls_a[gener[b]][0])
                actual_game[xy[i][0]][xy[i][1]].coltype = gener[b]
                actual_game[xy[i][0]][xy[i][1]].if_has = True
            else:
                pass
        except UnboundLocalError:
            pass
    t_t = ball_on.cope()
    scores()
    xy.pop()

def possible(i1, j1, i2, j2):
    if actual_game[i1][j1].if_has:
       return True
    else:
        return False

def pl_move(event):
    tile_now = actual_game[event.widget.row][event.widget.row]
    global click
    global ball_on
    global game_end

    check()

    if tile_now.if_has:
        event.widget.config(image = balls_a[tile_now][1])
        click = (event.widget.row, event.widget.col)
        print(click)
    elif click:
        if possible(click[0], click[1], tile_now.row, tile_now):
            tile_now.if_has = True
            tile_now.coltype = copy.copy(actual_game[click[0]][click[1]].coltype)
            ball_on[tile_now.coltype].remove(click)
            ball_on[tile_now].append((tile_now.row, tile_now.col))
            actual_game[tile_now][tile_now].config(image = balls_a[tile_now][0])
            actual_game[click[0]][click[1]].if_has = False
            actual_game[click[0]][click[1]].coltype = "ntg"
            actual_game[click[0]][click[1]].config(image = img)
            move()
        print(tile_now.row, tile_now.col)
    else:
        pass
for row in range(9):
    for col in range(9):
        cell = Mark(row, col) 
        actual_game[row][col] = cell
        cell.config(image = img, borderwidth=0)
        cell.bind("<Button-1>", pl_move)
        cell.grid(row=row, column=col, padx=1, pady=1)      
move()

def new_game():
    global result
    global game_end
    for i in range(9):
        actual_game[i][j].config(image=img)
        actual_game[i][j].coltype = "ntg"
        actual_game[i][j].if_has = False
    move()
    result = 0
    game_end.destroy()
    scores()
    check()
new = Button(master = frame, text = "Начать заново", padx = 5, pady = 5, font = ("Times New Roman", "16"), background = "white", actyvebackground = "#240935", command = new_game)
new.grid(row = 8,column = 10, padx = 10)

def notheng():
    pass

make_move = Button(master = frame, text = "Сделать ход", pax = 4, pady =4, font = ("Times New Roman", "16"), background = "white", activebackground = "#240935", command = move)
make_move.grid(row = 7, column = 10, padx = 10)

Title = Label(frame, text = "Колобочки", font = ("Times New Roman", "24"), fg = "white", bg = "#240935")
Title.grid(row = 0, column = 10, padx = 10)
help = Label(frame, text = "Ваша рука помощи", font = ("Times New Roman", "20"), fg = "white", bg = "#240935")
help.grid(row = 3, column = 10, padx = 10)

def show():
    for i in t_t.keys():
        c = 0
        if t_t[i]:
            for j in t_t[i]:    
                t_t = Label(frame, image = balls_a[i][0], borderwidth = 0)
                t_t.grid(row = 4+c, column = 10, padx = 10)
                c = c+1
show()
frame.mainloop