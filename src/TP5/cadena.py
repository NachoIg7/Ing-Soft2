# Cree una clase bajo el patrón cadena de responsabilidad donde los números del 
# 1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que 
# identifique la necesidad de consumir el número lo hará y caso contrario lo 
# pasará al siguiente en la cadena. Implemente una clase que consuma números 
# primos y otra números pares. Puede ocurrir que un número no sea consumido 
# por ninguna clase en cuyo caso se marcará como no consumido.

class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler  

    def handle(self, number):
        if self.next_handler:
            self.next_handler.handle(number)
        else:
            print(f"{number} no consumido.")

class EvenNumberHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} consumido por EvenNumberHandler.")
        else:
            super().handle(number)

class PrimeNumberHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} consumido por PrimeNumberHandler.")
        else:
            super().handle(number)

# -----------------------------
# Configurar la cadena
even_handler = EvenNumberHandler()
prime_handler = PrimeNumberHandler()

even_handler.set_next(prime_handler)

# Procesar números del 1 al 100
for num in range(1, 101):
    even_handler.handle(num)