from tkinter import Tk, Button
import json

size = (30, 30)

app = Tk()
btns = []

def dump():
    data = {"fields": []}
    data["size"] = size
    for btn in btns:
        data["fields"].append({"x": btn.x, "y": btn.y, "wall": btn.activated})
    with open("maze.json", "w") as f:
        json.dump(data, f)

def onkick(arg):
    arg.config(bg="#420cad")
    arg.activated = True
    dump()

def entkick(arg):
    arg.config(bg="#ffffff")
    arg.activated = False
    dump()

def clear():
    for btn in btns:
        btn.config(bg="#ffffff")
        btn.activated = False
    dump()

Button(app, text="🦍", command=clear).grid(row=size[0]+1,columnspan=size[1])
for x in range(size[0]):
    for y in range(size[1]):
        btn = Button(app, width=2, height=1)
        btn.x, btn.y, btn.activated = x, y, False
        btn.grid(row=x, column=y)
        btn.config(command=lambda btn=btn: onkick(btn))
        btn.config(bg="#ffffff")
        btn.bind("<Button-3>", lambda _, btn=btn: entkick(btn))
        btns.append(btn)

dump()

app.mainloop()
