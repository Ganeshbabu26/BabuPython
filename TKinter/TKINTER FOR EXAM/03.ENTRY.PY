import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Entry in tkinter")

result = tk.IntVar()

def square():
    num = int(entry.get())
    result.set(num*num)

lb1 = tk.Label(a,text="Enter a number: ")
lb1.pack(pady=5)

entry = tk.Entry(a)
entry.pack(pady=5)

btn = tk.Button(a,text="SQUARE",command=square)
btn.pack(pady=5)

lb2 = tk.Label(a,textvariable=result)
lb2.pack(pady=5)

a.mainloop()