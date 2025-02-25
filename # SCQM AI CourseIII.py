from PIL import Image
import numpy as np

# 读取图片（替换为你的图片路径）
image = Image.open('Happylife.jpg')  # 确保图片路径正确

# 将图片转换为numpy数组
img_array = np.array(image)

# 打印数组形状
print("数组形状:", img_array.shape)

# 打印数组内容
print("数组内容:")
print(img_array)