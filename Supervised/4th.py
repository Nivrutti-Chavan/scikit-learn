from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
x=[
#[size,color_shade]    
    [7,2],
    [8,3],
    [9,8],
    [10,9]
]
y=[0,0,1,1]

model.fit(x,y)    
size=float(input("enter the fruit size in cm:"))
shade=float(input("enter color shade range(1-10):"))

result=model.predict([[size,shade]])[0]

if result==0:
    print("this fruit is likely be appple")
else:
    print("this fruit is likely be orange")