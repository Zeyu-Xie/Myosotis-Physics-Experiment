import json
import os
import matplotlib.pyplot as plt
import numpy as np
import math

data = ""
with open(os.path.join(os.path.dirname(__file__), "original_data.json"), "r") as file:
    data = json.load(file)["exp2"]
    file.close()
description = data["description"]
sheet1 = data["sheet1"]["data"]
sheet1_1 = [0] * len(sheet1)
sheet1_2 = [0] * len(sheet1)
sheet2 = data["sheet2"]["data"]
ln_sheet1_1 = [0] * len(sheet1)
for i in range(len(sheet1)):
    sheet1_1[i] = sheet1[i]["magnitude"]
    sheet1_2[i] = sheet1[i]["period"]
    ln_sheet1_1[i] = math.log(sheet1_1[i])

X = np.column_stack((np.ones(12), range(0, 12)))
y = np.array(ln_sheet1_1)
beta_hat = np.linalg.lstsq(X, y, rcond=None)[0]
y_fit = np.dot(X, beta_hat)
b = beta_hat[1]
a = beta_hat[0]
zeta = -b/math.sqrt(4*math.pi*math.pi+b*b)
td = sum(sheet1_2)/12
omega_0 = 2*math.pi/(td*math.sqrt(1-zeta*zeta))
beta = zeta * omega_0
tau = 1 / beta

print("y = a + bx")
print(f"a={a}, b={b}")
print(f"\\zeta={zeta}")
print(f"td={td}")
print(f"\\omega_0={omega_0}")
print(f"\\beta={beta}")
print(f"\\tau={tau}")

plt.title('Calculate \\zeta and \\Delta_\\zeta by the Least Squares Method')
plt.xlabel('j')
plt.ylabel('ln(\\theta_j)')
plt.plot(range(0, 12), y, '.', label='Data')
plt.plot(range(0, 12), y_fit, 'r-', label='Fitted Line')
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "B.png"))
