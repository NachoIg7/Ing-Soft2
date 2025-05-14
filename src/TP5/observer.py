#  Implemente una clase bajo el patrón observer donde una serie de clases están 
# subscriptas, cada clase espera que su propio ID (una secuencia arbitraria de 4 
# caracteres) sea expuesta y emitirá un mensaje cuando el ID emitido y el propio 
# coinciden. Implemente 4 clases de tal manera que cada una tenga un ID 
# especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con 
# ID para el que tenga una clase implementada.


# Clase Subject (publicador)
class Subject:
    def __init__(self):
        # Lista de observadores registrados
        self.observers = []

    def subscribe(self, observer):
        # Agregar un observador a la lista
        self.observers.append(observer)

    def emit(self, id_value):
        # Emitir un ID y notificar a todos los observadores
        print(f"\nEmitiendo ID: {id_value}")
        for observer in self.observers:
            observer.notify(id_value)


# Clase base Observer (opcional, pero da claridad)
class Observer:
    def __init__(self, my_id):
        # Cada observador tiene su propio ID
        self.my_id = my_id

    def notify(self, id_value):
        # Si el ID emitido coincide con el suyo, muestra mensaje
        if id_value == self.my_id:
            print(f"El observador {self.my_id} detectó su ID.")


# Clases observadoras concretas
class ObserverA(Observer):
    def __init__(self):
        super().__init__("A123")


class ObserverB(Observer):
    def __init__(self):
        super().__init__("B456")


class ObserverC(Observer):
    def __init__(self):
        super().__init__("C789")


class ObserverD(Observer):
    def __init__(self):
        super().__init__("D000")


# =====================
#  Ejemplo de uso
# =====================

# Crear el publicador
subject = Subject()

# Crear los observadores
observer_a = ObserverA()
observer_b = ObserverB()
observer_c = ObserverC()
observer_d = ObserverD()

# Suscribir observadores al publicador
subject.subscribe(observer_a)
subject.subscribe(observer_b)
subject.subscribe(observer_c)
subject.subscribe(observer_d)

# Emitir IDs (al menos 4 coincidentes con los observadores)
id_list = ["A123", "X999", "B456", "Z111", "C789", "Y888", "D000", "W777"]
for id_value in id_list:
    subject.emit(id_value)