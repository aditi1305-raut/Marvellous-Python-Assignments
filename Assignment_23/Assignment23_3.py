'''
Add a new column 'Total' to the dataframe as the sum of all subject marks.
'''

import pandas as pd
data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math': [85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]

}

df = pd.DataFrame(data)

print(df)

Total_marks = df['Math'] + df['Science']+df['English']


df.insert(4, 'Total',Total_marks)

print(df)

df['Total'] = df['Math'] + df['Science']+df['English']
print(df)