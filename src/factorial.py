
import sys

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

if len(sys.argv) == 1:
    rango = input("Ingrese un rango de números separado por un guión (-) para calcular sus factoriales: ")
else:
    rango = sys.argv[1]

if rango.startswith("-"):
    hasta = int(rango[1:])
    desde = 1
    print("Calculando factoriales desde", desde, "hasta", hasta)
else:
    desde, hasta = map(int, rango.split("-"))
    if rango.endswith("-"):
        hasta = 60
    print("Calculando factoriales desde", desde, "hasta", hasta)

for num in range(desde, hasta+1):
    print("El Factorial del numero ", num, " es", factorial(num))
