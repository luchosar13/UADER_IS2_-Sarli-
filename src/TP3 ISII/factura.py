import os

class Factura:
    def __init__(self, monto, condicion_impositiva):
        self.monto = monto
        self.condicion_impositiva = condicion_impositiva

    def __str__(self):
        return f'El monto de la factura es de ${self.monto} con un tipo de condicion impositiva - {self.condicion_impositiva}'
        
class FacturaFactory:
    def crear_factura(self, monto , condicion_impositiva):
        fac = Factura(monto,condicion_impositiva)
        return fac

os.system('cls')

factu = FacturaFactory()

vec = ['IVA responsable','IVA no inscripto','IVA exento']

print('----------Bienvenido a la pagina de facturacion----------')

print('')

print('----------Opciones de facturacion----------')
print()
print('1- IVA responsable')
print('2- IVA no inscripto')
print('3- IVA no exento')

opcion = int(input())

print('')

print('----------Ingreso de monto----------')
print()
print('Ingrese el monto facturado: ')
monto = int(input())

if opcion:
    print(factu.crear_factura(monto,vec[opcion-1]))
