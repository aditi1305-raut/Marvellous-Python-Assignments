'''
plot a boxplot for English  marks to check the distribution and outliers 

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

Subject = df['English']
plt.boxplot(Subject) #bins control the number of bars
plt.xlabel('Marks Of English')
plt.ylabel('Number Of Students')
plt.show()
plt.title("Boxplot for English Marks")

