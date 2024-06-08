import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(x, x_data, y_data):
    def L(k, x):
        term = [(x - x_data[i]) / (x_data[k] - x_data[i]) for i in range(len(x_data)) if i != k]
        return np.prod(term, axis=0)
    
    return sum(y_data[k] * L(k, x) for k in range(len(x_data)))

# Menguji interpolasi Lagrange dan memplot hasilnya
x_test = np.linspace(5, 40, 100)
y_lagrange = lagrange_interpolation(x_test, x_data, y_data)

plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_test, y_lagrange, label='Lagrange Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()