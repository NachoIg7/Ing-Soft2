# Implemente una clase que permita a un número cualquiera imprimir su valor, 
# luego agregarle sucesivamente. 
# a. Sumarle 2. 
# b. Multiplicarle por 2. 
# c. Dividirlo por 3. 
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a 
# las clases con las diferentes operaciones. Use un patrón decorator para 
# implementar. 

from abc import ABC, abstractmethod
#clase abstracta base
class Numero (ABC):
    @abstractmethod
    def mostrar(self):
        pass

#clase concreta base
class NumeroConcreto(Numero):
    def __init__(self, valor):
        self.valor = valor
    
    def mostrar (self):
        print(f'{self.valor}')
        return self.valor

# decorator base
class NumeroDecorator(Numero):
    def __init__(self, numero):
        self.numero = numero

    def mostrar(self):
        self.numero.mostrar()
        
class SumarDos(NumeroDecorator):
    def mostrar (self):
        valor = self.numero.mostrar()
        resultado = valor + 2
        print (f" +2 = {resultado}")
        return resultado
        
class MultiplicarDos(NumeroDecorator):
    def mostrar (self):
        valor = self.numero.mostrar()
        resultado = valor * 2
        print (f" *2 = {resultado}")
        return resultado

class DividirTres(NumeroDecorator):
    def mostrar (self):
        valor = self.numero.mostrar()
        resultado = valor / 3
        print (f" /3 = {resultado}")
        return resultado

#ejemplo
if __name__ == "__main__":
    numero = NumeroConcreto(5)
    print ("Numero sin operaciones:")
    numero.mostrar()

    print("Con operaciones anidadas:")
    numero_operado = DividirTres(MultiplicarDos(SumarDos(numero)))
    numero_operado.mostrar()