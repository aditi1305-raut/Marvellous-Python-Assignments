'''
Play Predictor using K-Nearest Neighbors (KNN)

This project implements a Machine Learning classification model to predict whether to play or not 
based on weather and temperature conditions. It uses the K-Nearest Neighbors (KNN) algorithm for 
classification.

📂 Dataset
The dataset includes:

Features:
Weather: Sunny, Overcast, Rainy
Temperature: Hot, Mild, Cold

Target:
Play: Yes / No

'''

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

def KNNPlayPredictor(Datapath):

    #Step -1 : Get the data
    df = pd.read_csv(Datapath)
    #print(df)
    print("Data Loaded Successfully")

    #Step -2 : Clean , Prepare and Maipulate Data
    print(df.head())

    print("Dataset after cleaning: ")
    df.drop(columns='Unnamed: 0',axis=1,inplace=True)
    print(df.head())

    print("Shape of the Dataset: ",df.shape)

    #print("Check whether a dataset have any missing value:")
    #print(df.isnull())

    #print(df.describe())
      
    label_encoder = LabelEncoder()

    df['Whether'] = label_encoder.fit_transform(df['Whether'])
    df['Temperature'] = label_encoder.fit_transform(df['Temperature'])

    df['Play'] = label_encoder.fit_transform(df['Play'])

    print("""
    Encoded Labels for Weather:
    Sunny - 2
    OverCast - 0
    Rainy - 1
          
          """)
    
    print("""
    Encoded Labels Temperature: 
    Hot - 1
    Mild -2
    Cool - 0
          """)
    
    print("""
    Encoded Labels for Play Column: 
    Yes -1 
    No - 0
    """)
  
    x = df[['Whether','Temperature']]
    y = df['Play']

    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.2 , random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    
    #step-3: Training Data
    model.fit(x_train , y_train)

    #step-4: Testing Data
    new_X = 0   #Overcast
    new_Y = 1   #Hot

    new_point = [(new_X,new_Y)]

    y_pred = model.predict(new_point)

    decode_predict = label_encoder.inverse_transform(y_pred)
    print("Predicts whether to Play: ",decode_predict)

    
def CheckAccuracy(datapath):

    df = pd.read_csv(datapath)

    label_encoder = LabelEncoder()

    df['Whether'] = label_encoder.fit_transform(df['Whether'])
    df['Temperature'] = label_encoder.fit_transform(df['Temperature'])

    df['Play'] = label_encoder.fit_transform(df['Play'])

    
    x = df[['Whether','Temperature']]
    y = df['Play']

    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.5 , random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    
    model.fit(x_train , y_train)

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_pred,y_test)

    print("Accuracy of the Model is: ",Accuracy*100 ,"%")

def main():

    DataFrame = "PlayPredictor.csv"
    KNNPlayPredictor(DataFrame)
    CheckAccuracy(DataFrame)


if __name__ == "__main__":
    main()