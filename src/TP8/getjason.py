"""
===============================================================
-Programa de lectura de datos desde archivo JSON
-Permite obtener un valor asociado a una clave desde un archivo
-JSON externo, manejando errores controlados.
-Implementa dos versiones:
-Código procedural clásico (original)
-Versión orientada a objetos con patrón Singleton y branching
-La selección entre versiones se realiza mediante la constante 
-USAR_BRANCHING definida al inicio.
-Aplicado re-ingenieria para sistema de gestion de pago de multiples cuentas
-Utiliza patrón Iterator para listar cronológicamente los pagos realizados.



-copyright UADER FCyT-IS2©2024 todos los derechos reservados.
-===============================================================
"""
import json
import sys
import os
from abc import ABC, abstractmethod

VERSION = "1.2"


DEFAULT_JSON_FILE = "sitedata.json"

# ========================= CONFIGURACIÓN =============================
USAR_BRANCHING = True  # Cambiar a False para usar el código original
# ======================================================================

def mostrar_version():
    """Muestra la versión del programa y finaliza"""
    print(f"Versión {VERSION}")
    sys.exit(0)


# Clase abstracta: la abstracción
class JSONDataReader(ABC):
    """Interfaz para leer datos JSON."""

    @abstractmethod
    def cargar_dato(self):
        """Carga los datos desde un archivo JSON."""

    @abstractmethod
    def obtener_dato(self, key):
        """Obtiene el dato correspondiente a la clave dada."""

    @abstractmethod
    def imprimir_valor(self, key, value):
        """Imprime el valor asociado a la clave."""

    @abstractmethod
    def imprimir_error(self, message):
        """Imprime un mensaje de error."""

    @abstractmethod
    def validar_argumentos(self, argumentos):
        """Valida los argumentos recibidos desde línea de comandos."""



class JSONDataHandler(JSONDataReader):
    """Manejador de datos JSON con patrón Singleton."""

    __instance = None

    def __new__(cls, filename=DEFAULT_JSON_FILE):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.filename = filename
            cls.__instance.data = None
        return cls.__instance

    def __init__(self, filename=DEFAULT_JSON_FILE):
        if not hasattr(self, 'filename'):
            self.filename = filename
            self.data = None

    def cargar_dato(self):
        """
        Carga datos desde el archivo JSON definido en self.filename.

        Retorna:
            None si carga correctamente, o mensaje de error en caso contrario.
        """
        if not os.path.exists(self.filename):
            return f"El archivo '{self.filename}' no existe."

        try:
            with open(self.filename, "r", encoding="utf-8") as json_file:
                self.data = json.load(json_file)
        except json.JSONDecodeError:
            return f"El archivo '{self.filename}' no contiene un JSON válido."
        except (OSError, IOError) as error:
            return f"Error inesperado al cargar el archivo: {error}"

        return None

    def obtener_dato(self, key):
        """
        Obtiene el valor correspondiente a 'key' en los datos cargados.

        Retorna:
                (valor, None) si se encuentra la clave,
                (None, mensaje de error) en caso contrario.
        """
        if self.data is None:
            return None, "Los datos no han sido cargados. Llame a cargar_dato() primero."

        if key in self.data:
            return self.data[key], None

        return None, f"La clave '{key}' no se encuentra en {self.filename}"

    def imprimir_valor(self, key, value):
        """Imprime el valor asociado a la clave proporcionada."""
        print(f"Valor de '{key}': {value}")

    def imprimir_error(self, message):
        """Imprime un mensaje de error."""
        print(f"Error: {message}")

    def validar_argumentos(self, argumentos):
        """
        Valida los argumentos recibidos desde la línea de comandos.

        Retorna:
                (clave, None) si es válido,
                (None, mensaje de error) si no.
        """
        if len(argumentos) > 2:
            return None, "Demasiados argumentos."

        if len(argumentos) == 2:
            clave = argumentos[1].strip()
            if not clave:
                return None, "La clave no puede estar vacía."
            return clave, None

        return "token1", None
    
    def obtener_clave (self, token):
        valor, error = self.obtener_dato(token)
        if error:
            raise KeyError(error)
        return valor

