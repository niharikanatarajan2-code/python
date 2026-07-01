from tkinter import *
def check():
    p=e.get()
    if len(p)<6:
        r.config(text="Weak")
    elif len(p)<10:
        r.config(text="Medium")
    else:
        r.config(text="Strong")
root=Tk()
root.title("Password Strength")
Label(root,text="Enter Password").pack()
e=Entry(root,show="*")
e.pack()
Button(root,text="Check",command=check).pack()
r=Label(root,text="")
r.pack()
root.mainloop()