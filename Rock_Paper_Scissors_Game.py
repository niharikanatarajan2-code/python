import tkinter as tk
import random

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
        
    choice_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")
    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

choice_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
choice_label.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()

