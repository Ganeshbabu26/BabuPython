import tkinter as tk

a = tk.Tk()

a.title("Text box")
a.geometry("500x500")

def abc():
    a = str(entry.get("1.0", "end-1c"))
    # MultiLine = ""
    # for i in a:
    #     MultiLine += i+"\n"

    result.set(a[::-1])

result = tk.StringVar()

entry = tk.Text(a,height=5,width=30)
entry.pack(pady=3)

tk.Button(a,text="submit",command=abc).pack(pady=2)
tk.Label(a,textvariable=result,font=("Inter",20)).pack(pady=5)

a.mainloop()