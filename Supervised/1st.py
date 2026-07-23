from sklearn.linear_model import LinearRegression

model=LinearRegression()
X=[[1],[2],[3],[4],[5]]
y=[40,50,55,70,85]

model.fit(X,y)
Hours=float(input("enter how many hours you study="))

predict_marks=model.predict([[Hours]])
print(f"If you study {Hours} hours, your predicted marks are {predict_marks}")