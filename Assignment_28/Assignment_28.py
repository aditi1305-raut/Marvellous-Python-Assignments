import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 

import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt

def PredictWineClass(Datapath):

    df = pd.read_csv(Datapath)
    print(df)

    df.dropna(inplace=True)
    #df.drop(columns=[['']])

    print(df.head())
    print("Shape of the Dataset: ",df.shape)

    print("Statical Information about Dataset: ")
    print(df.describe())
   
    df.drop(columns=['Malic acid','Ash','Alcalinity of ash','Magnesium','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue'],axis=1,inplace=True)
    print("After Deleting Columns: ")
    print(df.head())

    #x = df.drop(columns= ['Class'])
    x = df[['Flavanoids','OD280/OD315 of diluted wines','Total phenols','Proline','Alcohol']]
    y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train , x_test , y_train ,y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_pred,y_test)

    print("Accuracy of the Model: ",accuracy*100)

    #Visual Representation of Heatmap
    corr = df.corr()
    plt.figure(figsize=(14,12))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm',  square=True, linewidths=0.5)
    plt.xticks()
    plt.yticks()
    plt.title('Full Heatmap Including Class Correlations')
    plt.show()
    
def main():

    PredictWineClass("WinePredictor.csv")

if __name__ == "__main__":
    main()