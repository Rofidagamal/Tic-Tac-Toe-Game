import math
import tkinter as tk
import tkinter.messagebox
import winsound
from random import choice
from tkinter import *
from tkinter import Button, DISABLED, StringVar, Label, NORMAL, Entry, Frame, RIDGE, S, \
    E, N, W, LEFT, RIGHT, CENTER

window = tk.Tk()
COM = +1
HUM = -1
m = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}


def start(button, n1, n2):
    winsound.PlaySound(None, winsound.SND_PURGE)
    global board, l1, l2
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = []
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    COM = +1
    HUM = -1
    global p1, p2
    num1 = (n1.get()).upper()
    num2 = (n2.get()).upper()
    global s
    global first
    global h_choice
    global c_choice
    first = ''
    global cnt
    h_choice = ''
    c_choice = ''
    cnt = 0
    if (num1 != 'X' and num1 != 'O') or (num2 != 'Y' and num2 != 'N'):
        try:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", 'You must enter true values !')
        except:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", 'You must enter true values !')
    else:
        winsound.PlaySound("Tone_wav (mp3cut.net).wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)

        if num1 == 'X':
            c_choice = 'O'
            h_choice = 'X'
        else:
            c_choice = 'X'
            h_choice = 'O'
        first = num2
        enable()
    if first == "N":
        computer_turn()

    else:
        return


def valid_move(x, y):  # check poistion of x,y in empty cell free or no
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def make_move(x, y, player):  # check this place free or no to put in place value
    global cnt
    if valid_move(x, y):
        board[x][y] = player
        cnt += 1
        return True
    else:
        return False


def empty_cells(state):
    cells = []
    for x, row in enumerate(
            state):  # state means board and we want to now coordinates ,enumerate :adds a counter to an iterable and returns it
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


def game_over(state):
    return wins(state, COM) or wins(state, HUM)


def wins(state, player):  # first 3 lines rows , second 3 colums , third dignoal
    wins_states = [[state[0][0], state[0][1], state[0][2]], [state[1][0], state[1][1], state[1][2]],
                   [state[2][0], state[2][1], state[2][2]],
                   [state[0][0], state[1][0], state[2][0]], [state[0][1], state[1][1], state[2][1]],
                   [state[0][2], state[1][2], state[2][2]],
                   [state[0][0], state[1][1], state[2][2]], [state[0][2], state[1][1], state[2][0]]]
    if [player, player, player] in wins_states:  # even that player is 1 or -1 or 0
        return True
    else:
        return False


def player_turn():  # we should make sure that the game end or not , depth decrease when we play once and we are not in depth 0 beacuse the number of rows is 3 and number of colums is 3 the num of cells is 9 so when we go below the level increase so at the last depth=0 and last level
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    move = -1  # iniale value to enter while
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while move < 1 or move > 9:
        move = s
        coord = moves[move]
        can_move = make_move(coord[0], coord[1], HUM)
        if not can_move:
            move = -1
    checkforwin()


def computer_turn():
    global board, l1, l2
    global s
    string = ""
    global cnt
    cnt = 0
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COM)
        x, y = move[0], move[1]
    make_move(x, y, COM)
    for i in empty_cells(board):
        for j in m:
            if i == m[j]:
                l2.append(j)
    n = set(l1) - set(l2)
    for i in But:
        if n == But[i]:
            string = i
        if string == "button1":
            button1["text"] = c_choice
            cnt += 1
            s = 1
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button2":
            button2["text"] = c_choice
            cnt += 1
            s = 2
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button3":
            button3["text"] = c_choice
            cnt += 1
            s = 3
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button4":
            button4["text"] = c_choice
            cnt += 1
            s = 4
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button5":
            button5["text"] = c_choice
            cnt += 1
            s = 5
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button6":
            button6["text"] = c_choice
            cnt += 1
            s = 6
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button7":
            button7["text"] = c_choice
            cnt += 1
            s = 7
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button8":
            button8["text"] = c_choice
            cnt += 1
            s = 8
            if l1.count(s) != 0:
                l1.remove(s)
        elif string == "button9":
            button9["text"] = c_choice
            cnt += 1
            s = 9
            if l1.count(s) != 0:
                l1.remove(s)
    checkforwin()


