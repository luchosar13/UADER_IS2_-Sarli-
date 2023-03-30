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

#Lista para los valores numericos que se van iterando
n_values = []
#Lista en la que se asignan la cantidad de iteraciones 
#que tiene un valor hasta llegar al numero 1
counts = []

#Se le suma al 100 un +1 porque la función -rango- no toma la ultima posicion
for n in range(1, 100+1):
    n_values.append(n)
    counts.append(collatz(n))

#Grafico
plt.scatter(n_values, counts)
plt.xlabel('Número de inicio')
plt.ylabel('Número de iteraciones')
plt.plot(n_values, counts)
plt.show()
