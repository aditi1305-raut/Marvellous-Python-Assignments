'''
Print the descriptive stastics using .describe()
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

    # Printing the descriptive stastical information
    print("Output of Describe Method")
    print(df.describe())

if __name__ =="__main__":
    main()