import os
import platform
import ctypes
import time
from tkinter import *


def get_free_space(folder):
    free_bytes = ctypes.c_ulonglong(0)
    #  Конструктор принимает необязательный инициализатор целого числа; проверка переполнения не выполняется.
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
    #  достает из заданной папки количество свободных байт c_wchar_p - указателем на широкую символьную
    #  строку оканчивающуюся нулём
    return free_bytes.value


def loop(n):
    poetry = "На диске свободно:\n" + str(get_free_space('C:/')/(1024**3)) + "ГБ"
    label = Label(text=poetry, justify=CENTER)
    label.place(relx=.3, rely=.3)
    qwert = time.ctime(time.time())
    label = Label(text=qwert, justify=CENTER)
    label.place(relx=.3, rely=.5)
    root.after(5000, loop, n+1)


root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300")
root.after_idle(loop, 5)  # start loop

root.mainloop()
