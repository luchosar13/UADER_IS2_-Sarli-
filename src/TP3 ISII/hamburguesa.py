import os

class Hamburguesa:
    def __init__(self, tipo_entrega):
        self.tipo_entrega = tipo_entrega

    def __str__(self):
        return f'Hamburguesa {self.tipo_entrega}'

class HamburguesaFactory:
    def crear_hamburguesa(self, tipo_entrega):
        hamburguesa = Hamburguesa(tipo_entrega)
        return hamburguesa
    

hamb = HamburguesaFactory()

os.system('cls')

print('----------Opciones----------')
print()
print('1- Entregada en mostrador')
print('2- Retirada por el cliente')
print('3- Enviada por delivery')

opcion = int(input())

vec = ['entregada en mostrador','retirada por el cliente','enviada por delivery']

if opcion:
    print(hamb.crear_hamburguesa(vec[opcion-1]))

