'''
Plot a pie chart of subject marks for Sagar
'''
import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math': [85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}

df = pd.DataFrame(data)

print(df)

df.set_index('Name',inplace=True) # Make Name the index

sagar = df.loc['Sagar']   #Amit = Series of Marks

plt.figure(figsize=(8,8))
subjects = df['Math','Science','English']
plt.pie(sagar.index,autopct='%1.1f%%',startangle=90)
plt.title("Sagar's Marks Distribution")
plt.show()


