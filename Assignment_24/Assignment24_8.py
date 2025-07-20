'''
plot a histogram of maths marks 

'''

import pandas as pd
import matplotlib.pyplot as plt 

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math': [85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]

}

df = pd.DataFrame(data)
print(df)

math = df['Math']
plt.hist(math , bins =5,edgecolor='black') #bins control the number of bars
plt.xlabel('Marks Of Maths')
plt.ylabel('Number Of Students')
plt.show()

