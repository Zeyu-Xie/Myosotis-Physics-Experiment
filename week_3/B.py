import numpy as np
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 创建示例数组 p 和 w
theta = np.array([np.pi, 1.5*np.pi, 2*np.pi, 2.5*np.pi, 3*np.pi, 3.5*np.pi, 4*np.pi, 4.5*np.pi, 5*np.pi, 6*np.pi])
p= np.array([515.9, 438.9, 368.9, 290.9, 227.9, 182.9, 165.9, 115.9, 95.9, 66.9])

# 使用 Matplotlib 绘制散点图
plt.scatter(theta, p, color='blue', label='Data Points')

plt.xlim(0, max(theta) + 1)
plt.ylim(0, max(p) + 1)

# 使用最小二乘法拟合一条直线
coefficients = np.polyfit(theta, p, 1)
poly = np.poly1d(coefficients)

# 获取拟合直线的斜率和截距
slope, intercept = coefficients

# 打印直线的斜率和截距
# print(slope, intercept)

# 生成拟合直线的 x 和 y 坐标
fit_x = np.linspace(0, max(theta) + 1, 100)
fit_y = poly(fit_x)

# 绘制拟合直线
plt.plot(fit_x, fit_y, color='red', label=f"M_p={slope:.2f}\\theta+{intercept:.2f}")

# 添加标签和标题
plt.xlabel("\\theta")
plt.ylabel("M_p")
plt.title('Scatter Plot of Arrays \\theta and M_p')

# 显示图例
plt.legend()

plt.savefig(os.path.join(os.path.dirname(__file__), "B.png"))