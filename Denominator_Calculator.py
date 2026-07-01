from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Denomination Counter")
root.geometry("300x300")
def calc():
    try:
        amt=int(e.get())
        for i,n in enumerate([2000,500,100]):
            out[i].delete(0,END)
            out[i].insert(0,amt//n)
            amt%=n
    except:
        messagebox.showerror("Error","Enter a valid amount")
Label(root,text="Enter Amount").pack()
e=Entry(root)
e.pack()
out=[]
for n in [2000,500,100]:
    Label(root,text=f"₹{n}").pack()
    x=Entry(root)
    x.pack()
    out.append(x)
Button(root,text="Calculate",command=calc).pack(pady=10)
root.mainloop()
    