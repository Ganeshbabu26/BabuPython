import tkinter as tk
from  tkinter import *

# import tkinter 
# from tkinter.constants import * 
# tk = tkinter.Tk() 
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2) 
# frame.pack(fill=BOTH,expand=1) 
# label = tkinter.Label(frame, text="Hello, World") 
# label.pack(fill=X, expand=1) 
# button = tkinter.Button(frame,text="Exit",command=tk.destroy) 
# button.pack(side=BOTTOM) 
# tk.mainloop()

# root = tk.Tk()       # Create a main window
# root.title("My App") # Title of the window
# root.geometry("300x200")  # Set size: width x height
# root.mainloop()      # Display the window

# label = tk.Label(root, text="Hello, Babu!")
# label.pack()


root = tk.Tk()
root.title("Tkinter Label Example")
root.geometry("300x100")

label = tk.Label(root, text="Hello, Babu!")
label.pack()
def click_me():
    print("Button clicked!")
    label = tk.Label(root, text="Hello, Babu!")
    label.pack()    

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()
canvas.create_rectangle(50, 20, 150, 100, fill="red")
canvas.create_oval(150,300,150,100,fill="green")

btn = tk.Button(root, text="Click Me", command=click_me)
btn.pack()

root.mainloop()
