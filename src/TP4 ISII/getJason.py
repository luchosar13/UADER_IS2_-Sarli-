import json
import sys

class Singleton:
    """Este programa permite extraer la clave de acceso API para utilizar los servicios del 
    Banco XXX.
    """
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Implementacion del patron Singleton al programa getJason.py")
        Singleton.__instance = self

    @staticmethod
    def get_instance():
        """
        Funcion por la cual se obtiene la instancia
        """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def run(self):
        """
        Funcion para correr el programa
        """
        print'copyright IS2 2022,2023 todos los derechos reservados'
        try:
            if sys.argv[1] == "-h":
                print"Ha entrado al panel de ayuda."
            else:
                jsonfile = sys.argv[1]
                jsonkey = sys.argv[2]
                try:
                    with open(jsonfile, 'r') as myfile:
                        data = myfile.read()
                        obj = json.loads(data)
                        try:
                            print(str(obj[jsonkey]))
                        except KeyError:
                            print"La clave especificada no existe en el objeto JSON."
                except IOError:
                    print"El archivo JSON especificado no existe."
        except IndexError:
            print"No se proporcionaron suficientes argumentos."

# Uso del Singleton
SINGLETON = Singleton.get_instance()
SINGLETON.run()

print


print'-----------------------------------------------------------'

print

class cuentas_banco:
    """Clase que representa una cuenta bancaria."""

    def __init__(self, token, balance):
        self.token = token
        self.balance = balance
        self.prox_cuenta = None

    def set_prox_cuenta(self, prox_cuenta):
        """Establece la siguiente cuenta en la cadena de responsabilidad."""
        self.prox_cuenta = prox_cuenta

    def procesar_pago(self, monto):
        """Procesa un pago en la cuenta actual o pasa la responsabilidad a la siguiente cuenta."""
        if self.balance >= monto:
            self.balance -= monto
            print("Pago realizado en la cuenta {}: {}".format(self.token, monto))
        elif self.prox_cuenta:
            self.prox_cuenta.procesar_pago(monto)
        else:
            print("Saldo insuficiente en todas las cuentas.")


# Crear las cuentas bancarias
account1 = cuentas_banco("token1", 1000)
account2 = cuentas_banco("token2", 2000)

# Establecer la cadena de responsabilidad
account1.set_prox_cuenta(account2)

# Procesar pagos
account1.procesar_pago(500)
account1.procesar_pago(1500)
account1.procesar_pago(1000)

