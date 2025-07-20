'''
Add a New Column status where students with total >= 250 are Pass ,else fail

'''

import pandas as pd
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

df['Status'] = df['Total'].apply(lambda x: 'Pass' if x>=250 else 'Fail')
print(df)