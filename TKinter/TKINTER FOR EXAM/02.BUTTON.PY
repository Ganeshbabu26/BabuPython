import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Button in tkinter")

def sample():
    tk.Label(a,text="tkinter button").pack(pady=5)

btn = tk.Button(a,text="Click",command=sample)
btn.pack(pady=5)

a.mainloop()


'''
import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Button in tkinter")

count = tk.IntVar(value=0)

def sample():
    count.set(count.get() + 1)

label = tk.Label(a, textvariable=count, font=("Arial", 20))
label.pack(pady=20)

btn = tk.Button(a, text="Click", command=sample)
btn.pack(pady=10)

a.mainloop()

'''
