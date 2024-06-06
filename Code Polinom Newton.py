import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung koefisien polinom Newton
def newton_divided_difference(x, y):
  n = len(x)
  f = np.zeros((n, n))
  f[:, 0] = y

  # Menghitung koefisien polinom
  for j in range(1, n):
    for i in range(j, n):
      f[i, j] = (f[i, j-1] - f[i-1, j-1]) / (x[i] - x[i-j])

  return f

# Fungsi untuk mengevaluasi polinom Newton
def evaluate_newton_polynomial(x, x_data, f):
  n = len(x_data)
  result = f[0, 0]
  for i in range(1, n):
    product = 1
    for j in range(i):
      product *= (x - x_data[j])
    result += f[i, i] * product
  return result

# Menghitung koefisien polinom Newton
f = newton_divided_difference(x, y)

# Mendefinisikan rentang x untuk interpolasi
x_interp = np.linspace(5, 40, 100)

# Mengevaluasi polinom Newton untuk rentang x
y_interp = evaluate_newton_polynomial(x_interp, x, f)

# Plot hasil interpolasi
plt.plot(x, y, 'o', label='Data')
plt.plot(x_interp, y_interp, label='Interpolasi')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()

# Test Interpolasi
x_test = 17.5
y_test = evaluate_newton_polynomial(x_test, x, f)
print(f'Waktu patah untuk tegangan {x_test} kg/mm² adalah {y_test:.2f} jam.')