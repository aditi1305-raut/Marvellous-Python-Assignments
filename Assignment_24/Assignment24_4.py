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


#subjects = df['Math','Science','English']
Marks = df[df['Name']=='Sagar'][['Math','Science','English']].values.flatten()  #flatten - Convert 2D into 1D
subjects= ['Math','Science','English']

fig=plt.figure(figsize=(10,7))
plt.pie(Marks,labels=subjects)
plt.title("Sagar's Marks Distribution")
plt.show()


