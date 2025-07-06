n = int(input("Enter your mark: "))

if n<=100 and n>90:
    print("Exellent")
elif n<=90 and n>80:
    print("very good")
elif n<=80 and n>70:
    print("Good")
elif n<=70 and n>60:
    print("Above average")
elif n<=60 and n>50:
    print("Average")
elif n<=50 and n>40:
    print("Below average")
elif n<=40 and n>35:
    print("Just pass")
else:
    print("Fail")
