import math

def f(N, L, T, rho):
    return N/(2*L)*math.sqrt(T/rho)



def main_1():
    T_list = [0.00055, 0.00098, 0.00191, 0.00350, 0.00578, 0.00936]
    for i in T_list:
        print(f"\\rho = {i}")
        for j in range(1, 7):
            f1 = f(1, 0.5, j*1.96, i)
            print(f"T = {j*1.96} kg, f = {f1} Hz")
        print

def main_2():
    N = float(input("N: "))
    L = float(input("L(m): "))
    T = float(input("T(N): "))
    rho = float(input("rho(kg/m): "))
    g = 9.8
    f1 = f(N, L, T, rho)
    print(f"f = {f1} Hz")

def main_3():
    T_list = [0.00055, 0.00098, 0.00191, 0.00350, 0.00578, 0.00936]
    for i in T_list:
        # f1 = f(1, 0.5, 9.8, i)
        print(f"理论 v = {math.sqrt(9.8/i)} m/s")

if __name__ == "__main__":
    main_3()