#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

#importamos la libreria sys
import sys


#Funcion factorial

def factorial(num):
    if num < 0:
        print("Factorial de un número negativo no existe")
    elif num == 0:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

#Definimos la condicion de que si no se paso el argumento lo pida

if len(sys.argv) == 1:
    rango = input("Ingrese un rango de números separado por un guión (-) para calcular sus factoriales: ")
else:
    rango = sys.argv[1]

#Con la funcion split separamos los numeros ingresados en el argumento
#y la funcion map los convierte en int para asigarnos a desde y hasta"

desde, hasta = map(int, rango.split("-"))
print("Calculando factoriales para el rango:", desde, "-", hasta)

#El for pasa por todos los numeros ingresados y va printeando sus factoriales

for num in range(desde, hasta+1):
    print("El Factorial del numero ", num, " es: ", factorial(num))


