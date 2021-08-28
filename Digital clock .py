from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text = timeVar)
    clock.after(200,get_time)

Label(master, font = ("Arial", 30), text = "!!!___Digital Clock by me___!!!", bg = "black", fg = "red").pack()
clock = Label(master, font = ("Blox", 100), bg = "black", fg = "cyan")
clock.pack()

get_time()

master.mainloop()