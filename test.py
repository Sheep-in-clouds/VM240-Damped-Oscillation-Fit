import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def damped_oscillation(t, A, B, mu, lam, Y):
    return np.e ** (lam * t) * ((A * np.sin(mu * t)) + (B * np.cos(mu * t))) + Y

def read_data(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    t_data, x_data = [], []
    for line in lines:
        t, x = map(float, line.split())
        t_data.append(t)
        x_data.append(x)
    return np.array(t_data), np.array(x_data)
bounds =  ([-np.inf, -np.inf, 0, -np.inf, -np.inf], [np.inf, np.inf, np.inf, np.inf, np.inf])

def fit_data(t_data, x_data):
    params, _ = curve_fit(damped_oscillation, t_data[1500: 3500], x_data[1500: 3500], p0=[1, 1, 2*np.pi, 0.05, 0], maxfev=50000)
    return params

def main():
    filepath = 'test1.txt'
    
    t_data, x_data = read_data(filepath)
    params = fit_data(t_data, x_data)
    
    print(f"A={params[0]}, B={params[1]}, mu={params[2]}, lam={params[3]}, , y={params[4]}")
    
    plt.scatter(t_data, x_data, label='原始数据')
    plt.plot(t_data, damped_oscillation(t_data, *params), label='拟合曲线')
    plt.legend()
    plt.xlabel('时间')
    plt.ylabel('位移')
    plt.title('阻尼振荡拟合')
    plt.show()

if __name__ == "__main__":
    main()
