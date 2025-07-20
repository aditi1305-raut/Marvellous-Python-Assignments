'''
Create a bar plot of Student names vs total marks.
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

Total_marks = df['Math'] + df['Science']+df['English']

df.insert(4, 'Total',Total_marks)
print(df)

plt.bar(df['Name'] ,df['Total'])
plt.xlabel('Names')
plt.ylabel('Total Marks')
plt.title('Bar Plot of Name vs Total Marks')
plt.legend()
plt.show()
