import tkinter as tk

a = tk.Tk()
a.title("Check button")
a.geometry("500x500")

def greet():
    lbl.config(text=var.get())
    print("Selected: ",var.get())
    # print("Selected: ",var.get() if var.get() !="" else "Not selected" )

var = tk.StringVar()

chk1 = tk.Checkbutton(a,text="Option 1", variable=var, onvalue="Option 1 is selected", offvalue="")
chk1.pack(pady=5)

chk2 = tk.Checkbutton(a,text="Option 2", variable=var, onvalue="Option 2 is selected", offvalue="")
chk2.pack(pady=5)

lbl = tk.Label(a,text="")
lbl.pack(pady=5)

btn = tk.Button(a,text="OK",command=greet)
btn.pack(pady=5)

a.mainloop()