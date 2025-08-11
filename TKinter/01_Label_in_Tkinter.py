import tkinter as tk

a = tk.Tk()

a.geometry("500x500")
a.title("Label in tkinter")
tk.Label(a,text="This is a label").pack()

a.mainloop()