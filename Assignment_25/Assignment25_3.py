'''
Apply Label Encoding to a 'City' column .
'''
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {

    'City':['Pune','Mumbai','Delhi','Pune','Delhi']
}

df = pd.DataFrame(data)

print("Original Data Frame")
print(df)

le = LabelEncoder()

df['City_Encoded'] = le.fit_transform(df['City'])
print("Dataframe After Label ")
print(df) 