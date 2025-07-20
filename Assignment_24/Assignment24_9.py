'''
Rename 'Math' column to 'Mathematics'

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

renamed_col = df.rename(columns={'Math':'Mathematics'})
print(renamed_col)

