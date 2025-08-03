try:
    file = open("Babu.txt","a")
    file.write("\nSample 3rd line")
    file.close()

    file = open("Babu.txt","r")
    print(file.read())

except Exception as e:
    print(e)