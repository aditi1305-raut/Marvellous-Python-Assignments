


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,accuracy_score
import matplotlib.pyplot as plt



def DataPreprocessing(Datapath):

    df = pd.read_csv(Datapath,delimiter=';')
    print(df.head())

    print("Columns in the dataset: ")
    print(df.columns)

    print("Information of the Dataset: ")
    print(df.info())

    print("Stastical Information of the Dataset: ")
    print(df.describe())

    print(df.shape)

    #print("Handling the missing Values in the dataset: ")
    
    # for column in df.columns:
    #     if df[column].dtype == 'object':
    #         if "unknown" in df[column].values:
    #             mode_val = df[column].mode()
    #             df[column]=df[column].replace('unknown',mode_val,inplace=True)
    #             #df.fillna(df[column].mode()[0],inplace=True)
    # print(df.head(10))
    
    
    print("After dropping unnecessary Columns: ")
    
    print("Column names in the dataset:")
    print(df.columns.tolist())

    df.columns = df.columns.str.strip()

    df.drop(["contact", "day", "duration"], axis=1, inplace=True,errors="ignore")

    
    
    print(df.head())
    print(df.shape)

    for col in df.select_dtypes(include = 'object'):
        df[col]=LabelEncoder().fit_transform(df[col])

    print(df.head())

    df.columns = df.columns.str.strip().str.replace('"', '')

    X = df.drop(columns='y',axis=1,inplace=True)
    Y = df['y']

    model = RandomForestClassifier(n_estimators=150,max_depth=7,random_state=42)
    importance = pd.Series(model.feature_importances_,index=X.columns)
    importance = importance.sort_values(ascending=False)

    importance.plot(kind='bar',figsize=(10,6),title="Feature Importance")
    plt.show()

# Load the dataset
#df = pd.read_csv('data.csv', delimiter=';')

# Loop through each column to replace 'unknown' with mode
    # for col in df.columns:
    #     if df[col].dtype == 'object':
    #         # Check if 'unknown' exists in the column
    #         if (df[col] == 'unknown').any():
    #             mode_value = df.loc[df[col] != 'unknown', col].mode()[0]
    #             df[col] = df[col].replace('unknown', mode_value)

    # # Optional: Display updated dataframe
    # print(df.head(10))

    # for col in df.columns:
    #     if df[col].dtype == 'object':
    #         count = (df[col] == 'unknown').sum()
            
    #         print("Number of Unknown values: ")
    #         print(f"{col}: {count}" )

def main():

    Dataset = "bank-full.csv"

    DataPreprocessing(Dataset)
    
    
    
if __name__ == "__main__":    
    main()