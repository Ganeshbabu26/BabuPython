import os

if os.path.exists("Babu.txt"):
    os.remove("Babu.txt")
    print("Successfully deleted!")
else:
    print("File not found")