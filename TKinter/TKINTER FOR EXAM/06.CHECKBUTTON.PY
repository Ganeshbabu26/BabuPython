import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Check button in tkinter")

result = tk.StringVar()

def check():
    print("Selected: ",result.get())

lb1 = tk.Label(a,text="Click anything: ")
lb1.pack(pady=5)

ch1 = tk.Checkbutton(a,text="OPTION 1",variable=result,onvalue="Option 1",offvalue="")
ch1.pack(pady=5)

ch2 = tk.Checkbutton(a,text="OPTION 2",variable=result,onvalue="Option 2",offvalue="")
ch2.pack(pady=5)

btn = tk.Button(a,text="CHECK",command=check)
btn.pack(pady=5)

a.mainloop()