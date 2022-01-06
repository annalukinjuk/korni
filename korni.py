print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")


from tkinter import *
n=0
def vajutamine(event):
    global n
    n+=1
    nupp.config(text="Vajutatud: "+str(n))

aken=Tk()
aken.title("Akna nimetus")
#aken.iconbitmap('iconka.ico')
aken.geometry('400x600')
nupp=Button(aken,text="Vajuta \nsiia",height=4,width=15,bg="blue",fg="green", font="Arial 36") #.pack(side=TOP) command=vajutamine()
nupp.pack(side=TOP) # grid(), place()
nupp.bind('<Button-3>',vajutamine)
aken.mainloop()
