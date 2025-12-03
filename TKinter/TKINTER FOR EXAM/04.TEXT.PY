import tkinter as tk

a = tk.Tk()
a.geometry("500x500")
a.title("Text in tkinter")

result = tk.StringVar()

def reverse():
    string = str(text.get("1.0","end-1c"))
    result.set(string[::-1])

lb1 = tk.Label(a,text="Enter anything: ")
lb1.pack(pady=5)

text = tk.Text(a,height=5,width=30)
text.pack(pady=5)

btn = tk.Button(a,text="REVERSE",command = reverse)
btn.pack(pady=5)

lb2 = tk.Label(a,textvariable=result, font=("Arial", 14))
lb2.pack(pady=5)

a.mainloop()