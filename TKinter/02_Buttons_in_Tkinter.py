import tkinter as tk

a = tk.Tk()

a.geometry("500x500")
a.title("Buttons in tkinter")

def abc():
    print(tk.Label(a,text="sample button1").pack())
    return tk.Label(a,text="sample button2").pack()

button = tk.Button(a,text="abc",command=abc)
button.pack(pady=3)
a.mainloop()