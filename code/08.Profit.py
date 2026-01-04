def maxProfit(values):
    min = float('inf')
    maxi = 0
    for num in values:
        if num < min:
            min = num
        else:
            maxi = max(maxi,num-min)
    return maxi
a = [3,4,5,33,23,6,2]
print(maxProfit(a))



def maxProfit(values):
    if not values:
        return 0,0,0
    
    Min = float('inf')
    Max = 0

    temp = 0
    buyDay = 0
    sellDay = 0

    for i, num in enumerate(values):
        if num < Min:
            Min = num
            temp = i+1
        elif num - Min > Max:
            Max = num - Min
            buyDay = temp
            sellDay = i+1
    return buyDay, sellDay, Max

a = [9,4,5,33,23,6,2]
buy, sell, profit = maxProfit(a)
print(f"BuyDay : {buy}, SellDay : {sell}, Profit : {profit}")



