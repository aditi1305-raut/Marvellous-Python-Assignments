'''
Sort the dataframe by 'Total Marks' in descending order.
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

print("Data Before Sorting ")
print(df)

print("After Sorting in Descending Order ")

sorted_df = df.sort_values(by='Total',ascending=False)
print(sorted_df)