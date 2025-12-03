import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox

a = tk.Tk()
a.geometry("500x500")
a.title("Student Details")

client = MongoClient("mongodb+srv://ganeshbabumadhavan:Babu7181@babudb.rc7jj7n.mongodb.net/")
db = client["GUI"]
collection = db["Students"]

name = tk.StringVar()
age = tk.IntVar()
gender = tk.StringVar()
status = tk.StringVar()
phone = tk.IntVar()
address = tk.StringVar()

def abcd():
    Name = str(nametext.get("1.0","end-1c"))
    Age = int(ageentry.get())
    Gender = gender.get()
    Status = status.get()
    Phone = int(phonenumber.get())
    Address = str(addresstext.get("1.0","end-1c"))

    UserData = { 
        "Name":Name,
        "Age":Age,
        "Gender":Gender,
        "Status":Status,
        "Phone":Phone,
        "Address":Address
        }
    
    collection.insert_one(UserData)

    messagebox.showinfo("Info","Submitted successful")

# 1. Name
namelabel = tk.Label(a,text="Enter your name: ")
namelabel.pack()

nametext = tk.Text(a,width=15,height=1)
nametext.pack(pady=1)

# 2. Age
agelabel = tk.Label(a,text="Enter your age: ")
agelabel.pack()

ageentry = tk.Entry(a)
ageentry.pack(pady=1)

# 3. Gender
genderlabel = tk.Label(a,text="Enter your gender: ")
genderlabel.pack()

genderradio1 = tk.Radiobutton(a,text="Male",variable=gender,value="Male")
genderradio1.pack()

genderradio2 = tk.Radiobutton(a,text="Female",variable=gender,value="Female")
genderradio2.pack()

# 4. Status
statuslabel = tk.Label(a,text="IsMarried?")
statuslabel.pack()

statuscheckbox1 = tk.Checkbutton(a,text="Married",variable=status,onvalue="Married",offvalue="")
statuscheckbox1.pack()

statuscheckbox2 = tk.Checkbutton(a,text="Not Married",variable=status,onvalue="Not Married",offvalue="")
statuscheckbox2.pack()

# 5. Phone
phonelabel = tk.Label(a,text="Enter your phone number: ")
phonelabel.pack()

phonenumber = tk.Entry(a)
phonenumber.pack()


# 6. Address
addresslabel = tk.Label(a,text="Enter your address: ")
addresslabel.pack()

addresstext = tk.Text(a,height=2,width=30)
addresstext.pack()

btn = tk.Button(a,text="Submit",command=abcd)
btn.pack(pady=10)

a.mainloop()