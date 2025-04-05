import tkinter as tk

root = tk.Tk()
root.title("My program")
root.geometry("400x300")
root.configure(bg="white")

label = tk.Label(
    root,
    text="Welcome",
    bg="#7cd964",  
    fg="white",
    font=("Arial", 30, "bold"),
    width=15,
    height=3
)
label.pack(pady=10)

button = tk.Button(
    root,
    text="Тиць!",
    bg="#4fc3f7", 
    fg="white",
    font=("Arial", 20, "bold"),
    width=10,
    height=2
)
button.pack(pady=10)

root.mainloop()