import numpy as np
import matplotlib.pyplot as plt

# 生成正弦波的数据
x = np.linspace(0, 2*np.pi, 100)  # 在0到2π之间生成100个点
y = np.sin(x)  # 计算对应点的正弦值

# 绘制正弦波
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.savefig('正弦波.png')
plt.close()

# 生成三角波的数据
x = np.linspace(0, 4*np.pi, 100)  # 在0到4π之间生成100个点
y = np.abs((2*np.pi*x - np.pi) % (4*np.pi) - 2*np.pi) - np.pi  # 计算对应点的三角波值

# 绘制三角波
plt.plot(x, y)
plt.title('Triangle Wave')
plt.xlabel('x')
plt.ylabel('Triangle Wave')
plt.grid(True)
plt.savefig('三角波.png')
plt.close()

# 生成方波的数据
x = np.linspace(0, 4*np.pi, 100)  # 在0到4π之间生成100个点
y = np.sign(np.sin(x))  # 计算对应点的方波值

# 绘制方波
plt.plot(x, y)
plt.title('Square Wave')
plt.xlabel('x')
plt.ylabel('Square Wave')
plt.grid(True)
plt.savefig('方波.png')
plt.close()

# 生成脉冲波的数据
x = np.linspace(0, 4*np.pi, 100)  # 在0到4π之间生成100个点
y = np.zeros(100)  # 初始化y为全0

# 将y的第0、25、50、75个点设为1
y[0] = 1
y[25] = 1
y[50] = 1
y[75] = 1

# 绘制脉冲波
plt.plot(x, y)
plt.title('Impulse Wave')
plt.xlabel('x')
plt.ylabel('Impulse Wave')
plt.grid(True)
plt.savefig('脉冲波.png')
plt.close()