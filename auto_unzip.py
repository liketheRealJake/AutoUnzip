from tkinter import *
from tkinter import ttk
from pyunpack import *
from pathlib import Path
import glob, os

win = Tk()
win.title("Auto Unzip")
win.resizable(False, False)
win.geometry("249x70")
win.iconbitmap('res/icon.ico')


file_extension = StringVar()
file_name = StringVar()

def open_help_win():
    help_win = Tk()
    help_win.title("Help")
    help_win.resizable(False,False)
    help_win.iconbitmap('res/icon.ico')

    ttk.Label(help_win, text="Put Archives into the 'in' folder, press Extract Button\nAll files will be extracted into 'out' folder.").pack()
    ttk.Button(help_win, text="Close", command=help_win.destroy).pack()


def extract_archive():
    os.chdir('in')
    for file in glob.glob("*.rar"):
        os.mkdir(os.pardir + '/out/' + file.removesuffix('.rar'))
        Archive(file).extractall(os.pardir + '/out/' + file.removesuffix('.rar'))

    for file in glob.glob("*.zip"):
        os.mkdir(os.pardir + '/out/' + file.removesuffix('.zip'))
        Archive(file).extractall(os.pardir + '/out/' + file.removesuffix('.zip'))





ttk.Label(win, text="AUTO UNZIP",font=("Helvetica",16,"bold")).place(x=10,y=0)

ttk.Button(win,text="Extract All Into Output Folder",width=30,command=extract_archive).place(x=15, y=37)

ttk.Button(win,text="Help",command=open_help_win).place(x=145,y=5)

win.mainloop()