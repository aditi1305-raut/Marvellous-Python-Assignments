'''
Replace 'Pooja' with 'Puja' in the 'Name' column .
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

print("Dataframe after Replacement: ")
#df.replace('Pooja','Puja',inplace = True)
df['Name'] = df['Name'].replace('Pooja','Puja',inplace=True)
print(df)