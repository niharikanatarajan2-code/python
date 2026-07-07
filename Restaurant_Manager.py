import tkinter as tk
from tkinter import ttk,messagebox
class Restaurant:
    def __init__(self,root):
        self.menu = {
            "Fries":2,"Lunch":2,"Burger":3,"Pizza":4,"Cheese Burger":2.5,"Drinks":1            
        }
        self.rate=82
        self.cur=tk.StringVar(value="USD")
        self.qty={}
        ttk.Label(root,text="Restaurant Order",font=("Arial",16,"bold")).pack(pady=10)
        frame=ttk.Frame(root)
        frame.pack()
        for i,(item,price) in enumerate(self.menu.items()):
            ttk.Label(frame,text=f"{item}(${price})").grid(row=i,column=0,padx=5,pady=5)
            e=ttk.Entry(frame,width=5)
            e.grid(row=i,column=1)
            self.qty[item]=e
            ttk.Combobox(root,textvariable=self.cur,values=["USD","INR"]state="readonly").pack(pady=5)
            ttk.Button(root,text="Place Order",command=self.order).pack(pady=10)
            def order(self):
                rate=self.rate if self.cur.get()=="INR"else 1
                sym = "₹" if self.cur.get() == "INR" else "$"
                total,text=0,"Order Summary\n\n"
                for item,price in self.menu.items():
                    q=self.qty[item].get()
                    if q.isdigit() and int(q):
                        q=int(q)
                        total+=q*price*rate
                        cost=q*price*rate
                        text+= f"{item}:{q}={sym}{cost}\n"
                        if total:
                            messagebox.showinfo("Bill",text+f"\nTotal={sym}{total}")
                        else:
                            messagebox.showerror("Error","Enter quantity!")
                            root=tk.Tk()
                            root.title("Restaurant")
                            root.geometry("350x350")
                            Restaurant(root)
                            root.mainloop()
                            