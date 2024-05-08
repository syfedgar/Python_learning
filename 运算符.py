print(9//2)

# 优先级，先加减乘除，再进行比较，最后逻辑运算符(not, and, or)
# 记不清楚上括号

import matplotlib.pyplot as plt
import numpy as np

# 定义转换函数
def convert_to_L1(L0):
    if L0 <= 0.008856:
        return 100 * L0**(1/2.4)
    else:
        return 100 * L0**(1/2.4)

# 生成一系列的L0值
L0_values = np.linspace(0, 1, 100)

# 计算对应的L1值
L1_values = [convert_to_L1(L0) for L0 in L0_values]

# 绘制曲线图
plt.figure()
plt.plot(L0_values, L1_values, label='L1 vs. L0')
plt.xlabel('亮度因子 L0')
plt.ylabel('显示屏亮度 L1')
plt.title('显示屏亮度 L1 与亮度因子 L0 的关系')
plt.legend()
plt.grid(True)
plt.show()