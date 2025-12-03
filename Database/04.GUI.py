import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox

client = MongoClient("mongodb+srv://ganeshbabumadhavan:Babu7181@babudb.rc7jj7n.mongodb.net/")
db = client["MyMongoDb"]
collection = db["Students"]

# Frontend
a = tk.Tk()
a.geometry("500x500")
a.title("GUI")

name = tk.StringVar()
age = tk.IntVar()

def abcd():
    Name = str(nametext.get("1.0","end-1c"))
    name.set(Name) #set

    Age = int(ageentry.get())
    age.set(Age) #set

    #Inserting
    collection.insert_one(
        {
            "Name": name.get(),
            "Age":age.get()
        }
    )
    print("Inserted successful")
    messagebox.showinfo("Info","Successfully Submitted!")

lbl1 = tk.Label(a,text="Student Details")
lbl1.pack(pady=5)

namelbl = tk.Label(a,text="Enter your name: ")
namelbl.pack(pady=1)

nametext = tk.Text(a,height=1,width=15)
nametext.pack(pady=5)

agelbl = tk.Label(a,text="Enter your age: ")
agelbl.pack(pady=1)

ageentry = tk.Entry(a)
ageentry.pack(pady=5)

btn = tk.Button(a,text="Submit",command=abcd)
btn.pack(pady=10)

a.mainloop()