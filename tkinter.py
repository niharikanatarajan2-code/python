from tkinter import *
import tkinter
def product():
    n1=int(e1.get())
    n2=int(e2.get())
    l3.config(text=n1*n2)
root=Tk()
Label(root,text="Number 1").pack()
e1=Entry(root)
e1.pack()
Label(root,text="Number 2").pack()
e2=Entry(root)
e2.pack()
Button(root,text="Multiply",command=product).pack()
l3=Label(root,text="")
l3.pack()
root.mainloop()    