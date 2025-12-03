import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Scale in tkinter")

scale = tk.Scale(a,from_=0,to=100)
scale.pack(pady=5)

a.mainloop()