class Sorting:
    def __init__(self,arr):
        self.arr = arr
        if self.valuable() == False:
            print("No values")
        self.result()

    def valuable(self):
        return len(self.arr) > 0
    
    def partition(self,low,high):
        if self.valuable():
            pivot= self.arr[high]
            i = low -1

            for j in range(low,high):
                if self.arr[j] < pivot:
                    i += 1
                    self.swap(i,j)
            self.swap(i+1,high)
            return i+1
    
    def swap(self,i,j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
    
    def quickSort(self,low,high):
        if self.valuable():
            if low < high:
                pi = self.partition(low,high)

                self.quickSort(low,pi-1)
                self.quickSort(pi+1,high)

    def result(self):
        if self.valuable():
            n = len(self.arr)-1
            self.quickSort(0,n)
            print(self.arr)


class ISort:
    def __init__(self):
        self.result()
    
    def Input(self):
        a = []
        while True:
            n = input("Enter a number: ")
            if n=="":
                break
            a.append(int(n))
        return a

    def result(self):
        data = self.Input()
        obj = Sorting(data)

o2 = ISort()