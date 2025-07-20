'''
Normalize the maths Score using Min_Max scaling.
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math': [85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}

df = pd.DataFrame(data)

print(df)
normalize_col = 'Math'

min_val = df[normalize_col].min()
max_val = df[normalize_col].max()

df[f'{normalize_col}_normalized'] = (df[normalize_col]-min_val)/(max_val-min_val)
print(df)


'''
#Using the Scikit Learn 

scaler = MinMaxScaler()

normalized_data = pd.DataFrame(scaler.fit_transform(df[['Math']]))
print("Normalized Data : ")
print(normalized_data)

'''