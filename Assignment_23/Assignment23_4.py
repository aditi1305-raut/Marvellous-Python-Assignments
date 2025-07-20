'''
Display Students who scored more than 85 in Science.
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

    print("Students Who Scored More than 85 in Science:")
    #filtered_df = df.query('Science>85')

    #print(filtered_df)

    print(df[df['Science']>=85])
    print(df)

if __name__ =="__main__":
    main()