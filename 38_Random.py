import random as rd

a = "abcdefghijklmnopqrstuvwxyz"
b = []
for i in a:
    b.append(i)

c = []

for i in range(1,201):
    c.append(f"{i:3}{rd.choice(b)}")

for i in c:
    print(i)