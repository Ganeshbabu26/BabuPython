import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox

client = MongoClient("mongodb+srv://ganeshbabumadhavan:Babu7181@babudb.rc7jj7n.mongodb.net/")
db = client["NewStudents"]
collection = db["Students"]

a = tk.Tk()
a.geometry("500x500")
a.title("Student details")

gender = tk.StringVar()
status = tk.StringVar()
viewAll = tk.StringVar()

def abcd():
    Name = entryname.get()
    Age = int(entryage.get())
    Gender = gender.get()
    Status = status.get()
    Address = str(addresstext.get("1.0","end-1c"))

    UserData = {
            "Name":Name,
            "Age":Age,
            "Gender":Gender,
            "Status":Status,
            "Address":Address
        }
    
    if Name !="" and Age!=None:
        collection.insert_one(UserData)
        messagebox.showinfo("Info",message="Inserted successful")
    else:
        messagebox.showerror("Error","Insertion failed")

def view():
    win = tk.Toplevel(a)
    win.title("All Students")
    win.geometry("500x500")

    # Fetch data
    all_data = collection.find()
    output = ""

    for d in all_data:
        output += f"Name: {d.get('Name')} | Age: {d.get('Age')} | Gender: {d.get('Gender')} | Status: {d.get('Status')} | Address: {d.get('Address')}\n\n"

    if output == "":
        output = "No records found"

    # Text box to show results
    text = tk.Text(win, width=60, height=25)
    text.insert(tk.END, output)
    text.pack(pady=10)

    # Back button (close window)
    btn = tk.Button(win, text="Back to Home", command=win.destroy)
    btn.pack(pady=10)



# ------------------ RESET --------------------
def reset():
    entryname.delete(0, tk.END)
    entryage.delete(0, tk.END)
    gender.set("Male")
    status.set("")
    addresstext.delete("1.0", tk.END)
    viewAll.set("")

label = tk.Label(a,text="Student form",font="Arial")
label.pack(pady=5)

labelname = tk.Label(a,text="Enter your name: ")
labelname.pack()

entryname = tk.Entry(a)
entryname.pack()

labelage = tk.Label(a,text="Enter your age: ")
labelage.pack()

entryage = tk.Entry(a)
entryage.pack()

labelgender = tk.Label(a,text="Enter your gender: ")
labelgender.pack()

radiogender = tk.Radiobutton(a,text="Male",variable=gender,value="Male")
radiogender.pack()

radiogender2 = tk.Radiobutton(a,text="Female",variable=gender,value="Female")
radiogender2.pack()

statuslabel = tk.Label(a,text="Married or Not?")
statuslabel.pack()

statuscheck = tk.Checkbutton(a,text="Married",variable=status,onvalue="Married",offvalue="")
statuscheck.pack()

statuscheck2 = tk.Checkbutton(a,text="Not Married",variable=status,onvalue="Not Married",offvalue="")
statuscheck2.pack()

addresslabel = tk.Label(a,text="Enter your address: ")
addresslabel.pack()

addresstext = tk.Text(a,height=5,width=30)
addresstext.pack()

btn = tk.Button(a,text="Submit",command=abcd)
btn.pack(pady=10)

btn2 = tk.Button(a,text="View All",command=view)
btn2.pack(pady=5)

btn3 = tk.Button(a,text="Reset",command=reset)
btn3.pack(pady=5)

labelviewall = tk.Label(a,textvariable=viewAll)
labelviewall.pack()

a.mainloop()