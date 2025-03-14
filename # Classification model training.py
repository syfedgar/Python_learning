# Classification  model training

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

# 数据加载（假设数据格式）
df = pd.read_csv("datafor5th.csv")

# 特征预处理
features = [
    'Air temperature [K]', 
    'Process temperature [K]',
    'Rotational speed [rpm]', 
    'Torque [Nm]',
    'Tool wear [min]'
]

# 创建复合标签（六分类）
df['fault_label'] = df.apply(lambda x: 
    'Normal' if x['Machine failure'] == 1 else
    'AirTemp' if x['Air temperature [K]'] > 310 else
    'ProcessTemp' if x['Process temperature [K]'] > 315 else
    'RpmFault' if x['Rotational speed [rpm]'] < 1500 or x['Rotational speed [rpm]'] > 2500 else
    'TorqueFault' if x['Torque [Nm]'] < 30 or x['Torque [Nm]'] > 50 else
    'ToolWear' if x['Tool wear [min]'] > 200 else 'Unknown',
    axis=1
)

# 标签编码
le = LabelEncoder()
df['encoded_label'] = le.fit_transform(df['fault_label'])

# 数据分割
X = df[features]
y = df['encoded_label']

# 处理类别不平衡
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.2, stratify=y_res, random_state=42
)

# 构建模型管道
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(
        class_weight='balanced',
        random_state=42,
        n_jobs=-1
    ))
])

# 超参数调优
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10],
    'classifier__min_samples_split': [2, 5]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1_weighted')
grid_search.fit(X_train, y_train)

# 模型评估
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("最佳参数:", grid_search.best_params_)
print("\n分类报告:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# 可视化混淆矩阵
fig, ax = plt.subplots(figsize=(10,8))
ConfusionMatrixDisplay.from_estimator(
    best_model, X_test, y_test,
    display_labels=le.classes_,
    cmap='Blues', ax=ax
)
plt.xticks(rotation=45)
plt.title("Confusion Matrix")
plt.savefig('confusion_matrix.png', bbox_inches='tight')