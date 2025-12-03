import tkinter as tk

a = tk.Tk()
a.geometry("400x300")
a.title("Scrollbar Example")

# Text widget
text = tk.Text(a, width=40, height=10)
text.pack(side="left", fill="both", expand=True)

# Scrollbar
scroll = tk.Scrollbar(a)
scroll.pack(side="right", fill="y")

# Connect scrollbar to text
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

a.mainloop()
