class student:
    def __init__(self,total):
        self._total = total

    def average(self):
        return self._total /5
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,t):
        if t<=0 or t>=500:
            print("Invalid total")
        else:
            self._total = t
    
o = student(450)
print("Total: ",o.total)
print(o.average())
o.total = 550
print("Total: ",o.total)
print(o.average())