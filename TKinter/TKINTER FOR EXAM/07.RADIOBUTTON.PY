import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Radio button in tkinter")

result = tk.StringVar()
result.set("Gender: Male")   # default selection

def check():
    print("selected: ",result.get())

lb1 = tk.Label(a,text="Select: ")
lb1.pack(pady=5)

rb1 = tk.Radiobutton(a,text="Male",variable=result ,value="Gender: Male")
rb1.pack(pady=5)

rb2 = tk.Radiobutton(a,text="Female",variable=result,value="Gender: Female")
rb2.pack(pady=5)

btn = tk.Button(a,text="Check",command=check)
btn.pack(pady=5)

a.mainloop()