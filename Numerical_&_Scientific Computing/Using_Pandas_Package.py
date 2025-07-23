import pandas as pd

data = {
    'ID':   list(range(1,11+1,1)),
    'REGISTER NO' : list(range(622200001,622200011+1,1)),
    'NAME': ['Dhayanidhi','Dilliganesh','Ganeshbabu','Laksmanan','Saran keerthi','Vignesh','Yuvaraj','Karishma','Nethra','Deerajkumar','Aakhash'],
    'Assignment1': ['SS','SS','PL','PL','PL','RR','RR','RR','KP','KP','KP']
}

DT = pd.DataFrame(data)

print(DT)
print("Names:")
print( DT['NAME'])
