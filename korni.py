import numpy as np
from tkinter import *
def lahenda():
    global a,b,c
    if(a.get()!="" and b.get()!="" and c.get()!=""):
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x1_=round((-1*b_-sqrt(D))/(2*a_),2)
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
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")


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
x2=Label(aken,text="x**2+",font="Calibri 26",fg="black", bg="purple", padx=10 )
x2.pack(side=LEFT)
b=Entry(aken, font="Calibri 26",fg="black", bg="purple", width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Calibri 26",fg="purple")
x.pack(side=LEFT)
c=Entry(aken, font="Calibri 26",fg="black", bg="purple", width=3) 
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Calibri 26",fg="black")
y.pack(side=LEFT)
btn=Button(aken,text="check the solution",font="Calibri 26",bg="pink",command=lahenda)
btn.pack(side=LEFT) # grid(), place()
#btn_g=Button(aken,text="график",font="Calibri 26",bg="green",command=graafik)
#nupp.bind('<Button-3>',vajutamine)
aken.mainloop()
