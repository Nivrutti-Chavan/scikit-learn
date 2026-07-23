import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
import seaborn as sns

data={
    "Study_hours":[1,2,3,4,5],
    "Test_Score":[40,50,60,70,80]
}

df=pd.DataFrame(data)
#print(df)

Standard_scaler=StandardScaler()
Standard_scaled=Standard_scaler.fit_transform(df)

minmax_scaler=MinMaxScaler()
minmax_scaled=minmax_scaler.fit_transform(df)

print("\n output of standard_scaled")
print(pd.DataFrame(Standard_scaled,columns=[["Study_hours","Test_Score"]]))

print("\n output of Minmax_scaled")
print(pd.DataFrame(minmax_scaled,columns=[["Study_hours","Test_Score"]]))

X=df[["Study_hours"]]#input(X)
y=df[["Test_Score"]]#output(y)

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("training data of x ")
print(x_train)

print("testing data X")
print(x_test)

print("training data of y ")
print(y_train)

print("testing data y")
print(y_test)