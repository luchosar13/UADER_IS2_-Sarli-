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
