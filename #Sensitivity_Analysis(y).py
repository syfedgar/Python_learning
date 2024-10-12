#Sensitivity_Analysis LCD color coordinate y

#  x,y, output follow normal distribution, and output = sqrt(A^2+B^2)

import numpy as np
import matplotlib.pyplot as plt

# 模型：输出结果为因子A和因子B的均方根关系
def model(A, B):
    return np.sqrt(A**2 + B**2)

# 因子A和因子B的正态分布参数
A_mean = 0.3305  # 因子A的均值
A_std = 0.0030  # 因子A的标准差
B_mean = 0.3310  # 因子B的均值
B_std = 0.0054  # 因子B的标准差

# 蒙特卡罗模拟参数
n_samples = 1000  # 样本数

# 根据正态分布生成因子A和因子B的样本
A_samples = np.random.normal(A_mean, A_std, n_samples)
B_samples = np.random.normal(B_mean, B_std, n_samples)

# 计算输出结果
outputs = model(A_samples, B_samples)

# 计算因子A和因子B的梯度，作为敏感性指标
A_sensitivity = np.gradient(outputs, A_samples)
B_sensitivity = np.gradient(outputs, B_samples)

# 计算因子A和因子B的均方根敏感性
A_sensitivity_rms = np.sqrt(np.mean(A_sensitivity**2))
B_sensitivity_rms = np.sqrt(np.mean(B_sensitivity**2))

# 计算各因子的百分占比
total_sensitivity = A_sensitivity_rms + B_sensitivity_rms
A_percent = (A_sensitivity_rms / total_sensitivity) * 100
B_percent = (B_sensitivity_rms / total_sensitivity) * 100

# 打印均方根敏感性结果和百分占比
print(f"RMS Sensitivity to Factor A: {A_sensitivity_rms:.4f} ({A_percent:.2f}%)")
print(f"RMS Sensitivity to Factor B: {B_sensitivity_rms:.4f} ({B_percent:.2f}%)")

# 可视化敏感性分析结果
plt.figure(figsize=(14, 6))

# 敏感性分布图
plt.subplot(1, 2, 1)
plt.scatter(A_samples, A_sensitivity, alpha=0.5, color='b')
plt.title(f'Sensitivity to Factor A\nRMS: {A_sensitivity_rms:.4f} ({A_percent:.2f}%)')
plt.xlabel('Factor A')
plt.ylabel('Sensitivity')

plt.subplot(1, 2, 2)
plt.scatter(B_samples, B_sensitivity, alpha=0.5, color='r')
plt.title(f'Sensitivity to Factor B\nRMS: {B_sensitivity_rms:.4f} ({B_percent:.2f}%)')
plt.xlabel('Factor B')
plt.ylabel('Sensitivity')

plt.tight_layout()

# 柱状图显示百分占比
plt.figure(figsize=(6, 6))
labels = ['Factor A', 'Factor B']
percentages = [A_percent, B_percent]

plt.bar(labels, percentages, color=['blue', 'red'])
plt.title('Percentage Contribution to Output Sensitivity')
plt.ylabel('Percentage (%)')

# 显示百分占比数值
for i, v in enumerate(percentages):
    plt.text(i, v + 1, f"{v:.2f}%", ha='center', fontsize=12)

plt.show()