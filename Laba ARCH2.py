import os
import platform
import ctypes
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import shutil


root = Tk()
root.title("Графическая программа на Python")
root.geometry("500x400")
poetry = "Выбирете файл для перемещения или копирования"
text = Text(root, height=1, width=40)
text.place(relx=.0, rely=.1)
text1 = Text(root, height=1, width=40)
text1.place(relx=.0, rely=.4)
label = Label(text=poetry, justify=LEFT)
label.place(relx=.0, rely=.0)


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    text.insert('1.0', filename)


def save_file():
   savef = fd.askdirectory()
   text1.insert('1.0', savef)

def copy_file():
    print(text.get("1.0", END))
    print(text1.get("1.0", END))
    source_folder = text.get("1.0", END)
    source_folder = source_folder.split("/")
    print(source_folder)
    changed_folder = text1.get("1.0", END)
    changed_folder = changed_folder[0:-1] + "/" + source_folder[-1]
    print(changed_folder)
    source_folder = '/'.join(source_folder)
    shutil.copyfile(source_folder[0:-1], changed_folder[0:-1])
    text.delete("1.0", END)
    text1.delete("1.0", END)


def replace_file():
    print(text.get("1.0", END))
    print(text1.get("1.0", END))
    source_folder = text.get("1.0", END)
    source_folder = source_folder.split("/")
    print(source_folder)
    changed_folder = text1.get("1.0", END)
    changed_folder = changed_folder[0:-1] + "/" + source_folder[-1]
    print(changed_folder)
    source_folder = '/'.join(source_folder)
    shutil.move(source_folder[0:-1], changed_folder[0:-1])
    text.delete("1.0", END)
    text1.delete("1.0", END)


open_button = ttk.Button(
    root,
    text='Find a File',
    command=select_file
)
open_button.place(relx=.7, rely=.1)

save_button = ttk.Button(
    root,
    text='Find path',
    command=save_file
)
save_button.place(relx=.7, rely=.4)

copy_button = ttk.Button(
    root,
    text='Copy a File',
    command=copy_file
)
copy_button.place(relx=.0, rely=.5)

replace_button = ttk.Button(
    root,
    text='Replace a File',
    command=replace_file
)
replace_button.place(relx=.2, rely=.5)

poetry = "Выбирете место для перемещения или копирования"
label = Label(text=poetry, justify=LEFT)
label.place(relx=.0, rely=.3)


root.mainloop()