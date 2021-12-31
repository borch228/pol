from tkinter import *
from math import *
import random
root = Tk()
root.geometry("1920x1080")
c = Canvas(root, width = 1920, height = 1080)
c.pack()
def moveCircle(angle = [0.0]):
    global cx
    global cy
    global kt
    if(kt != 0):
        angle[0]+=360/kt+180
    rr = d/2
    cx, cy = r*cos(radians(angle[0])) + x, r*sin(radians(angle[0])) + y
    c.create_polygon(cx+rr*sqrt(2)*cos(radians(105-angle[0])), cy-sin(radians(105-angle[0]))*rr*sqrt(2), cx+rr*sqrt(2)*cos(radians(30-angle[0])), cy-rr*sqrt(2)*sin(radians(30-angle[0])), cx+rr*sqrt(2)*cos(radians(-30-angle[0])), cy-rr*sqrt(2)*sin(radians(-30-angle[0])), cx+rr*sqrt(2)*cos(radians(-105-angle[0])), cy-rr*sqrt(2)*sin(radians(-105-angle[0])),
                     fill = "black") 
    angle[0] += 360/d2
    
def generate_shest(coordx, coordy, size, ct, wt):
    global p
    global r
    global d
    global d2
    global x
    global y
    global cx
    global cy
    x = coordx
    y = coordy
    cy = coordy
    r = ct*wt/3.14
    cx = coordx
    d2 = ct
    d = wt
    c.create_oval(coordx-r, coordy-r, coordx+r, coordy+r,
                  fill = "black")
    p = c.create_polygon(coordx+r-wt/2, coordy-wt/2, coordx+r-wt/2, coordy+wt/2, coordx+r+wt/2, coordy+wt/2, coordx+r+wt/2, coordy-wt/2, fill = "")
    #p = c.create_pol(coordx+r-wt/2, coordx+r-wt/2, coordy-wt/2, coordy-wt/2, coordx+r+wt/2, coordx+r+wt/2, coordy+wt/2, coordy+wt/2, fill = "black")
tx = 100
ty = 200
kt = 0
sa = Label(root, text = '''Ведущая шестерня №1 крутится против часовой стрелке.
Вопрос 1: в какую сторону крутится шестерня №(какой то номер)? 
Вопрос 2: сколько оборотов сделает шестерня №(какой то номер), если ведущая шестерня сделала один оборот.
Если шестеренки находятся на одной оси , они скреплены и движутся как единое целое. ''')
kkk = random.randint(2, 6)
jh = []
for i in range(kkk):
    jh.append(i+1)
for i in range(kkk):
    kth = random.randint(6, 10)
    if(i != 0):
        tx+=(ror+kth*30/3.14+30)
        ty+= sin(radians(-180/ddd+180))*(ror+kth*30/3.14+30)
        kt = ddd/2
    generate_shest(tx, ty, 10, kth, 30)
    jhg = random.randint(0, len(jh)-1)
    a = Label(root, text = str(jh[jhg]))
    jh.pop(jhg)
    a.place(x=tx+kth*30/3.14, y=ty-kth*30/3.14)
    for j in range(kth):
        moveCircle()
        kt = 0
    ror = kth*30/3.14
    ddd = kth
sa.place(x=100, y=600)
root.mainloop()


#canvas_object = canvas.create_image(30+10*int(steps),250, image=canvas_image)
#canvas.update()
