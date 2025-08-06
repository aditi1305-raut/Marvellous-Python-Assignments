import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score , r2_score ,confusion_matrix
from sklearn.metrics import precision_score,recall_score,f1_score

import matplotlib.pyplot as plt
import seaborn as sns

def DataPreprocessing(data):

    Border = "-"*90
    print(Border)

    print("Dataset Loaded Successfully..!!!")
    df = pd.DataFrame(data=data.data,columns=data.feature_names)
    print(df.head().T)

    print(Border)

    print("Checking the dataset have missng value: ")
    print(df.isna().sum())

    print(Border)

    
    df['target']=data.target
    print(df)

    print(Border)
    print("Size of the Dataset and Column Names: ")
    print(df.shape)
    print(df.columns.tolist())

    
    print("Stastical Information of the Data: ")
    print(df.describe())
    
    print(Border)

    print(data.keys())

    return df
    

def VisualRepresentation(df):
    

    df["target"].value_counts()

    df["target"].value_counts().plot(kind="bar",color=["Peru","darkmagenta"])
    plt.show()

    # print("Correlation Matrix")

    # corr_matrix = df.corr()
    # fig,ax = plt.subplot()
    # ax = sns.heatmap(corr_matrix)
    # plt.show()

def Model_Selection(data,df):

    X = data.data
    Y = data.target

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    X_train , X_test,Y_train ,Y_test = train_test_split(x_scaled,Y,test_size=0.2,random_state=42)

    rf_clf = RandomForestClassifier(n_estimators=150,max_depth=7,random_state=42)
    knn_clf = KNeighborsClassifier(n_neighbors=5)
    lr_clf = LogisticRegression(max_iter=100)

    voting_clf = VotingClassifier(
        estimators=[
            ('rf',rf_clf),
            ('knn',knn_clf),
            ('lr',lr_clf)
    
        ],voting='hard'
    )

    voting_clf.fit(X_train,Y_train)

    y_pred = voting_clf.predict(X_test)

    Accuracy = accuracy_score(Y_test,y_pred)

    print("Accuracy of the model : ",Accuracy*100)

    print("Confusion Matrix for the model: ")
    
    conf_matrix = confusion_matrix(Y_test,y_pred)
    print(conf_matrix)

    return scaler , voting_clf
    

def main():

    data = load_breast_cancer()
    dataframe = DataPreprocessing(data)

    VisualRepresentation(dataframe)

    scaler, model = Model_Selection(data, dataframe)  
      
    # ✅ Sample to predict (first record from dataset)
    sample = data.data[0].reshape(1, -1)
    sample_scaled = scaler.transform(sample)

    prediction = model.predict(sample_scaled)

    print("Prediction for the sample is:", "Malignant" if prediction[0] == 0 else "Benign")


if __name__ == "__main__":
    main()

