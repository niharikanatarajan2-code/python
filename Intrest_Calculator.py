from tkinter import *
from tkinter import messagebox
def calculator():
    p=float(principal.get())
    r=float(rate.get())
    t=float(time.get())
    si=(p*r*t)/100
    ci=p*((1+(r/100))**t)
    messagebox.showinfo("Result",f"Simple Intrest={si:.2f}\nCompound Intrest={ci:.2f}")
    root=Tk()
    root.title("Intrest Calculator")
    Label(root,text="Principal").grid(row=0,column=0)
    Label(root,text="Rate").grid(row=1,column=0)
    Label(root,text="Time").grid(row=2,column=0)
    principal=Entry(root)
    rate=Entry(root)
    time=Entry(root)
    principal.grid(row=0,column=1)
    rate.grid(row=1,column=1)
    time.grid(row=2,column=1)
    Button(root,text="Calculate",command=calculator).grid(row=3,column=0,columnspan=2)
    root.mainloop()
