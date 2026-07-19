#By one-hot-encoding method
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.read_csv("sample_data.csv")

encoder = OneHotEncoder(sparse_output=False)#

encoded = encoder.fit_transform(df[["Gender"]])

print(encoded)
#_________________________________________________________________________
#by get dummies
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df=pd.read_csv("sample_data.csv")
df_label=df.copy()

le=LabelEncoder()
df_label["Gender_Encoded"]=le.fit_transform(df_label["Gender"])
df_label["passed_encoded"]=le.fit_transform(df_label["Passed"])

df_encoded=pd.get_dummies(df_label,columns=["City"],dtype=int)
print(df_encoded)