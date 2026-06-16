from tkinter import *
from datetime import date
from unittest import result
def age():
    y=int(year.get())
    today=date.today()
    a=today.year-y
    result.config(text="Age="+str(a))
root=Tk()
root.title("Age Claculation")
root.geometry("250x150")
Label(root,text="Enter Birth Year").pack()
year=Entry(root)
year.pack()
Button(root,text="Calculate Age",command=age).pack()
result=Label(root,text="")
result.pack()
root.mainloop()