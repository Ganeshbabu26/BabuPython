import tkinter as tk

a = tk.Tk()
a.title("Entry Field")
a.geometry("500x500")

def abc():
    num = float(entry.get())
    result.set(num*num)

tk.Label(a,text="Enter any number: ").pack(pady=2)

result = tk.IntVar()

entry = tk.Entry(a)
entry.pack(pady=2)

tk.Button(a,text="Square",command=abc).pack(pady=3)

tk.Label(a,textvariable=result).pack(pady=5)

a.mainloop()