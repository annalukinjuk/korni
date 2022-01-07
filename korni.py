import numpy as np
from math import*
import matplotlib.pyplot as plt
from tkinter import *
global D,t
D=-1
t="no solutions"
graf=False
def lahenda():
    global a,b,c, D, t
    if(a.get()!="" and b.get()!="" and c.get()!=""):
        if type(a) and type(b) and type(c)!=str:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            graf=True
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f"X1={x1_}, \nX2={x2_}"
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"X1={x1_}"
                graf=True
            else:
                t="No square roots detected"
                graf=False
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="pink")
        b.configure(bg="pink")
        c.configure(bg="pink")
    elif (a.get()==0 and b.get()==0 and c.get()==0):
            vastus.configure(text=f"cannot be zero")
            a.configure(bg="red")
            graf=False
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
        graf=True
    return graf, D, t
def graafik():
    graf,D,t=lahenda()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x=np.arange(x0-10,x0+10,0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig=plt.figure()
        plt.plot(x,y,'b:o')
        plt.title('square equation')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"apex of a parabola({x0},{y0})"
    else:
        text=f"the option is not avalible \n with these variables"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
aken=Tk()
aken.title("Square equations")
#aken.iconbitmap('iconka.ico')
aken.geometry('650x600')
lbl=Label(aken,text="Square equation solving",font="Calibri 26",fg="black", bg="purple")
lbl.pack()
vastus=Label(aken,text="Press the green button to check", height=4, width=60, bg="pink",font="Calibri 26")
vastus.pack(side=BOTTOM)
a=Entry(aken, font="Calibri 26",fg="black", bg="purple", width=3)
a.pack(side=LEFT)#,padx=10,pady=10
x2=Label(aken,text="x**2+",font="Calibri 26",fg="purple", padx=10 )
x2.pack(side=LEFT)
b=Entry(aken, font="Calibri 26",fg="black", bg="purple", width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Calibri 26",fg="purple")
x.pack(side=LEFT)
c=Entry(aken, font="Calibri 26",fg="black", bg="purple", width=3) 
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Calibri 26",fg="black")
y.pack(side=LEFT)
btn=Button(aken,text="solution",font="Calibri 26",bg="pink",command=lahenda)
btn.pack(side=LEFT)
grph=Button(aken,text="graph",font="Calibri 26",bg="pink",command=graafik)
grph.pack(side=RIGHT)
# grid(), place()
#btn_g=Button(aken,text="график",font="Calibri 26",bg="green",command=graafik)
#nupp.bind('<Button-3>',vajutamine)
aken.mainloop()
