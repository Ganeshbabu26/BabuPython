import tkinter as tk
from tkinter import messagebox

a = tk.Tk()
a.geometry("500x500")
a.title("Messagebox in tkinter")

messagebox.showinfo("info", "This is a message!")

a.mainloop()