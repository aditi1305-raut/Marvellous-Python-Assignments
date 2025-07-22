'''
Replace values in 'Marks' less than 50 with 'Fail' using where() 
'''

import pandas as pd
import numpy as np

def main():

    data = {
        'Marks' : [45,67,88,32,76]
    }

    df = pd.DataFrame(data)
    print("Original DataFrame")
    print(df)

    print("DataFrame After Changes: ")
    #df['Marks'] = df['Marks'].where(df['Marks']<50)
    df['Marks'] = np.where(df["Marks"]<50,'Fail',df["Marks"])
    print(df)
    
    
    
    
    
    
if __name__ == "__main__":    
    main()