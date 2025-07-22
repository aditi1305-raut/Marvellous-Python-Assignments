'''
Fill Missing Values in a numeric column using interpolation
'''

import pandas as pd
import numpy as np

def main():

    data = {
        'Marks':[85,np.nan,90,np.nan,95]
        }
    
    df = pd.DataFrame(data)

    print("Original Dataframe: ")
    print(df)

    print("Dataframe After Interpolation")
    new_df = df.interpolate()
    print(new_df)


if __name__ == "__main__":
    main()