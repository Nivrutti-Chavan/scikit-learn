#label encoding

from sklearn.preprocessing import LabelEncoder
import pandas as pd

df=pd.read_csv("scikit-learn/sample_data.csv")
df_label=df.copy()

le=LabelEncoder()
df_label["Gender_Encoded"]=le.fit_transform(df_label["Gender"])
df_label["passed_encoded"]=le.fit_transform(df_label["Passed"])

print(df_label[["Name","Gender","Gender_Encoded","City","Passed","passed_encoded"]])