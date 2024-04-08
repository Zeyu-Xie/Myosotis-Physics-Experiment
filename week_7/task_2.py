import matplotlib.pyplot as plt
import numpy as np

# Part 1 - Calculate the speed of voice in the air

# The equation you've provided appears to be the formula for the speed of sound (
# v
# v) in a gas. Here's a breakdown of the terms:

# v
# v is the speed of sound.
# γ
# γ (gamma) is the adiabatic index or the ratio of specific heats (
# C
# p
# /
# C
# v
# C 
# p
# ​	
#  /C 
# v
# ​	
#  ).
# R
# R is the specific gas constant for the particular gas.
# T
# T is the temperature of the gas in Kelvin.
# μ
# μ (mu) is the molecular mass of the gas.
# The formula expresses that the speed of sound in a gas is determined by the square root of the ratio of the product of the adiabatic index, the gas constant, and the temperature of the gas to the molecular mass of the gas.

# Is there anything specific you would like to know or discuss about this equation?

gamma = 1.4  # adiabatic index
R = 8.31441
T = 273.15  + 25.6
mu = 29e-3  # molecular mass of air in kg/mol

v = (gamma * R * T / mu) ** 0.5

print("Speed of sound in air:", v)

# Part 2

# Part 3

y = [0.00, 8.99, 17.93, 26.86, 35.03, 43.83, 53.06, 61.59, 70.52, 79.01, 86.93]
x = range(len(y))

# 使用最小二乘法拟合
degree = 1  # 多项式的次数
coefficients = np.polyfit(x, y, degree)

# 创建拟合的多项式函数
poly_function = np.poly1d(coefficients)

# 绘制原始数据和拟合曲线
plt.plot(x, y, 'o', label="Original Data")
plt.plot(x, poly_function(x), label="Fitted Curve")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Fitting Curve")
plt.savefig("plot.png")

print("Parameters", coefficients)
