'''
Create a dataframe with missing values and fill them with column mean.
'''

import pandas as pd
import numpy as np

data2 = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[np.nan,76,88],
    'Science':[91,np.nan,85]
}

df = pd.DataFrame(data2)
print(df)

print("After Replacing the Missing Values ")
df.fillna(df.mean(numeric_only=True),inplace=True)
print(df)
