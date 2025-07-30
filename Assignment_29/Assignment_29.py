
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix,precision_score,recall_score,f1_score,ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

import joblib      ##Saving the trained Model

def DataPreprocessing(Datapath):
    print("Dataset is Loaded Successfully !!")
    
    Border = "*"*80
    print(Border)
    df = pd.read_csv(Datapath)
    #print(df)

    print(df.head())

    print(Border)
    print("Columns in Dataframe: ",df.columns)

    #print("Number of Null Values: ",df.isnull.sum())

    print(Border)
    print("Stastical Information about Dataset: ")
    print(df.describe())

    print(Border)
    
    plt.hist(df, edgecolor='black')     #Plotting of histogram
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Histogram for the dataset')
    plt.show()

    plt.boxplot(df)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Boxplot for the dataset')
    plt.show()

    #Data Preprocessing

    #Replacing the zero Values with NaN in Blood Pressure,skin thickness , Insulin
    print("After Replacing the Zero Values:  ")
    for values in ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']:
        df[values]=df[values].replace(0,np.nan)

        mean_value = df[values].mean()

        df[values] = df[values].fillna(mean_value)
    print(df.head(10))
    print(Border)

    #Standardizing the inputs 
    #Standardizing the Dataset:
    X = df.drop('Outcome',axis=1)
    Y = df['Outcome']

    scaler = StandardScaler()
    
    x_scaled = scaler.fit_transform(X)

    return x_scaled ,Y,scaler


def LogisticTraining(X,Y):
    
    print("Using Logistic Regression Algorithm ")
    Border = "*"*80
    print(Border)
#df = pd.read_csv(Datapath)
    
    x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = LogisticRegression()

    model.fit(x_train,y_train)

    #Saving the trained Model
    joblib.dump(model,'logistic_model.pkl')
    print("saved Logistic_model.pkl")

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy of The model: ",Accuracy*100)

    conf_matrix = confusion_matrix( y_test,y_pred)
    print("Confusion Matrix for the Data: ")
    print(conf_matrix)

    precision = precision_score(y_test,y_pred)
    print("Precision of model: ",precision)

    recall = recall_score(y_test , y_pred)
    print("Recall for the Model: ",recall)

    f1 = f1_score(y_test,y_pred)
    print("F1 Score for Model: ",f1)

    #Visualizing the Confusion Matrix
    print("Visualization of the Confusion Matrix for the Logistic Regression")
    disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix,display_labels=[0,1])
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix for the Logistic Regression")
    #plt.show()


def KNNTraining(X,Y):

    Border = "*"*80
    print(Border)

    print("Using K-Nearest Neighbors Algorithm")
    print(Border)
    
    x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    acc_scores= []
    k_range = range(1,25)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train , y_train)
        y_pred = model.predict(x_test)
        Accuracy = accuracy_score(y_test , y_pred)
        acc_scores.append(Accuracy)

    plt.figure(figsize=(8,5))
    plt.plot(k_range,acc_scores,marker='o',linestyle='--')
    plt.title("Accuracy vs K value")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy of Model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()    

    best_k = k_range[acc_scores.index(max(acc_scores))]
    print("Best accuracy score is: ",best_k)

    print(Border)
    model = KNeighborsClassifier(n_neighbors= best_k)
    model.fit(x_train , y_train)

    joblib.dump(model, 'knn_model.pkl')
    print("Saved knn_model.pkl")
    
    y_pred = model.predict(x_test)
    Accuracy = accuracy_score(y_test , y_pred)
      
    print("Final Best Accuracy is : ",Accuracy*100)
    
    conf_matrix = confusion_matrix( y_test,y_pred)
    print("Confusion Matrix for the Data: ")
    print(conf_matrix)

    precision = precision_score(y_test,y_pred)
    print("Precision of model: ",precision)

    recall = recall_score(y_test , y_pred)
    print("Recall for the Model: ",recall)

    f1 = f1_score(y_test,y_pred)
    print("F1 Score for Model: ",f1)
    
    #Visualizing the Confusion Matrix
    print("Visualization of the Confusion Matrix for KNN")
    disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix,display_labels=[0,1])
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix for KNN")
    #plt.show()
    print(Border)

    return best_k

def PredictDiabetes(scaler):
    
    print("Enter Patient Details: ")
    features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    input_data = []

    for feature in features:
        while True:
            value = input(f"{feature}:")
            try:
                value = float(value)
                input_data.append(value)
                break 
                
            except ValueError:
                print("Please enter the valid numeric data ")
                
    #convert input data to Numpy array and reshape
    input_array = np.array(input_data).reshape(1,-1)

    #Preprocess input data using the same scaler
    input_scaled = scaler.transform(input_array)

    #Load the trained model 
    model = joblib.load('knn_model.pkl')

    prediction = model.predict(input_scaled)

    if prediction[0]==1:
        print("The Patient is Predicted to be: Diabetic")

    else:
        print("Patient is Predicted to be: Non-Diabetic")


def main():

    #Dataset = "diabetes.csv"
    
    X,y,scaler = DataPreprocessing("diabetes.csv")
    
    LogisticTraining(X,y)
    K = KNNTraining(X,y)

    info_list = []
    PredictDiabetes(scaler)

if __name__ =="__main__":
    main()