def evaluate(state):
    if wins(state, COM):
        score = 1
    elif wins(state, HUM):
        score = -1
    else:
        score = 0
    return score


def minimax(board, depth, player):  # function combaine two function minimization and maximzation
    if player == COM:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, +math.inf]
    if depth == 0 or game_over(board):
        score = evaluate(board)  # see the poistion of board // draw / win // lose
        return [-1, -1, score]
    for cell in empty_cells(board):
        x, y = cell[0], cell[1]
        board[x][y] = player
        score = minimax(board, depth - 1, -player)  # recu to arrive to thing
        board[x][y] = 0
        score[0], score[1] = x, y
        if player == COM:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
    return best


window.title("Tic Tac Toe")


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def enable():
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)


def Click(buttons, n1, n2):
    global cnt
    global s
    global first
    global l1, l2
    cnt = 0

    if buttons["text"] == " ":
        if buttons == button1:
            button1["text"] = h_choice
            cnt += 1
            s = 1
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button2:
            button2["text"] = h_choice
            cnt += 1
            s = 2
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button3:
            button3["text"] = h_choice
            cnt += 1
            s = 3
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button4:
            button4["text"] = h_choice
            cnt += 1
            s = 4
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button5:
            button5["text"] = h_choice
            cnt += 1
            s = 5
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button6:
            button6["text"] = h_choice
            cnt += 1
            s = 6
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button7:
            button7["text"] = h_choice
            cnt += 1
            s = 7
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button8:
            button8["text"] = h_choice
            cnt += 1
            s = 8
            if l1.count(s) != 0:
                l1.remove(s)
        elif buttons == button9:
            button9["text"] = h_choice
            cnt += 1
            s = 9
            if l1.count(s) != 0:
                l1.remove(s)
        l2.clear()
        player_turn()
        computer_turn()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "This button is already clicked before!!")


