
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,accuracy_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import VotingClassifier

import joblib


def DataPreprocessing(Datapath):

    border = "*"*90
    print(border)

    print("Dataset Loaded Successfully..!!")
    print(border)
    
    df = pd.read_csv(Datapath,delimiter=';')
    print("Sample Data from the Dataset: ")  
    print(df.head())
    print(border)

    print("Columns in the dataset: ")
    print(df.columns)
    print(border)

    print("Information of the Dataset: ")
    print(df.info())
    print(border)

    print("Stastical Information of the Dataset: ")
    print(df.describe())
    print(border)
    print(df.shape)
     
    print("After dropping unnecessary Columns: ")
    
    print("Column names in the dataset:")
    print(df.columns.tolist())

    df.columns = df.columns.str.strip()

    df.drop(["contact", "day", "duration"], axis=1, inplace=True,errors="ignore")
 
    print(df.head())
    print(df.shape)
    print(border)

    
    
    print("Encoding the Data: ")
    
    label_encoders = {}
    for col in df.select_dtypes(include='object'):
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    print(df.head())
    print(border)

    joblib.dump(label_encoders, 'label_encoders.pkl')  # ✅ Save all label encoders


    print("Handling the missing and Unknown Values in the dataset: ")
    
    for col in df.columns:
        if df[col].dtype == 'object':
            # Check if 'unknown' exists in the column
            if (df[col] == 'unknown').any():
                mode_value = df.loc[df[col] != 'unknown', col].mode()[0]
                df[col] = df[col].replace('unknown', mode_value)

    
    print(df.head(10))
    print(border)

    df.columns = df.columns.str.strip().str.replace('"', '')

    X = df.drop(columns='y',axis=1)
    Y = df['y']

    scaler = StandardScaler()

    x_scaled = scaler.fit_transform(X)

    X_train , X_test , Y_train , Y_test = train_test_split(x_scaled,Y,test_size=0.2,random_state=42)

    log_clf = LogisticRegression()                         #Logistic Regression
    rf_clf = RandomForestClassifier(max_depth=8)          #Decison Tree classifier
    knn_clf = KNeighborsClassifier(n_neighbors=3)          #KNN
    
    voting_clf = VotingClassifier(
          estimators = [
                    ('lr',log_clf),
                    ('rf',rf_clf),
                    ('knn',knn_clf)
                ],
                voting='hard'
            )
    
    voting_clf.fit(X_train,Y_train)
    y_pred = voting_clf.predict(X_test)

    Accuracy = accuracy_score(Y_test,y_pred)*100
    print("Accuracy of the model is : ",Accuracy)
    print(border)

    # prediction = voting_clf.predict(df)[0]
    # print("Prediction:", "Subscribed (yes)" if prediction == 1 else "Not Subscribed (no)")

    # importance = pd.Series(model.feature_importances_,index=X.columns)
    # importance = importance.sort_values(ascending=False)

    # importance.plot(kind='bar',figsize=(10,6),title="Feature Importance")
    # plt.show()/
    joblib.dump(voting_clf, 'voting_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    joblib.dump(le, 'label_encoders.pkl')
    joblib.dump(X.columns.tolist(), 'features.pkl')  # Save column order


    return x_scaled , Y ,Accuracy



def MakePredictions():
    model = joblib.load('voting_model.pkl')
    scaler = joblib.load('scaler.pkl')
    label_encoders = joblib.load('label_encoders.pkl')
    features = joblib.load('features.pkl')

    new_data = {
        'age': 35,
        'job': 'technician',
        'marital': 'married',
        'education': 'secondary',
        'default': 'no',
        'balance': 200,
        'housing': 'yes',
        'loan': 'no',
        'month': 'may',
        'campaign': 1,
        'pdays': 999,
        'previous': 0,
        'poutcome': 'unknown'
    }

    input_df = pd.DataFrame([new_data])

    for col, encoder in label_encoders.items():
        if col in input_df.columns:
            input_df[col] = encoder.transform(input_df[col])

    input_df = input_df[features]
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]
    print("Prediction:", "✅ Subscribed (yes)" if prediction == 1 else "❌ Not Subscribed (no)")

def main():

    Dataset = "bank-full.csv"

    DataPreprocessing(Dataset)

    MakePredictions()   
    
if __name__ == "__main__":    
    main()
