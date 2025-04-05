import tkinter as tk
import random

colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']

def change_border():
    color = random.choice(colors)
    frame.config(bg=color)

def exit_app():
    root.destroy()

root = tk.Tk()

frame = tk.Frame(root, bg='black', padx=4, pady=4)
frame.pack(pady=20)

button = tk.Button(frame, text="Змінити рамку", command=change_border)
button.pack()

exit_button = tk.Button(root, text="Вихід", command=exit_app)
exit_button.pack(pady=10)

root.mainloop()