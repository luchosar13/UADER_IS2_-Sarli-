class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, number):
        if self.can_handle(number):
            self.process_request(number)
        elif self._successor is not None:
            self._successor.handle_request(number)

    def can_handle(self, number):
        raise NotImplementedError()

    def process_request(self, number):
        raise NotImplementedError()


class PrimeHandler(Handler):
    def can_handle(self, number):
        return self.is_prime(number)

    def process_request(self, number):
        print("Número primo consumido:", number)

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True


class EvenHandler(Handler):
    def can_handle(self, number):
        return self.is_even(number)

    def process_request(self, number):
        print("Número par consumido:", number)

    def is_even(self, number):
        return number % 2 == 0


class UnhandledHandler(Handler):
    def can_handle(self, number):
        return True

    def process_request(self, number):
        print("Número no consumido:", number)


# Creación de la cadena de responsabilidad
prime_handler = PrimeHandler()
even_handler = EvenHandler()
unhandled_handler = UnhandledHandler()

prime_handler.set_successor(even_handler)
even_handler.set_successor(unhandled_handler)

# Consumo de los números del 1 al 100
for number in range(1, 101):
    prime_handler.handle_request(number)
