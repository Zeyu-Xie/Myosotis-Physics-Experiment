import json
import os
import matplotlib.pyplot as plt
import numpy as np
import math

data = ""
with open(os.path.join(os.path.dirname(__file__), "original_data.json"), "r") as file:
    data = json.load(file)["exp1"]
    file.close()
description = data["description"]
sheet1 = data["sheet1"]["data"]
sheet2 = data["sheet2"]["data"]
ln_sheet1 = [0] * len(sheet1)
for i in range(len(sheet1)):
    sheet1[i] = sheet1[i]["magnitude"]
    ln_sheet1[i] = math.log(sheet1[i])
for i in range(len(sheet2)):
    sheet2[i] = sheet2[i]["period"]
X = np.column_stack((np.ones(50), range(0, 50)))
y = np.array(ln_sheet1)
beta_hat = np.linalg.lstsq(X, y, rcond=None)[0]
y_fit = np.dot(X, beta_hat)
b = beta_hat[1]
a = beta_hat[0]
zeta = -b/math.sqrt(4*math.pi*math.pi+b*b)
td = sum(sheet2)/50
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

plt.title('Calculate ζ and Δζ by the Least Squares Method')
plt.xlabel('j')
plt.ylabel('ln(θⱼ)')
plt.plot(range(0, 50), y, '.', label='Data')
plt.plot(range(0, 50), y_fit, 'r-', label='Fitted Line')
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "A.png"))
