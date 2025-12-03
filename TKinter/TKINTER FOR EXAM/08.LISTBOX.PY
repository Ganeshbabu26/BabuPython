import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Listbox in tkinter")

list = tk.Listbox(a)
list.insert(1,"Python")
list.insert(2,"C++")
list.insert(3,"Java")
list.pack()

a.mainloop()