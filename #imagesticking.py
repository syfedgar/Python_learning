import numpy as np
import matplotlib.pyplot as plt

# 定义显示屏亮度范围
display_brightness = np.linspace(0, 400, 81)

# 根据公式计算 CIE Lab 亮度(L)
cie_lab_l = 116 * (display_brightness/400)**(1/3) - 16

# 计算δL= display_brightness- cie_lab_l
δL = display_brightness - cie_lab_l

# 计算δL% = (display_brightness- cie_lab_l) / display_brightness
δLper = (display_brightness - cie_lab_l) / display_brightness


# 绘制曲线1: display_brightness VS CIE_lab_L
plt.figure(figsize=(8, 6))
plt.plot(display_brightness, cie_lab_l)
plt.xlabel('Displayed Brightness (Ld in nits)')
plt.ylabel('CIE Lab Lightness (L)')
plt.title('Displayed Brightness vs CIE Lab Lightness (L) Curve (400 nits, x=0.313, y=0.329)')
plt.grid(True)
plt.show()


# 绘制曲线2: display_brightness VS δL
plt.figure(figsize=(8, 6))
plt.plot(display_brightness, δL)
plt.xlabel('Displayed Brightness (Ld in nits)')
plt.ylabel('δL (δL)')
plt.title('Displayed Brightness vs δL (δL) Curve (400 nits, x=0.313, y=0.329)')
plt.grid(True)
plt.show()


# 绘制曲线3: display_brightness VS δLper
plt.figure(figsize=(8, 6))
plt.plot(display_brightness, δLper)
plt.xlabel('Displayed Brightness (Ld in nits)')
plt.ylabel('δLper')
plt.title('Displayed Brightness vs δLper Curve (400 nits, x=0.313, y=0.329)')
plt.grid(True)
plt.show()