#Clase para la cadena de pagos
class PagoHandler(ABC):
    
    # Representa una cuenta bancaria con saldo y token asociado.

    # Permite verificar si puede procesar un pago y descontar su saldo.
    
    def __init__(self, saldo_inicial, token):
        #  Inicializa la cuenta con un saldo y un token.
        self.saldo = saldo_inicial
        self.token = token
        self.siguiente = None

    def establecer_siguiente (self, siguiente):
        self.siguiente = siguiente

    def puede_procesar (self, monto):
        #Verifica si el saldo disponible de la cuenta puede cubrir el monto de la operacion.
        return self.saldo >= monto
    
    
    def procesar_pago(self, pedido, monto, listado):
        #Si el saldo de la cuenta no puede cubrir la operacion, avisa con un mensaje
        if self.puede_procesar(monto):
            clave = JSONDataHandler().obtener_clave(self.token)
            self.saldo -= monto
            pago = {
                "pedido": pedido,
                "token": self.token,
                "clave": clave,
                "monto" : monto
            }
            listado.agregar_pago (pago)
            print(f"Pedido {pago['pedido']} - Token: {pago['token']} - Clave: {pago['clave']} - Monto: ${pago['monto']}")
        elif self.siguiente:
            self.siguiente.procesar_pago(pedido, monto, listado)
        else:
            print (f"Pedido {pedido}: Sin fondos en ninguna cuenta para ${monto}")
    
   
# Iterator para listado de pagos
class ListadoPagos:
    # Gestiona el registro ordenado de pagos realizados.
    def __init__ (self):
        #Inicializa el listado de pagos como lista vacía.
        self.pagos = []
    
    def agregar_pago (self, pago):
        #Agrega un pago al listado.
        self.pagos.append(pago)
    
    def __iter__ (self):
        #Permite iterar sobre los pagos registrados.
        return iter (self.pagos)
    
    def mostrar_listado(self):
        # Muestra el resumen de pagos ordenado por número de pedido.
        print("\n======= RESUMEN DE PAGOS REALIZADOS =======")
        for pago in self:
            print(f"Pedido N°{pago['pedido']}: ${pago['monto']} pagado con {pago['token']} (Clave: {pago['clave']})")
        print("===========================================\n")




def branching_main():
    """
    Ejecuta la versión orientada a objetos con gestión de pagos automática.

    Aplica balanceo secuencial de pagos entre cuentas según disponibilidad.
    """
 # Mostramos versión actual si se pide en consola
    if "-v" in sys.argv:
        mostrar_version()

    data_handler = JSONDataHandler(DEFAULT_JSON_FILE)

    clave, error = data_handler.validar_argumentos(sys.argv)
    if error:
        data_handler.imprimir_error(error)
        return

    error = data_handler.cargar_dato()
    if error:
        data_handler.imprimir_error(error)
        return

    valor, error = data_handler.obtener_dato(clave)
    if error:
        data_handler.imprimir_error(error)
    else:
        data_handler.imprimir_valor(clave, valor)
    
    #  Definición de cuentas bancarias y sus saldos
    cuentas = [
        PagoHandler(1000, "token1"),
        PagoHandler(2000, "token2")
    ]
   
    listado = ListadoPagos()
    # Simular pedidos de pago $500
    pedidos = [(1, 500), (2, 500), (3, 500), (4, 500), (5, 500)]

    indice_actual = 0

    for pedido, monto in pedidos:
        intentos = 0
        procesado = False
        
        while intentos < len(cuentas):
            cuenta = cuentas[indice_actual]
            if cuenta.puede_procesar(monto):
                cuenta.procesar_pago(pedido, monto, listado)
                procesado = True
                break
            else:
                print(f">>> {cuenta.token} sin saldo suficiente para Pedido {pedido}, se pasa a la siguiente cuenta.")

            indice_actual = (indice_actual + 1) % len(cuentas)
            intentos +=1
        
        if not procesado:
            print (f"Pedido {pedido}: Sin fondos en ninguna cuenta")
    

        # Avanza turno al siguiente banco para el próximo pedido
        indice_actual = (indice_actual + 1) % len(cuentas)
    listado.mostrar_listado()

    # Resumen de saldos finales
    print("======= SALDOS FINALES DE CADA CUENTA =======")
    for cuenta in cuentas:
        print(f"{cuenta.token}: ${cuenta.saldo}")
    print("=============================================")

def original_main():
    """Ejecuta la lógica principal con código procedural original."""

   # Mostramos versión actual si se pide en consola
    if "-v" in sys.argv:
        mostrar_version()

    json_filename = DEFAULT_JSON_FILE
    default_key = "token1"

    if len(sys.argv) > 2:
        print("Error: Demasiados argumentos.")
        return

    key = sys.argv[1].strip() if len(sys.argv) == 2 else default_key

    if not os.path.exists(json_filename):
        print(f"Error: El archivo '{json_filename}' no existe.")
        return

    try:
        with open(json_filename, "r", encoding="utf-8") as json_file_obj:
            data = json.load(json_file_obj)
    except json.JSONDecodeError:
        print(f"Error: El archivo '{json_filename}' no contiene un JSON válido.")
        return
    except Exception as error:
        print(f"Error inesperado al cargar el archivo: {error}")
        return

    if key in data:
        print(f"[Original] Valor de '{key}': {data[key]}")
    else:
        print(f"[Original] La clave '{key}' no se encuentra en {json_filename}")


if __name__ == "__main__":
    if USAR_BRANCHING:
        branching_main()
    else:
        original_main()
