'''
Detect the outliers in the salary column using IQR method

'''
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

def main():

    data = {'Salary': [25000,27000,29000,31000,50000,100000]}

    df = pd.DataFrame(data)

    #Sorting data in ascending Order
    sort_data = np.sort(df['Salary'])
    print(sort_data)

    #Calculating Q1 , Q2 , Q3 and IQR

    Q1 = np.percentile(df['Salary'],25,interpolation = 'midpoint')
    print('Q1 25 Percentile of the given data is : ',Q1)

    Q2 = np.percentile(df['Salary'],50,interpolation = 'midpoint')
    print('Q1 50 Percentile of the given data is : ',Q2)

    Q3 = np.percentile(df['Salary'],75,interpolation = 'midpoint')
    print('Q1 50 Percentile of the given data is : ',Q3)

    IQR = Q3 - Q1 
    print("Interquartile range is : ",IQR)

    #Find the Lower and Upper Limits
    low_lim = Q1 - 1.5 * IQR
    up_lim = Q3 + 1.5 * IQR
    print("Lower Limit is : ",low_lim)
    print("Upper Limit is : ",up_lim)

    #Identify the outliers 
    outlier = []
    for x in df['Salary']:
        if ((x>up_lim) or (x<low_lim)):
            outlier.append(x)
    print('Outlier in the data set is : ',outlier)

    #Plot the box plot to highlight the outliers

    sns.boxplot(df['Salary'])
    plt.show()

if __name__ == "__main__":
    main()