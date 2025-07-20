'''
Create a Gender column and perform one-hot encoding 
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

gen_val = ['Male','Male','Female']
df.insert(4,'Gender',gen_val)

print("Encoded DataFrame: ")

df_encoded = pd.get_dummies(df,columns=['Gender'],drop_first=True)

print(df_encoded)