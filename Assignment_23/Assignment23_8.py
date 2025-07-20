'''
plot a line chart of marks for 'Amit' across all subjects 
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

Marks = df[df['Name']=='Amit'][['Math','Science','English']].values.flatten()  #flatten - Convert 2D into 1D
subjects= ['Math','Science','English']

plt.plot(subjects,Marks,marker='o')
plt.xlabel("subjects")
plt.ylabel("Marks")
plt.title("Amit Report")
plt.grid(True)
plt.show()