# -*- coding:gbk -*-
# print("����˭��Who're you?")

# print("Hello, World!")
# print("Goodbye, World!")
# print("\nGoodbye, World!\n1\n2")
 
import numpy as np  
from scipy.optimize import fsolve  
  
def func(x):  
    return x * np.sin(np.arctan(x / 0.35)) - 0.017  
  
# 初始猜测值  
x0 = 0.1  # 注意：这个初始猜测值可能需要根据你的具体情况进行调整  
  
# 求解方程  
solution = fsolve(func, x0)  
  
print("解为:", solution)

