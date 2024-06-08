# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Menguji interpolasi Lagrange dan memplot hasilnya
x_test = np.linspace(5, 40, 100)
y_lagrange = lagrange_interpolation(x_test, x_data, y_data)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_test, y_lagrange, label='Lagrange Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)

# Menguji interpolasi Newton dan memplot hasilnya
y_newton = newton_interpolation(x_test, x_data, y_data)

plt.subplot(1, 2, 2)
plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_test, y_newton, label='Newton Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)

plt.show()