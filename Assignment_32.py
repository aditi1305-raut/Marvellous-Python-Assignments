
from matplotlib import cm
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier

from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,precision_score,recall_score,f1_score

import seaborn as sns
import matplotlib.pyplot as plt

def DataPreprocessing():

    print("Dataset is Loaded Successfully..!! ")
    true_df = pd.read_csv("True.csv")
    fake_df = pd.read_csv("Fake.csv")

    
    true_df['label'] = 1
    fake_df['label'] = 0

    #Combining both datasets
    data = pd.concat([true_df,fake_df],ignore_index=True)

    data = data[['title','text','label']]

    data['combined Text'] = data['title'] + " "+data['text']
    
    print(data.head())
    #Drop Null Values

    data.dropna(inplace=True)

    X = data['combined Text']
    Y = data['label']

    #Converting Text to numerical features
    vectorizer = TfidfVectorizer(stop_words='english',max_df=0.7)
    x_vectors = vectorizer.fit_transform(X)

    print("shape of X and Y")
    print(x_vectors.shape)
    print(Y.shape)

    x_train , x_test , y_train , y_test = train_test_split(x_vectors,Y,test_size=0.2,random_state=42)

    log_clf = LogisticRegression()
    dt_clf = DecisionTreeClassifier(max_depth=10)

    voting_clf = VotingClassifier(
        estimators=[
            ('lr',log_clf),
            ('dt',dt_clf)
        ],
        voting='hard'
    )

    voting_clf.fit(x_train,y_train)

    y_pred = voting_clf.predict(x_test)

    Accuracy = accuracy_score(y_test , y_pred)
    print("Accuracy of the Model: ",Accuracy*100)

    conf_matrix = confusion_matrix(y_pred,y_test)
    print("Confusion Matrix for the Model: ")
    print(conf_matrix)

    print("Precison Score of the Model: ",precision_score(y_pred,y_test))

    print("Recall Score of the Model: ",recall_score(y_pred,y_test))

    print("F1 Score of the Model: ",f1_score(y_pred,y_test))

    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix,display_labels = [0,1])

    cm_display.plot()
    plt.show()

def main():

    DataPreprocessing()


if __name__ == "__main__":
    main()