def checkforwin():
    if button1['text'] == button2['text'] == button3['text'] == c_choice or \
            button4['text'] == button5['text'] == button6['text'] == c_choice or \
            button7['text'] == button8['text'] == button9['text'] == c_choice or \
            button1['text'] == button5['text'] == button9['text'] == c_choice or \
            button3['text'] == button5['text'] == button7['text'] == c_choice or \
            button1['text'] == button4['text'] == button7['text'] == c_choice or \
            button2['text'] == button5['text'] == button8['text'] == c_choice or \
            button3['text'] == button6['text'] == button9['text'] == c_choice:
        disableButton()
        winsound.PlaySound(None, winsound.SND_PURGE)
        winsound.PlaySound("loser.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + c_choice + "  wins")


    elif button1['text'] == button2['text'] == button3['text'] == h_choice or \
            button4['text'] == button5['text'] == button6['text'] == h_choice or \
            button7['text'] == button8['text'] == button9['text'] == h_choice or \
            button1['text'] == button5['text'] == button9['text'] == h_choice or \
            button3['text'] == button5['text'] == button7['text'] == h_choice or \
            button1['text'] == button4['text'] == button7['text'] == h_choice or \
            button2['text'] == button5['text'] == button8['text'] == h_choice or \
            button3['text'] == button6['text'] == button9['text'] == h_choice:
        disableButton()
        winsound.PlaySound(None, winsound.SND_PURGE)
        winsound.PlaySound("winner.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + h_choice + " wins")

    elif len(empty_cells(board)) == 0:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Tie!!")
        winsound.PlaySound(None, winsound.SND_PURGE)
        disableButton()


def center(win):
    win.update_idletasks()
    width = 1050
    height = 550
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


window.resizable(0, 0)
p1 = StringVar()
p2 = StringVar()
buttons = StringVar()
window.title("Welcome to TIC-Tac-Toe Game ")
center(window)
window.configure(background='khaki')
Tops = Frame(window, bg='khaki', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)
lblTitle = Label(Tops, font=('Magneto', 50, 'bold'), text="Tic Tac Toe Game", bd=30, fg='yellow', bg='blue',
                 justify=CENTER)
lblTitle.grid(row=0, column=0)
MainFrame = Frame(window, bg='khaki', pady=2, width=1350, height=100, relief=RIDGE)
MainFrame.grid(row=1, column=0)
LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=14, bg='blue', relief=RIDGE)
LeftFrame.pack(side=LEFT)
RightFrame = Frame(MainFrame, bd=10, width=750, height=500, padx=18, pady=2, bg='blue', relief=RIDGE)
RightFrame.pack(side=RIGHT)
RightFrame1 = Frame(RightFrame, bd=10, width=600, height=360, padx=10, pady=2, bg='yellow', relief=RIDGE)
RightFrame1.grid(row=0, column=0)
RightFrame2 = Frame(RightFrame, bd=10, width=600, height=360, padx=10, pady=2, bg='yellow', relief=RIDGE)
RightFrame2.grid(row=1, column=0)
lblPlayerX = Label(RightFrame1, font=('Bookman Old Style', 15, 'bold'), text="What's your choice? X or O:", padx=2,
                   pady=2, bg='yellow', fg="black")
lblPlayerX.grid(row=0, column=1, sticky=W)
nmPlayerX = Entry(RightFrame1, font=('Forte', 15, 'bold'), bd=3, fg="black", textvariable=p1, width=7,
                  justify=LEFT).grid(row=0, column=2)
lblPlayerO = Label(RightFrame1, font=('Bookman Old Style', 15, 'bold'),
                   text="Do you want to play first?\n Enter Y to say yes\n else Enter N:", padx=2, pady=2, bg='yellow',
                   fg="black")
lblPlayerO.grid(row=2, column=1, sticky=W)
nmPlayerO = Entry(RightFrame1, font=('Forte', 15, 'bold'), bd=3, fg="black", textvariable=p2, width=7,
                  justify=LEFT).grid(row=2, column=2)
button10 = Button(RightFrame2, text="Start/Restart", font=('Forte', 20, 'bold'), height=1, width=15, fg='black',
                  bg='dodgerblue', command=lambda: start(button10, p1, p2))
button10.grid(row=1, column=0, padx=1, pady=11)
button1 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='dodgerblue',
                 command=lambda: Click(button1, p1, p2))
button1.grid(row=1, column=0, sticky=S + N + E + W)
button2 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='yellow',
                 command=lambda: Click(button2, p1, p2))
button2.grid(row=1, column=1, sticky=S + N + E + W)
button3 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='dodgerblue',
                 command=lambda: Click(button3, p1, p2))
button3.grid(row=1, column=2, sticky=S + N + E + W)
button4 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='yellow',
                 command=lambda: Click(button4, p1, p2))
button4.grid(row=2, column=0, sticky=S + N + E + W)
button5 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='dodgerblue',
                 command=lambda: Click(button5, p1, p2))
button5.grid(row=2, column=1, sticky=S + N + E + W)
button6 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='yellow',
                 command=lambda: Click(button6, p1, p2))
button6.grid(row=2, column=2, sticky=S + N + E + W)
button7 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='dodgerblue',
                 command=lambda: Click(button7, p1, p2))
button7.grid(row=3, column=0, sticky=S + N + E + W)
button8 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='yellow',
                 command=lambda: Click(button8, p1, p2))
button8.grid(row=3, column=1, sticky=S + N + E + W)
button9 = Button(LeftFrame, text=" ", font=('Forte', 20, 'bold'), height=3, width=8, bg='dodgerblue',
                 command=lambda: Click(button9, p1, p2))
button9.grid(row=3, column=2, sticky=S + N + E + W)
photo = PhotoImage(file="tic5.png")
label = Label(RightFrame1, image=photo, bd=0)
label.grid(row=0, column=0)

But = {"button1": {1}, "button2": {2}, "button3": {3}, "button4": {4}, "button5": {5}, "button6": {6}, "button7": {7},
       "button8": {8}, "button9": {9}}

disableButton()
window.mainloop()
