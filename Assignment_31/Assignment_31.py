import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score

import matplotlib.pyplot as plt

def DataPreprocessing(Datapath):

    Border = "*"*90
    print(Border)

    print("Data Loaded Successfully..!!!")
    
    df= pd.read_csv(Datapath)
    print(df.head())

    Label= LabelEncoder()
    df['CancerType'] = Label.fit_transform(df['CancerType'])

    print("After Encoding the Data: ")
    print(df.head())


    print(Border)
    print("Size of the Dataset: ")
    print(df.shape)

    print(Border)
    df.drop('CodeNumber',axis=1,inplace=True)

    print("Displaying the Stastical Information: ")
    print(df.describe())
    print(Border)

    mode_values = {}
    for col in df.columns:

        if ( df[col]== '?').any():
            mode_value = df.loc[df[col] != '?',col].mode()[0]
            df[col] = df[col].replace('?',mode_value)
            mode_values[col] = mode_value
        else:
            mode_values[col] = df[col].mode()[0]



    print(df.head(45))
    print(df['BareNuclei'].head(45))

    X = df.drop('CancerType',axis=1)
    Y = df['CancerType']

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    X_train, X_test , Y_train , Y_test = train_test_split(x_scaled,Y,test_size=0.2,random_state=42)

    rf_clf = RandomForestClassifier(n_estimators=150,max_depth=7,random_state=42)
    dt_clf = DecisionTreeClassifier(max_depth=10)
    
    voting_clf = VotingClassifier(
        estimators=[
            ('rf',rf_clf),
            ('dt',dt_clf)
        ],
        voting='hard'
    )

    voting_clf.fit(X_train,Y_train)
    y_pred = voting_clf.predict(X_test)

    Accuracy = accuracy_score(Y_test,y_pred)

    print("Accuracy of the model : ",Accuracy*100)

    
    
    from sklearn.inspection import permutation_importance
    import numpy as np

    result = permutation_importance(
        voting_clf, X_test, Y_test,
        scoring='accuracy',
        n_repeats=20, random_state=42, n_jobs=-1
    )

    perm_imp = pd.Series(result.importances_mean, index=X.columns)\
                .sort_values(ascending=False)

    perm_imp.plot(kind='bar', figsize=(10,5), title="Permutation Importance")
    plt.ylabel("Mean decrease in accuracy")
    plt.show()


    return voting_clf,scaler,Label,list(X.columns),mode_values



def Cancer_Prediction(sample: dict, voting_clf, scaler, encoder, feat_names: list, mode_values: dict):
    # Build dataframe and ensure order
    df_new = pd.DataFrame([sample], columns=feat_names)

    # Impute and convert types
    for col in df_new.columns:
        val = df_new.at[0, col]
        if str(val) == '?' or pd.isna(val):
            df_new.at[0, col] = mode_values[col]  # mode of that feature from training
    df_new = df_new.fillna(value=mode_values)

    df_new = df_new.astype(int)

    # Scale and predict
    X_new = scaler.transform(df_new)
    pred_enc = voting_clf.predict(X_new)[0]
    return encoder.inverse_transform([pred_enc])[0]

def main():

    dataset = "breast-cancer-wisconsin.csv"

    voting_clf , scaler , Label , feat_names ,mode_values = DataPreprocessing(dataset)

    sample_row = {
        "ClumpThickness": 10,
        "Uniformity_of_Cell_Size": 8,
        "Uniformity_of_Cell_Shape": 8,
        "Marginal_Adhesion": 10,
        "Single_Epithelial_Cell_Size": 8,
        "BareNuclei": 7,  # Make sure this is integer, not string
        "Bland_Chromatin": 10,
        "Normal_Nucleoli": 7,
        "Mitoses": 1

    }

    Prediction = Cancer_Prediction(sample_row,voting_clf,scaler,Label,feat_names,mode_values)
    if (Prediction == 2):
        print("Predicted Cancer Type: benign ")
    
    else:
        print("Predicted Cancer Type: malignant ")
    

if __name__ == "__main__":
    main()