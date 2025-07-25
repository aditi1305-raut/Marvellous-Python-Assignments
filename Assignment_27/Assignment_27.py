'''
According the given Dataset :
   
     -Build a ML model using Linear Regression
     - Predict the sales based on the advertisement.
     -Compare the predicted sales with actual sales Value from
      the dataset. 
'''

import pandas as pd
from  sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def LinearRegSalesPrediction(Datapath):

    #Step-1 : Get The Data
    df = pd.read_csv(Datapath)
    print("Dataset Loaded Successfully!!")
   # print(df)

    #step -2 
    print(df.head())

    print("Data after Cleaning")
    df.drop(columns=['Unnamed: 0'],axis=1,inplace=True)
    print(df.head())

    x = df[['TV','radio','newspaper']]
    y = df['sales']

    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.5,random_state=42)

    model = LinearRegression()

    model.fit(x_train,y_train)

    #Add Your input Points
    # new_X1 = 151.5
    # new_X2 = 41.3
    # new_X3 = 58.4

    # new_point = [(new_X1,new_X2,new_X3)]

    #y_pred = model.predict(new_point)
    y_pred = model.predict(x_test)

    print("Comparison between Actual Values and Predicted Values ")
    c = pd.DataFrame({"Actual":y_test,"Predictions":y_pred})
    print(c)


def main():
    LinearRegSalesPrediction("Advertising.csv")


if __name__ == "__main__":
    main()