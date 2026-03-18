from tkinter import *
import math

root = Tk()

Label(root, text="Radius").pack()
r = Entry(root); r.pack()

Label(root, text="Height").pack()
h = Entry(root); h.pack()

def calc():
    R = float(r.get()); H = float(h.get())
    sa = 2*math.pi*R*(H+R)
    v  = math.pi*R*R*H
    Label(root, text=f"SA={sa:.2f}  Vol={v:.2f}").pack()

Button(root, text="Calculate", command=calc).pack()

root.mainloop()
