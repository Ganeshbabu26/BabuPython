import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Canvas in tkinter")

canvas = tk.Canvas(a,height=200,width=200)
canvas.pack()

canvas.create_line(50,10,200,10)
canvas.create_oval(50,50,200,150)

a.mainloop()
