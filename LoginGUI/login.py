from tkinter import *
from tkinter import messagebox

def logfn():
    id = logen.get()
    pwd = pasen.get()
    f = open(r'C:\Users\X127961\Desktop\Login repo\usersRepo.txt')
    l = f.readlines()
    fg = 0
    for i in range(len(l)):
        if ('id-' + id == l[i].strip()):
            fg = 1
            if ('pw-' + pwd == l[i + 1].strip()):
                messagebox.showinfo("Information", "Successful Login")
                logwin.destroy()
                break
            else:
                messagebox.showwarning("Information", "Incorrect password")
                logwin.destroy()
                break
    if fg == 0:
        messagebox.showinfo("Information", "User Not Found")
    logwin.destroy()
    f.close()


def regfn():
    f = open(r'C:\Users\X127961\Desktop\Login repo\usersRepo.txt','a')          #using a text file as db of the users, U must create a text file and copy its path here.
    id=regid.get()
    pwd=regpd.get()
    f.write('\n'+'id-'+id+'\n'+'pw-'+pwd)                                       #Creating a difference between userid and password for easy acknoledgement
    f.close()
    messagebox.showinfo("Information", "User Registered Successfully")
    regwin.destroy()


def login():
    global logwin
    logwin = Toplevel(root)
    logwin.geometry('200x130')
    global logen
    global pasen
    logen = StringVar()
    pasen = StringVar()
    Label(logwin, text="Login ID").pack()
    lo = Entry(logwin, bd=2, textvariable=logen)
    lo.pack()
    lo.focus()
    Label(logwin, text="Password").pack()
    Entry(logwin, bd=2, textvariable=pasen, show="*").pack()                      #show(*) will hide the entry by showing * instead of the entered value
    Label(logwin, text='').pack()
    Button(logwin, width=4, height=1, text='ok', command=logfn, relief=RAISED).pack()


def Register():
    global regwin
    regwin = Toplevel(root)
    regwin.geometry('200x130')
    global regid
    global regpd
    regid = StringVar()
    regpd = StringVar()
    Label(regwin, text='ENTER ID*').pack()
    rid = Entry(regwin, bd=2, textvariable=regid)
    rid.pack()
    rid.focus()
    Label(regwin, text='ENTER PASSWORD*').pack()
    Entry(regwin, bd=2, textvariable=regpd,show="*").pack()
    Button(regwin, text='Submit', command=regfn, relief=RAISED).pack()


if __name__ == '__main__':
    root = Tk()
    root.title('LOGIN')
    root.geometry('200x100')
    f1 = Frame(root, bg='lightblue', relief=SUNKEN, bd=3)
    f1.pack(fill=BOTH, expand=True)
    Label(f1, text='Choose an action', bd=1, pady=1, bg='lightgreen', relief=SUNKEN).pack()
    Button(f1, text='Login', command=login, relief=RAISED, bg='lightpink').pack(expand=True)
    Button(f1, text='Register', command=Register, relief=RAISED, bg='lightgrey').pack(expand=True)
    root.mainloop()
