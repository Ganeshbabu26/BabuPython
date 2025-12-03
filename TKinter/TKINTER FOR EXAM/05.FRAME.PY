import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Frame in tkinter")

def abc():
    print("Button clicked")

frame = tk.Frame(a)
frame.pack()

label = tk.Label(frame,text="This is label")
label.pack(pady=5)

btn1 = tk.Button(frame,text="Click",command=abc)
btn1.pack(pady=5)

a.mainloop()
