import tkinter as tk

a = tk.Tk()

a.title("Text box")
a.geometry("500x500")

check = tk.IntVar()

def abc():
    if check.get()==1:
        mylabel.config(text="I agree")
    else:
        mylabel.config(text="I dont agree")

tk.Checkbutton(a,text="Agree or not",variable=check,command=abc,font=("Arial",14)).pack(pady=4)

mylabel = tk.Label(a,text="I dont agree",font=("Arial",14))
mylabel.pack(pady=3)

a.mainloop()