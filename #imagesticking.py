import numpy as np
import matplotlib.pyplot as plt

# 定义显示屏亮度范围
display_brightness = np.linspace(0, 400, 81)

# 根据公式计算 CIE Lab 亮度(L)
cie_lab_l = 116 * (display_brightness/400)**(1/3) - 16

# 绘制曲线
plt.figure(figsize=(8, 6))
plt.plot(display_brightness, cie_lab_l)
plt.xlabel('Displayed Brightness (Ld in nits)')
plt.ylabel('CIE Lab Lightness (L)')
plt.title('Displayed Brightness vs CIE Lab Lightness (L) Curve (400 nits, x=0.313, y=0.329)')
plt.grid(True)
plt.show()
