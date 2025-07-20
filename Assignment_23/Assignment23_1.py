'''
Q1. Create a dataframe for student marks and print basic information like shape , columns , and data types

'''

import pandas as pd 
def main():

    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math': [85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }

    df = pd.DataFrame(data)

    print(df)

    #Printing Shape
    print("Shape: ",df.shape)

    #Printing the column name
    print("Columns: ",df.columns)

    #printing the data type 
    print("Datatype : ",df.dtypes)

if __name__ == "_-main__":
    main()