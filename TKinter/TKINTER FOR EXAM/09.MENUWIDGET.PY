import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("menu in tkinter")

menu = tk.Menu(a)
a.config(menu=menu)

filemenu = tk.Menu(menu)

menu.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Exit",command=a.quit)

a.mainloop()