a = int(input("Enter a tuple length: "))
t = ()
for i in range(a):
    b = input(f"Enter value {i+1}: ")
    x = (b,)    #() and , makes it a tuple with one instant element, because tuple only concatenate with tuple
    t = t+x
print(t)

t = ()
while True:
    a = input("Enter anything (leave blank to stop): ")
    if a == "":
        break
    b = (a,)
    t = t + b
print(t)