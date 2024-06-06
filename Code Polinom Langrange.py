import numpy as np
import matplotlib.pyplot as plt

# Data yang terbatas
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Interpolasi menggunakan metode polinom Langrange
def langrange_interpolation(xi, y, x_new):
    n = len(xi)
    y_new = 0
    for i in range(n):
        numerator = 1
        denominator = 1
        for j in range(n):
            if i != j:
                numerator *= (x_new - x[j])
                denominator *= (x[i] - x[j])
        y_new += y[i] * numerator / denominator
    return y_new

# Membuat kode testing
def test_interpolation():
    x_new = np.linspace(5, 40, 100)
    y_langrange = [langrange_interpolation(x, y, xi) for xi in x_new]
    plt.plot(x_new, y_langrange, label='Langrange Interpolation')
    plt.plot(x, y, 'o', label='Given Data')
    plt.xlabel('Tegangan, x (kg/mm²)')
    plt.ylabel('Waktu patah, y (jam)')
    plt.legend()
    plt.title('Langrange Interpolation')
    plt.grid(True)
    plt.show()

# Jalankan kode testing
test_interpolation()