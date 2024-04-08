import matplotlib.pyplot as plt
import numpy as np

y = [0.00, 8.99, 17.93, 26.86, 35.03, 43.83, 53.06, 61.59, 70.52, 79.01, 86.93]
x = range(len(y))

v = 331.5 * np.sqrt(1 + 25.6/273.15) * np.sqrt(1 + 0.31 * (29.9e-2 * 0.0317e5) / 1.013e5 )
x_mean = np.mean(x)
y_mean = np.mean(y)
uncertain_degree = np.sqrt((np.sum((y-y_mean)**2))/(np.sum((x-x_mean)**2))/(len(y)-2))
coefficients = np.polyfit(x, y, 1)
a = coefficients[1]
b = coefficients[0]
speed = b*1e-3*4e4
per = (speed/v-1)*100

poly_function = np.poly1d(coefficients)
plt.plot(x, y, 'o', label="Original Data")
plt.plot(x, poly_function(x), label="Fitted Curve")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Fitting Curve")
plt.savefig("plot.png")

print(f"理论声速：{v} m/s")
print(f"拟合结果：y = {a} + {b}x")
print(f"斜率不确定度：{uncertain_degree}")
print(f"速度：{speed} m/s")
print(f"速度不确定度：{uncertain_degree*4e4*1e-3} m/s")
print(f"相对偏差：{per}%")