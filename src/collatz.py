import matplotlib.pyplot as plt
import numpy as np

#Funcion para calcular la secuencia de collatz
def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

#Listas
n_values = []
counts = []

#Se le suma al 10000 un +1 porque la función -rango- no toma la ultima posicion
for n in range(1, 100):
    n_values.append(n)
    counts.append(collatz(n))

#Grafico
plt.scatter(n_values, counts)
plt.xlabel('Número de inicio')
plt.ylabel('Número de iteraciones')
plt.plot(n_values, counts)
plt.show()
