content = '''
try:
    a = 10/0
    print(a)
except Exception as e:
    print(e)
'''

with open("35_Try_Catch.py","w") as file:
    file.write(content)

with open("35_Try_Catch.py","r") as file:
    code = file.read()
    print(code)
    print("Output:\n")
    exec(code)

with open("29_Convert_Number_To_Words.py") as file:
    code = file.read()
    exec(code)