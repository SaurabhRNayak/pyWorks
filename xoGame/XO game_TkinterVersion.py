from tkinter import *

import numpy as np

def victory(p):
    vict=Toplevel(bmain)
    tag='**PLAYER '+p+' WINS**'
    lb=Label(vict,text=tag,font=("Helvetica", 26),bg='#E74C3C',fg='#fdfd96')
    lb.pack(expand=True)

def freeze():
    for i in range(3):
        for j in  range(3):
            if(board[i,j]==0):
                Label(f1, text='', bg='#E1CF79', height=2, width=3, relief=SUNKEN).grid(row=i, column=j)
    res.config(text='New Game',height=2, width=10)

def reset():
    global board
    board = np.zeros([3, 3], int)
    res.config(text='Reset', height=2, width=10)
    boardCreation()

def logic():
    global board
    global banner
    d1=board[0,0]+board[1,1]+board[2,2]
    d2=board[0,2]+board[1,1]+board[2,0]
    for i in range(3):
        r=board[i].sum()
        c=board[:,i].sum()
        print(r,c)
        if (r==3 or c==3 or d1==3 or d2==3):
            print('X')
            banner.config(text='**PLAYER X WINS**')
            freeze()
            victory('X')
            break
        if (r == -3 or c == -3 or d1==-3 or d2==-3):
            banner.config(text='**PLAYER O WINS**')
            freeze()
            victory('O')
            break


def but(a, b):
    global board
    global pl
    # global banner
    Label(f1, text=pl, bg='#E1CF79', height=2, width=3, relief=SUNKEN).grid(row=a, column=b)
    if (pl == 'X'):
        board[a][b] = 1
        banner.config(text="Player O ur turn!")
        pl = 'O'
    else:
        board[a][b] = -1
        pl = 'X'
        banner.config(text="Player X ur turn!")
    logic()
    print(board)


def boardCreation():
    global pl
    pl='X'
    banner.config(text="Player X ur turn!")

    b1 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(0, 0)).grid(row=0, column=0)
    b2 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(0, 1)).grid(row=0, column=1)
    b3 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(0, 2)).grid(row=0, column=2)
    b4 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(1, 0)).grid(row=1, column=0)
    b5 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(1, 1)).grid(row=1, column=1)
    b6 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(1, 2)).grid(row=1, column=2)
    b7 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(2, 0)).grid(row=2, column=0)
    b8 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(2, 1)).grid(row=2, column=1)
    b9 = Button(f1, text='', bg='#E1CF79', height=2, width=3, relief=RAISED, activebackground='#baa647',
                command=lambda: but(2, 2)).grid(row=2, column=2)


if __name__ == '__main__':
    global bmain
    bmain = Tk()
    bmain.title("XO HeRe wE GO!!")
    bmain.config(bg='#E55437')

    global board
    board = np.zeros([3, 3], int)

    global banner
    banner = Label(bmain, text="Player X ur turn!", font=("Helvetica", 16), bg='#154360', fg='#D1F2EB',relief=GROOVE)
    banner.pack(expand=True)

    global pl
    pl = 'X'

    global f1
    f1 = Frame(bmain)
    f1.pack(expand=True)
    global f2
    f2= Frame(bmain)
    f2.pack(expand=True)

    global res
    res = Button(f2, text='RESET', font=("Helvetica", 8), height=2, width=6, relief=RAISED, bg='lightblue',
                 fg='Darkblue', activebackground='#0055ff',
                 command=reset)
    res.grid(row=3, column=2)

    boardCreation()
    bmain.mainloop()