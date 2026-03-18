from tkinter import *

root = Tk()
root.geometry("200x150")
colors = ["red","green","blue"]
i = 0

def change():
    global i
    root.config(bg=colors[i])
    i = (i+1) % 3
    root.after(500, change)

change()
root.mainloop()
