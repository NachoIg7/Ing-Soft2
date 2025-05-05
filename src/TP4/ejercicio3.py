# Represente la lista de piezas componentes de un ensamblado con sus 
# relaciones jerárquicas. Empiece con un producto principal formado por tres 
# sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases 
# que representen esa configuración y la muestren. Luego agregue un sub
# conjunto opcional adicional también formado por cuatro piezas. (Use el patrón 
# composite).
from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

#pieza invidiual
class Pieza(Componente):
    def __init__(self, nombre):
        self._nombre = nombre

    def mostrar(self, nivel=0):
        print(" "* nivel + f"- {self._nombre}")

#composite (subconjunto o ensamblado)
class SubConjunto (Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self._componentes = []
    
    def agregar (self, componente):
        self._componentes.append(componente)

    def mostrar(self, nivel=0):
        print(" "* nivel + f"- {self.nombre}")
        for componente in self._componentes:
            componente.mostrar(nivel + 1)

#cliente
if __name__=="__main__":
    #producto principal
    producto=SubConjunto("Producto principal")

    #creamos 3 subconjuntos con 4 piezas cada uno
    for i in range(1,4):
        subconjunto = SubConjunto(f"SubConjunto {i}")
        for j in range(1,5):
            pieza = Pieza(f"pieza {i}.{j}")
            subconjunto.agregar(pieza)
        producto.agregar(subconjunto)
    
    #mostramos ensamblado inicial
    print("Ensamblado inicial:")
    producto.mostrar()

    #agregamos un subconjunto opcional
    subconjunto_extra = SubConjunto("Subconjunto opcional")
    for k in range (1,5):
        pieza = Pieza (f"Pieza extra.{k}")
        subconjunto_extra.agregar(pieza)
    producto.agregar(subconjunto_extra)

    #mostramos ensamblado final
    print("\nEnsamblado final con producto opcional:")
    producto.mostrar()
    