'''
Normalize 'Age' column using min-max Scaling.
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def main():

    data = {'Age':[18,22,25,30,35]}

    df = pd.DataFrame(data)
    print(df)

    normalize_col = 'Age'

    min_val = df[normalize_col].min()
    max_val = df[normalize_col].max()

    df['Age_Normalize'] = (df[normalize_col]-min_val)/(max_val-min_val)
    print(df)



if __name__ == "__main__":
    main()