'''
Group Students by Gender and Calculate average-marks
'''

import pandas as pd 

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math': [85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}

df = pd.DataFrame(data)

gen_val = ['Male','Male','Female']
df.insert(4,'Gender',gen_val)

Total_marks = df['Math'] + df['Science']+df['English']

df.insert(4, 'Total',Total_marks)

print(df)

grouped_data = df.groupby('Gender')['Total'].mean()
print(grouped_data)

