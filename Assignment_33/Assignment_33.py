import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def DataPreprocessing(Datapath):

    df = pd.read_csv(Datapath,delimiter=";")

    print("Dataset Sample: ")
    print(df.head())

    print("Columns in the Dataset")
    print(df.columns)

    X = df[['G1','G2','G3','studytime','failures','absences']]

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    WCSS = []
    for k in range(1,10):
        model = KMeans(n_clusters=k ,init = 'k-means++',n_init=10,random_state=42)
        model.fit(x_scaled)
        print(model.inertia_)
        WCSS.append(model.inertia_)

    plt.plot(range(1,10),WCSS,marker='o')
    plt.xlabel("Number Of Clusters")
    plt.ylabel('WCSS')
    plt.title('Elbow Method')
    plt.show()

    model = KMeans(n_clusters=3,init='k-means++',n_init=10,random_state=42)
    y_means = model.predict(x_scaled)
    df['cluster'] = y_means

    print("Value of Y_means: ")
    print(y_means)

    Cluster_summary = df.groupby('Cluster').mean()
    print("Cluster Summary")


    sns.pairplot(x_scaled,hue='Cluster',vars=['G1','G2','G3','studytime','failures','absences'])
    plt.show()


    


    

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)








def main():

    dataset = "student-mat.csv"

    DataPreprocessing(dataset)

if __name__ == "__main__":
    main()