import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Label in tkinter")
label = tk.Label(a,text="This is label")
label.pack(pady=5)
a.mainloop()