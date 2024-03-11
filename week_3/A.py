import numpy as np
import os
import matplotlib.pyplot as plt

# 创建示例数组 p 和 w
w = np.array([100, 200, 300, 400, 500, 600, 700, 800])
p= np.array([56.9, 123.9, 184.9, 254.9, 302.9, 382.9, 429.9, 515.9])

# 使用 Matplotlib 绘制散点图
plt.scatter(w, p, color='blue', label='Data Points')

plt.xlim(0, max(w) + 1)
plt.ylim(0, max(p) + 1)

# 使用最小二乘法拟合一条直线
coefficients = np.polyfit(w, p, 1)
poly = np.poly1d(coefficients)

# 获取拟合直线的斜率和截距
slope, intercept = coefficients

# 打印直线的斜率和截距
# print(slope, intercept)

# 生成拟合直线的 x 和 y 坐标
fit_x = np.linspace(0, max(w) + 1, 100)
fit_y = poly(fit_x)

# 绘制拟合直线
plt.plot(fit_x, fit_y, color='red', label=f"M_p={slope:.2f}M_w+{intercept:.2f}")

# 添加标签和标题
plt.xlabel("M_w")
plt.ylabel("M_p")
plt.title('Scatter Plot of Arrays M_w and M_p')

# 显示图例
plt.legend()

plt.savefig(os.path.join(os.path.dirname(__file__), "A.png"))