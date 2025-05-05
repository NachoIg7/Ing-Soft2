# Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho 
# dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro 
# de 10 mts. Genere una clase que represente a las láminas en forma genérica al 
# cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el 
# patrón bridge en la solución). 
from abc import ABC, abstractmethod
#implementador
class TrenLaminador(ABC):
    def laminar(self):
        pass

class Tren5mts (TrenLaminador):
    def laminar(self):
        print("Plancha en tren de 5 metros")

class Tren10mts (TrenLaminador):
    def laminar(self):
        print("Plancha en tren de 10 metros")

class Lamina:
    def __init__(self, Tren_laminador):
        self.espesor = 0.5 #pulgadas
        self.ancho = 1.5 #metros
        self.tren = Tren_laminador
    
    def producir (self):
        print(f'Lamina de {self.espesor}" de espesor y {self.ancho}mts de ancho.')
        self.tren.laminar()


if __name__=="__main__":
    tren5 = Tren5mts()
    tren10 = Tren10mts()
    print("--------------------")
    lamina = Lamina(tren5)
    lamina.producir()
    print("--------------------")
    lamina = Lamina(tren10)
    lamina.producir()