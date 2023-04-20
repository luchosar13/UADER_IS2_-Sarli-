import sys

class Factorial:
    __instance = None

    def __init__(self):
        if Factorial.__instance is not None:
            raise Exception("La instancia Singleton ya existe.")
        else:
            Factorial.__instance = self

    @staticmethod
    def get_instance():
        if Factorial.__instance is None:
            Factorial()
        return Factorial.__instance

    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n-1)

fac = Factorial.get_instance()

if len(sys.argv) == 2:
    num = int(sys.argv[1])
    print(f"el factorial de ",num," es: ",fac.calculate_factorial(num))
else:
    print("No se ha ingresado un argumento.")



