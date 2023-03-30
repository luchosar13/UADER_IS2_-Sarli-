class Factorial:
    def __init__(self):
        pass
    
    def calcular(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact
    
    def run(self, min, max):
        for num in range(min, max+1):
            print("El Factorial del numero ", num, " es: ", self.calcular(num))

f = Factorial()

print('Ingrese el numero minimo: ')

min = (int(input()))

print('Ingrese el numero maximo: ')

max = (int(input()))

f.run(min,max)
