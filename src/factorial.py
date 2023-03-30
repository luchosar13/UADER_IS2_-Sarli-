#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
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

if (len(sys.argv)) == 2:
    num = (int(sys.argv[1]))
else:
    if (len(sys.argv)) == 1:
        num = (int(input("Debe ingresar un numero para poder resolver el factorial: ")))

print("El factorial de ", num, " es: ", factorial(num))


