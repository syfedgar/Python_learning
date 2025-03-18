# Classification  model training

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

#数据预处理
df = pd.read_csv('datafor5th.csv')
#数据清洗
df = df.loc[:,"Air temperature [K]":"Machine failure"]
#将String转成Float
#errors='coerce'表示如果有非数值的数据，转换为NaN（Not a Number)
for col in df.columns:
    df[col] = pd.to_numeric(df[col],errors='coerce')

#删除空值
df = df.dropna()

x = df.loc[:,'Air temperature [K]':'Tool wear [min]']
y = df.loc[:,'Machine failure']
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True)

def train():
    model = SVC(kernel='linear')
    model.fit(X_train,y_train)
    return model

def test(model):
    y_pred = model.predict(X_test)
    return y_pred

model = train()
test(model)
print(classification_report(y_test,test(model)))