'''
Replace Multiple Values in Column using a Dictionary
'''

import pandas as pd

def main():

    data = {
        'Grade':['A+','B','A','C','B+']
    }

    df = pd.DataFrame(data)
    print("original Dataframe: ")
    print(df)

    dict_replacement = {'A+':'Excellent','A':'Very Good','B+':'Good','B':'Average','C':'Poor'}

    df['Grade'] = df['Grade'].replace(dict_replacement)
    print("DataFrame After Replacement: ")
    print(df)


if __name__ == "__main__":
    main()