
# class FactorialSingleton:
#     #instancia unica de la clase
#     _instance = None
#     # metodo _new_ para asegurarse de que solo haya una instancia.
#     def __new__ (clase):
#         if clase._instance is None:
#             clase._instance = super (FactorialSingleton, clase).__new__ (clase)
#         return clase._instance
    
#     #calculamos facrorial
#     def factorial (self, num):
#         if num < 0:
#             raise ValueError ("El factorial de un número negativo no existe")
#         if num == 0 or num == 1:
#             return 1
#         else:
#             return num * self.factorial (num - 1)

# class OtraClase:
#     def __init__(self):
#         self.factorial_instance = FactorialSingleton()

#     def calcular_factorial(self, num):
#         return self.factorial_instance.factorial(num)

# class OtraClase2:
#     def __init__(self):
#         self.factorial_instance = FactorialSingleton()

#     def calcular_factorial(self, num):
#         return self.factorial_instance.factorial(num)



# a = OtraClase()
# b = OtraClase2()

# # Verificamos que ambas clases usan la misma instancia
# print(a.factorial_instance is b.factorial_instance)

# # Cálculos
# print(a.calcular_factorial(5))
# print(b.calcular_factorial(6))



##-------------------------------------------------------------------------------------##
#Calculadora de impuestos

# class CalculadoraImpuestos:
#     def __init__ (self, base_imponible):
#         self.base_imponible = base_imponible

#     def calcular_iva(self):
#         return self.base_imponible * 0.21
    
#     def calcular_iibb(self):
#         return self.base_imponible * 0.05
    
#     def calcular_contribuciones_municipales(self):
#         return self.base_imponible * 0.012

#     def calcular_total_impuestos(self):
#         iva = self.calcular_iva()
#         iibb = self.calcular_iibb()
#         contribuciones_municipales = self.calcular_contribuciones_municipales()
#         return iva + iibb + contribuciones_municipales
    

# base_imponible = (1426)

# calculadora = CalculadoraImpuestos(base_imponible)

# total_impuestos = calculadora.calcular_total_impuestos()

# print(f"Con una base imponible de {base_imponible}: el total de impuestos serà de: {total_impuestos}")


##-------------------------------------------------------------------------------------##
#Comida rapida Hamburguesa

# class ComidaRapida:
#     def __init__(self, nombre, metodo_entrega):
#         self.nombre = nombre
#         self.metodo_entrega = metodo_entrega

#     def entrega(self):
#         if self.metodo_entrega == "mostrador":
#             print (f"El pedido de {self.nombre} sera entregado en el mostrador.")
#         elif self.metodo_entrega == "delivery":
#             print (f"El pedido de {self.nombre} sera entregado por delivery.")
#         elif self.metodo_entrega == "retiro":
#             print (f"El pedido de {self.nombre} sera retirado por el cliente.")
#         else:
#             print (f"El pedido de {self.nombre} no pudo ser entregado.")

# pedido1 = ComidaRapida ("hamburguesa", "mostrador")
# pedido1.entrega()

# pedido2 = ComidaRapida ("hamburguesa", "delivery")
# pedido2.entrega()

# pedido3 = ComidaRapida ("hamburguesa", "retiro")
# pedido3.entrega()

# pedido4 = ComidaRapida ("hamburguesa", "--")
# pedido4.entrega()


##-------------------------------------------------------------------------------------##

# Implemente una clase “factura” que tenga un importe correspondiente al total 
# de la factura pero de acuerdo a la condición impositiva del cliente (IVA 
# Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal 
# condición. 

# class Factura:
#     def __init__(self, importe, condicion_impositiva):
#         self.importe = importe
#         self.condicion_impositiva = condicion_impositiva

#     def calcular_importe(self):
#         if self.condicion_impositiva == "IVA Responsable":
#             return self.importe * 1.21
#         elif self.condicion_impositiva == "IVA No Inscripto":
#             return self.importe * 1.1
#         elif self.condicion_impositiva == "IVA Exento":
#             return self.importe
#         else:
#             return self.importe

# cliente1 = Factura (2000, "IVA Responsable")
# importe1 = cliente1.calcular_importe()
# print(f"El importe de la factura es de {importe1} pesos. Su condicion frente a IVA : {cliente1.condicion_impositiva}")

