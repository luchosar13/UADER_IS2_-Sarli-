import sys

class Impuestos:
    def __init__(self, base_imponible):
        self.base_imponible = base_imponible

    def calcular_iva(self):
        return self.base_imponible * 0.21

    def calcular_iibb(self):
        return self.base_imponible * 0.05

    def calcular_contribuciones_municipales(self):
        return self.base_imponible * 0.012

    def calcular_total_impuestos(self):
        iva = self.calcular_iva()
        iibb = self.calcular_iibb()
        contribuciones = self.calcular_contribuciones_municipales()
        return iva + iibb + contribuciones

base = int(sys.argv[1])

imp = Impuestos(base)

print('----------Impuestos----------')
print()
print(f"El valor del iva es de: ${imp.calcular_iva()}")
print()
print(f"El valor del iibb es de: ${imp.calcular_iibb()}")
print()
print(f"El valor de las contribuciones municipales es de: ${imp.calcular_contribuciones_municipales()}")
print('----------TOTAL----------')
print()
print(f"El total de impuestos sobre la base imponible es de: ${imp.calcular_total_impuestos()}")