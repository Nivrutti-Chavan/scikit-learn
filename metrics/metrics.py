from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score

y_true=[1,0,1,1,0,1,0]
y_predict=[1,0,1,0,0,1,1]

print("accuracy",accuracy_score(y_true,y_predict))
print("accuracy",precision_score(y_true,y_predict))
print("accuracy",recall_score(y_true,y_predict))
print("accuracy",f1_score(y_true,y_predict))
