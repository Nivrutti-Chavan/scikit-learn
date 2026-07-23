from sklearn.linear_model import LogisticRegression
X=[[1],[2],[3],[4],[5]]
y=[0,0,1,1,1]

model=LogisticRegression()
model.fit(X,y)

Hours=float(input("Enter study of Hours="))

Result=model.predict([[Hours]])[0]
print(Result)
if Result==1:
    print(f"from your study of {Hours} Hours You may be likely to PASS")
else:
    print(f"from your study of {Hours} Hours You may be likely to FAIL")