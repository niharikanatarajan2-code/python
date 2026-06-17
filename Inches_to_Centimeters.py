from tkinter import *
from unittest import result
def convert():
    inches=float(entry.get())
    cm=inches*2.54
    result.config(text="centimeters="+str(cm))
root=Tk()
root.title("Inches to Centimeters")
Label(root,text="Enter Length in Inches").pack()
entry=Entry(root)
entry.pack()
Button(root,text="Convert",command=convert).pack()
result=Label(root,text="")
result.pack()
root.mainloop()