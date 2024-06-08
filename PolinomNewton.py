def newton_interpolation(x, x_data, y_data):
    n = len(x_data)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y_data
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i,j] = (divided_diff[i+1,j-1] - divided_diff[i,j-1]) / (x_data[i+j] - x_data[i])
    
    def P(x):
        total = divided_diff[0,0]
        product_terms = 1.0
        for i in range(1, n):
            product_terms *= (x - x_data[i-1])
            total += divided_diff[0,i] * product_terms
        return total
    
    return np.vectorize(P)(x)

# Menguji interpolasi Newton dan memplot hasilnya
y_newton = newton_interpolation(x_test, x_data, y_data)

plt.plot(x_data, y_data, 'o', label='Data Points')
plt.plot(x_test, y_newton, label='Newton Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()