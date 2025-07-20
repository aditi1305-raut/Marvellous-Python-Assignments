'''
Apply one hot Encoding to a 'department' column

'''

import pandas as pd

def main():
    data = {
        'Department':["HR","IT","Finance","HR","IT"]

    }

    df = pd.DataFrame(data)
    print("Original Data Frame: ")
    print(df)

    df_encoded = pd.get_dummies(df,columns=['Department'])
    print("One hot Encoded Data Frame")
    print(df_encoded)

if __name__ == "__main__":
    main()