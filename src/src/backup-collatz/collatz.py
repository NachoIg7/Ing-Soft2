import matplotlib.pyplot as plt

# Función que calcula el número de iteraciones de la secuencia de Collatz
def collatz_iterations(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:  # Si es par
            n = n // 2
        else:  # Si es impar
            n = 3 * n + 1
        iterations += 1
    return iterations

# Lista para almacenar los números y sus iteraciones
numbers = []
iterations = []

# Calcular el número de iteraciones de Collatz para los números entre 1 y 10,000
for n in range(1, 10001):
    num_iterations = collatz_iterations(n)
    numbers.append(n)
    iterations.append(num_iterations)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(numbers, iterations, s=1, color='blue')  # Gráfico de dispersión
plt.title('Número de Iteraciones de la Conjetura de Collatz (1-10,000)')
plt.xlabel('Número Inicial (n)')
plt.ylabel('Número de Iteraciones')
plt.grid(True)

# Guardar el gráfico como imagen
plt.savefig('C:/Users/nacho/Desktop/Lic-en-Sistemas/3ro/Ing-soft2/TP1/src/collatz.png')

# Mostrar el gráfico
plt.show()