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


def main():
    
    df = pd.read_csv("diabetes.csv")
    #Standardizing the Dataset:

    X = df.drop('Outcome',axis=1)
    Y = df['Outcome']

    scaler = StandardScaler()
    
    x_scaled = scaler.fit_transform(X)

    x_train , x_test , y_train , y_test = train_test_split(x_scaled,Y,test_size=0.2,random_state=42)

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

    model = KNeighborsClassifier(n_neighbors= best_k)
    model.fit(x_train , y_train)
    y_pred = model.predict(x_test)
    Accuracy = accuracy_score(y_test , y_pred)

    print("Final Best Accuracy is : ",Accuracy*100)
    
    
    
    # model = KNeighborsClassifier()
    # model.fit(x_train,y_train)

    # y_pred = model.predict(x_test)

    # Accuracy = accuracy_score(y_test,y_pred)
    # print("Accuracy of The KNeighbors Classifier model: ",Accuracy*100)

    



if __name__ == "__main__":
    main()