import pandas as pd 
a = [1,2,3]

val = pd.Series(a)
val1 = pd.Series(a,index = ['x','y','z'])

print(val)
print(val1)

# dictionary in Series 
calories = {'day1':420,'day2':450,'day3':480}
a1 = pd.Series(calories)
a2 = pd.Series(calories,index=['day1','day2'])
print(a1)
print(a2)