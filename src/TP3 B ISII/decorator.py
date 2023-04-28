class Numero:
    def __init__(self, value):
        self.value = value
    
    def print_value(self):
        print(self.value)

class suma:
    def __init__(self, Numero, value):
        self.Numero = Numero
        self.value = value
    
    def print_value(self):
        self.Numero.print_value()
        print(self.Numero.value + self.value)

class Multiplicacion:
    def __init__(self, Numero, value):
        self.Numero = Numero
        self.value = value
    
    def print_value(self):
        self.Numero.print_value()
        print(self.Numero.value * self.value)

class Division:
    def __init__(self, Numero, value):
        self.Numero = Numero
        self.value = value
    
    def print_value(self):
        self.Numero.print_value()
        print(self.Numero.value / self.value)

print('El valor ingresado es: ')
num = Numero(5)
num.print_value()

print('')

num = suma(num,2)
num.print_value()

print('')

num = Multiplicacion(num, 2)
num.print_value()
#
num = Division(num, 3)
num.print_value()



