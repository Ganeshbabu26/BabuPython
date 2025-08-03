try:
    file = open("35_Try_Catch.py","r")
    print(file.readline())
    print(file.readline(5))
    print(file.readlines())

except Exception as e:
    print(e)