# Caculuting the difference between CIE1931 and CIELab 

import numpy as np
import matplotlib.pyplot as plt

def xy_to_xyz(x, y, L):
    """将CIE1931色坐标(x, y)和亮度L转换为XYZ颜色空间"""
    Y = L
    X = (Y / y) * x
    Z = (Y / y) * (1 - x - y)
    return X, Y, Z

def xyz_to_lab(X, Y, Z):
    """将XYZ颜色空间转换为CIELab颜色空间"""
    # 定义参考白点 (D65)
    Xn = 95.047
    Yn = 100.0
    Zn = 108.883
    
    # 计算f(X/Xn), f(Y/Yn), f(Z/Zn)
    def f(t):
        if t > (6/29)**3:
            return t**(1/3)
        else:
            return (1/3) * (29/6)**2 * t + 4/29
    
    L_star = 116 * f(Y/Yn) - 16
    a_star = 500 * (f(X/Xn) - f(Y/Yn))
    b_star = 200 * (f(Y/Yn) - f(Z/Zn))
    
    return L_star, a_star, b_star

def delta_L(L1, L0):
    """计算δL = L1 - L0"""
    return L1 - L0

def delta_L_star(L1_star, L0_star):
    """计算δL* = L1* - L0*"""
    return L1_star - L0_star

def delta_delta_L(delta_L, delta_L_star):
    """计算δδL = δL - δL*"""
    return delta_L - delta_L_star

def calculate_deltas(x0, y0, L0, x1, y1, L1):
    """计算δL, δL*, δδL"""
    # 计算初始点的XYZ和L*
    X0, Y0, Z0 = xy_to_xyz(x0, y0, L0)
    L0_star, _, _ = xyz_to_lab(X0, Y0, Z0)

    # 计算待测点的XYZ和L*
    X1, Y1, Z1 = xy_to_xyz(x1, y1, L1)
    L1_star, _, _ = xyz_to_lab(X1, Y1, Z1)

    # 计算δL, δL*和δδL
    delta_L_value = delta_L(L1, L0)
    delta_L_star_value = delta_L_star(L1_star, L0_star)
    delta_delta_L_value = delta_delta_L(delta_L_value, delta_L_star_value)

    return delta_L_value, delta_L_star_value, delta_delta_L_value, L1_star

# 获取用户输入
x0 = float(input("请输入初始点的x坐标 (x0): "))
y0 = float(input("请输入初始点的y坐标 (y0): "))
L0 = float(input("请输入初始点的亮度 (L0) [nits]: "))

x1 = float(input("请输入待测点的x坐标 (x1): "))
y1 = float(input("请输入待测点的y坐标 (y1): "))

# 设置亮度范围
L1_range = np.linspace(300, 500, 100)

# 计算δL, δL*和δδL随亮度变化的曲线
delta_L_values = []
delta_L_star_values = []
delta_delta_L_values = []
L1_star_values = []

for L1 in L1_range:
    dL, dL_star, ddL, L1_star = calculate_deltas(x0, y0, L0, x1, y1, L1)
    delta_L_values.append(dL)
    delta_L_star_values.append(dL_star)
    delta_delta_L_values.append(ddL)
    L1_star_values.append(L1_star)

# 绘制曲线
plt.figure(figsize=(18, 6))

# δδL vs δL
plt.subplot(1, 3, 1)
plt.plot(delta_L_values, delta_delta_L_values, label='δδL vs δL')
plt.xlabel('δL')
plt.ylabel('δδL')
plt.title('δδL vs δL')
plt.legend()

# δδL vs δL*
plt.subplot(1, 3, 2)
plt.plot(delta_L_star_values, delta_delta_L_values, label='δδL vs δL*')
plt.xlabel('δL*')
plt.ylabel('δδL')
plt.title('δδL vs δL*')
plt.legend()

# δδL vs L*
plt.subplot(1, 3, 3)
plt.plot(L1_star_values, delta_delta_L_values, label='δδL vs L*')
plt.xlabel('L*')
plt.ylabel('δδL')
plt.title('δδL vs L*')
plt.legend()

plt.tight_layout()
plt.show()
