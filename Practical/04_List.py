list = [10,20,30,40,50]

print("\n-----1. append-----")
list.append(60)
print(list)

print("\n-----2. insert-----")
list.insert(2,25)  #(index,element)
print(list)

print("\n-----3. extend-----")
list.extend([70,80,90,100])
print(list)

print("\n-----4. pop-----")
list.pop(10) #index
print(list)

print("\n-----5. remove-----")
list.remove(90) #element
print(list)

print("\n-----6. reverse-----")
list.reverse()
print(list)

print("\n-----7. clear-----")
list.clear()
print(list)