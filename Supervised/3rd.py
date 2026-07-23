import os
os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")#Defult setting 

from sklearn.neighbors import KNeighborsClassifier
X=[
    [180,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]
y=[0,0,0,1,1,1]
model=KNeighborsClassifier(n_neighbors=5)

model.fit(X,y)
weight=float(input("enter weight of fruits in gm:"))
height=float(input("enter height of fruits in cm:"))
predict=model.predict([[weight,height]])[0]
print(predict)