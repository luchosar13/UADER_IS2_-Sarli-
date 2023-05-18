import os
from random import randint
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):
		
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {} {} {}".format(self.stations[self.pos], self.name,"con memoria",self.memoria[randint(0,1)]))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"
		self.memoria = ["M1","M3"]

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"
		self.memoria = ["M2","M4"]

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)

#*--- Inicialmente en FM

		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

#*---------------------

if __name__ == "__main__":
	os.system("cls")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 3

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

