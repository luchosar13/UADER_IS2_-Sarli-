class TrenLaminador:
    def laminar(self, lamina):
        pass

class TrenLaminador5(TrenLaminador):
    def laminar(self, lamina):
        print(f'Laminando la lámina de {lamina.esp} de espesor y {lamina.ancho} metros de ancho en un tren laminador de 5 metros')
        lamina.producto = f'Plancha de {lamina.esp} de espesor y {lamina.ancho} metros de ancho, laminada en un tren laminador de 5 metros'

class TrenLaminador10(TrenLaminador):
    def laminar(self, lamina):
        print(f'Laminando la lámina de {lamina.esp} de espesor y {lamina.ancho} metros de ancho en un tren laminador de 10 metros')
        lamina.producto = f'Plancha de {lamina.esp} de espesor y {lamina.ancho} metros de ancho, laminada en un tren laminador de 10 metros'

class Lamina:
    def __init__(self, esp, ancho, tren_laminador):
        self.esp = esp
        self.ancho = ancho
        self.tren_laminador = tren_laminador
        self.producto = None
        
    def enviar_a_laminar(self):
        self.tren_laminador.laminar(self)

class Lamina5(Lamina):
    def __init__(self, esp, ancho):
        super().__init__(esp, ancho, TrenLaminador5())

class Lamina10(Lamina):
    def __init__(self, esp, ancho):
        super().__init__(esp, ancho, TrenLaminador10())


lamina = Lamina5(0.5, 1.5)
lamina.enviar_a_laminar()
print(lamina.producto)

lamina = Lamina10(0.5, 1.5)
lamina.enviar_a_laminar()
print(lamina.producto)