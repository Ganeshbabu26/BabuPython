import tkinter as tk

a = tk.Tk()
a.title("Checkbox")
a.geometry("500x500")

def greet():
    print("Selected: ", var.get())

var = tk.StringVar()

label = tk.Label(a,text="Selected checkbox")
label.pack(pady=5)

ch1 = tk.Checkbutton(a,text="Option 1", variable=var, onvalue="option 1 is active", offvalue="")
ch1.pack(pady=5)

ch2 = tk.Checkbutton(a,text="Option 2", variable=var, onvalue="Option 2 ", offvalue="")
ch2.pack(pady=5)

button = tk.Button(a,command=greet, text="Check")
button.pack(pady=5)

label = tk.Label(a,textvariable=var)
label.pack(pady=5)

a.mainloop()