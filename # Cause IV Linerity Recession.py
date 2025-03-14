# Cause IV Linerity Recession 

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score

df = pd.read_csv("./train.csv")

# print(df.head())

x = df.loc[:,"CRIM":"LSTAT"]
y = df.loc[:,"MEDV"]

def draw_picture():
    plt.scatter(x.loc[:,"LSTAT"],y)
    plt.show()

def train():
    #构建线性模型
    model = linear_model.linerRegression()
    model.fit(x,y)
    #斜率 & 截距
    print("模型的截距b:")
    print(model.intercept)
    print("模型的系数w:)")
    print(model.coef)
    return model

def test(model):
    #预测
    test_df = pd.read_csv("./test.vsv")
    test_x = test_df.loc[:,"CRIM":"LSTAT"]
    test_y = test_predict(test_x)
    print(test_y)




