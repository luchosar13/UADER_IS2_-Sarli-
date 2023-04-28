import os
#*--------------------------------------------------------------------
#* Ejemplo de pattern composite
#* Se genera una clase LeafElement que representa nodos terminales y una
#* CompositeLement que representa al arbol (de CompositeElement y LeafElement)
#* que de el dependen.
#*--------------------------------------------------------------------

#*------------- Define una clase para los nodos terminales (leaf)
class LeafElement:

	def __init__(self, *args):

#*--- indenta las posiciones a medida que se agregan
		self.position = args[0]

#*--- lista elementos

	def showDetails(self):

		'''Prints the position of the child element.'''
		print("\t", end ="")
		print(self.position)

#*---- Elemento compuesto, representa objetos en cualquier nivel de la jerarquia excepto el último

class CompositeElement:

	def __init__(self, *args):

		self.position = args[0]
		self.children = []

#*----- Crea jerarquia

	def add(self, child):

		self.children.append(child)

#*---- Remueve jerarquia

	def remove(self, child):

		self.children.remove(child)

#*---- muestra detalles (itera a los niveles inferiores


	def showDetails(self):

		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()


"""main method"""

if __name__ == "__main__":

	os.system("cls")

#*------ Crea el top level de la jerarquia

	ensamblado = CompositeElement("Ensamblado")

#*----- Crea el primer subconjunto

	subconjunto1 = CompositeElement("Subconjunto 1")

	pieza11 = LeafElement("Pieza 1")
	pieza12 = LeafElement("Pieza 2")
	pieza13 = LeafElement("Pieza 3")
	pieza14 = LeafElement("Pieza 4")
	

	subconjunto1.add(pieza11)
	subconjunto1.add(pieza12)
	subconjunto1.add(pieza13)
	subconjunto1.add(pieza14)

#*---- Crea el segundo subconjunto

	subconjunto2 = CompositeElement("Subconjunto 2")

	pieza21 = LeafElement("Pieza 1")
	pieza22 = LeafElement("Pieza 2")
	pieza23 = LeafElement("Pieza 3")
	pieza24 = LeafElement("Pieza 4")
	
	subconjunto2.add(pieza21)
	subconjunto2.add(pieza22)
	subconjunto2.add(pieza23)
	subconjunto2.add(pieza24)
	
#*---- Crea el tercer subconjunto

	subconjunto3 = CompositeElement("Subconjunto 3")

	pieza31 = LeafElement("Pieza 1")
	pieza32 = LeafElement("Pieza 2")
	pieza33 = LeafElement("Pieza 3")
	pieza34 = LeafElement("Pieza 4")
	
	subconjunto3.add(pieza31)
	subconjunto3.add(pieza32)
	subconjunto3.add(pieza33)
	subconjunto3.add(pieza34)

#*---- Agrega ahora las dos gerencias al nivel raiz

	ensamblado.add(subconjunto1)
	ensamblado.add(subconjunto2)
	ensamblado.add(subconjunto3)

#*---- Muestra el resultado

	ensamblado.showDetails()

print('')

res = str(input('Desea agregar un nuevo subconjunto?: (y/n): '))

if res == 'y':
	
	subconjunto4 = CompositeElement("Subconjunto 4")

	pieza41 = LeafElement("Pieza 1")
	pieza42 = LeafElement("Pieza 2")
	pieza43 = LeafElement("Pieza 3")
	pieza44 = LeafElement("Pieza 4")
	
	subconjunto4.add(pieza41)
	subconjunto4.add(pieza42)
	subconjunto4.add(pieza43)
	subconjunto4.add(pieza44)
	
	ensamblado.add(subconjunto4)
	
else:
	print('Gracias por utilizar el sistema.')

new = str(input('Desea ver el nuevo arbol modificado? (y/n): '))

if new == 'y':
    ensamblado.showDetails()
else:
	print('Gracias por utilizar el sistema.')
	

	#print("Remueve el subconjunto #3 recién agregada\n")
	#ensamblado.remove(subconjunto3)
	#ensamblado.showDetails()