# cliente2 = Factura (1450, "IVA No Inscripto")
# importe2 = cliente2.calcular_importe()
# print(f"El importe de la factura es de {importe2} pesos. Su condicion frente a IVA : {cliente2.condicion_impositiva}")

# cliente3 = Factura (4200, "IVA Exento")
# importe3 = cliente3.calcular_importe()
# print(f"El importe de la factura es de {importe3} pesos. Su condicion frente a IVA : {cliente3.condicion_impositiva}")




# Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar 
# para construir aviones en lugar de vehículos. Para simplificar suponga que un 
# avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje

# class Avion:
#    def __init__(self):
#       self.partes = []

#    def agregar_parte(self, parte):
#       self.partes.append(parte)

#    def mostrar_partes(self):
#       print ("Avion construido con:")
#       for parte in self.partes:
#          print (f"- {parte}")

# #builder
# class AvionBuilder:
#    def construir_body(self):
#         self.avion = Avion()
#         self.avion.agregar_parte("body")

#    def construir_turbinas(self):
#         self.avion.agregar_parte("turbina 1")
#         self.avion.agregar_parte("turbina 2")

#    def construir_alas(self):
#         self.avion.agregar_parte("ala izquierda")
#         self.avion.agregar_parte("ala derecha")
#    def construir_tren(self):
#         self.avion.agregar_parte("tren de aterrizaje")

#    def obtener_avion(self):
#       return self.avion

# # Director
# class AvionDirector:
#    def __init__(self):  
#       self.builder = AvionBuilder()

#    def construir_avion(self):
#       self.builder.construir_body()
#       self.builder.construir_turbinas()
#       self.builder.construir_alas()
#       self.builder.construir_tren() 
#       return self.builder.obtener_avion()

# # Ejemplo de uso
# director = AvionDirector()
# avion = director.construir_avion()
# avion.mostrar_partes()


# Dado una clase que implemente el patrón “prototipo” verifique que una clase 
# generada a partir de ella permite por su parte obtener también copias de si 
# misma.

# import copy

# class Prototipo:
#     def __init__(self, nombre, datos):
#         self.nombre = nombre
#         self.datos = datos

#     def clonar (self):
#         return copy.deepcopy(self)
    
#     def mostrar (self):
#         print (f"Nombre: {self.nombre}")
#         print (f"Datos: {self.datos}")

# #Prueba
# original = Prototipo ("Original", [1,2,3,4,5])
# print ("Objeto original")
# original.mostrar()

# clon1 = original.clonar()
# print ("primer clon")
# clon1.mostrar()

# clon2 = clon1.clonar()
# print ("clon de clon1")
# clon2.mostrar()


##Imagine una situación donde pueda ser de utilidad el patrón “abstract factory”. 

# Un ejemplo de situacion donde seria util utilizar el patron abstract factory seria en un e-commerce osco donde existen varios metodos de pago
# como mercadopago y paypal, implementandolo en codigo:

#metodo de pago abstract factory
class MetodoPago:
    def crear_metodo_pago(self): pass
    def crear_reembolso(self): pass

#metodos concretos de pago
class MercadoPago(MetodoPago):
    def crear_metodo_pago(self):
        return PagoMercadopago()
    def crear_reembolso(self):
        return ReembolsoMercadopago()

class Paypal(MetodoPago):
    def crear_metodo_pago(self):
        return PagoPaypal()
    def crear_reembolso(self):
        return ReembolsoPaypal()

class PagoMercadopago:
    def pagar(self):
        print("-Pagando con Mercadopago")

class ReembolsoMercadopago:
    def reembolsar(self):
        print("-Reembolsando con Mercadopago")

class PagoPaypal:
    def pagar(self):
        print("-Pagando con Paypal")

class ReembolsoPaypal:
    def reembolsar(self):
        print("-Reembolsando con Paypal")

def procesar_pago(factory: MetodoPago): 
    pago = factory.crear_metodo_pago()
    reembolso = factory.crear_reembolso()
    pago.pagar()
    reembolso.reembolsar()

print ("----------Procesando pago con Mercadopago----------")
procesar_pago(MercadoPago())

print ("----------Procesando pago con Paypal----------")
procesar_pago(Paypal())
