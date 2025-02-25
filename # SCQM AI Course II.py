# SCQM AI Course II 2nd homework

import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel("第二课.xlsx")

# 使用loc+条件查询筛选数据
condition = df["Part MM"] > 100  # 创建筛选条件
filtered_df = df.loc[condition]  # 应用loc筛选

# 绘制散点图（假设用'Part MM'和另一个数值列，这里示例为'Value'，请根据实际列名修改）
plt.figure(figsize=(10, 6))
plt.scatter(
    x=filtered_df["Part MM"],
    y=filtered_df["Part Supplier"],  # 修改为你的Y轴列名
    c='blue',
    alpha=0.7
)

# 添加图表元素
plt.title("Part MM > 100 数据散点图")
plt.xlabel("Part MM")
plt.ylabel("Part Supplier")  # 修改为你的Y轴标签
plt.grid(True)
plt.show()
