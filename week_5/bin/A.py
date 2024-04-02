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

plt.title('Calculate \\zeta and \\Delta_\\zeta by the Least Squares Method')
plt.xlabel('j')
plt.ylabel('ln(\\theta_j)')

X = np.column_stack((np.ones(50), range(0, 50)))
y = np.array(ln_sheet1)

beta_hat = np.linalg.lstsq(X, y, rcond=None)[0]

y_fit = np.dot(X, beta_hat)
k = beta_hat[1]
b = beta_hat[0]
zeta = -k/math.sqrt(4*math.pi*math.pi+k*k)
print(f"k={k}, b={b}")
print(f"\\zeta={zeta}")

plt.plot(range(0, 50), y, '.', label='Data')
plt.plot(range(0, 50), y_fit, 'r-', label='Fitted Line')
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "A.png"))
