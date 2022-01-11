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
t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.config(text="window smaller")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="window bigger")
        t=0
def kala():
    x1=np.arange(0,9.5,0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)#min max step
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-3,0.5)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,10,0.5)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,9,0.5)#min max step
    y6=(1/8)*(x6-7)*2+1.5
    x7=np.arange(-13,-8.5,0.5)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)#min max step
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)#min max step
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('square equation')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

aken=Tk()
aken.title("Square equations")
#aken.iconbitmap('iconka.ico')
aken.geometry('700x600')
f1=Frame(aken,width=650,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)

lbl=Label(f1,text="Square equation solving",font="Calibri 26",fg="black", bg="purple")
lbl.pack(side=TOP)
vastus=Label(f1,text="Press the solution button to check", height=4, width=60, bg="pink",font="Calibri 26")
vastus.pack(side=BOTTOM)
a=Entry(f1, font="Calibri 26",fg="black", bg="purple", width=3)
a.pack(side=LEFT)#,padx=10,pady=10
x2=Label(f1,text="x**2+",font="Calibri 26",fg="purple", padx=10 )
x2.pack(side=LEFT)
b=Entry(f1, font="Calibri 26",fg="black", bg="purple", width=3)
b.pack(side=LEFT)
x=Label(f1,text="x+",font="Calibri 26",fg="purple")
x.pack(side=LEFT)
c=Entry(f1, font="Calibri 26",fg="black", bg="purple", width=3) 
c.pack(side=LEFT)
y=Label(f1,text="=0",font="Calibri 26",fg="black")
y.pack(side=LEFT)
btn=Button(f1,text="solution",font="Calibri 26",bg="pink",command=lahenda)
btn.pack(side=LEFT)
grph=Button(f1,text="graph",font="Calibri 26",bg="pink",command=graafik)
grph.pack(side=RIGHT)
btn_veel=Button(f1,text="window bigger",font="Calibri 26",bg="pink",command=veel)
btn_veel.pack(side=TOP)
var=IntVar()
r1=Radiobutton(f2,text="kala",variable=var, var=1, font="Calibri 26",command=kala )
r2=Radiobutton(f2,text="glasses",variable=var, var=2, font="Calibri 26" )
r3=Radiobutton(f2,text="lyagukha",variable=var, var=3, font="Calibri 26" )
r4=Radiobutton(f2,text="heart",variable=var, var=4, font="Calibri 26" )
r5=Radiobutton(f2,text="star",variable=var, var=5, font="Calibri 26" )
r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
# grid(), place()
#btn_g=Button(aken,text="график",font="Calibri 26",bg="green",command=graafik)
#nupp.bind('<Button-3>',vajutamine)
aken.mainloop()
