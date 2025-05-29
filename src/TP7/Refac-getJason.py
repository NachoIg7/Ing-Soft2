# ===============================================================
#  Programa de lectura de datos desde archivo JSON
#  
#  Permite obtener un valor asociado a una clave desde un archivo
#  JSON externo, manejando errores controlados.
#
#  Implementa dos versiones:
#   - Código procedural clásico (original)
#   - Versión orientada a objetos con patrón Singleton y branching
#
#  La selección entre versiones se realiza mediante la constante
#  USAR_BRANCHING definida al inicio.
#
#  copyright UADER FCyT-IS2©2024 todos los derechos reservados.
# ===============================================================
VERSION = "1.1"

import json
import sys
import os
from abc import ABC, abstractmethod

# ========================= CONFIGURACIÓN =============================
USAR_BRANCHING = False  # Cambiar a False para usar el código original
# ======================================================================

def mostrar_version():
    """Muestra la versión del programa y finaliza"""
    print(f"Versión {VERSION}")
    sys.exit(0)


# Clase abstracta: la abstracción
class JSONDataReader(ABC):
    @abstractmethod
    def cargar_dato(self):
        pass

    @abstractmethod
    def obtener_dato(self, key):
        pass

    @abstractmethod
    def imprimir_valor(self, key, value):
        pass

    @abstractmethod
    def imprimir_error(self, message):
        pass

    @abstractmethod
    def validar_argumentos(self, argumentos):
        pass

# Implementación refactorizada con Singleton
class JSONDataHandler(JSONDataReader):
    _instance = None

    def __new__(cls, filename="sitedata.json"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.filename = filename
            cls._instance.data = None
        return cls._instance

    def cargar_dato(self):
        if not os.path.exists(self.filename):
            return f"El archivo '{self.filename}' no existe."
        try:
            with open(self.filename, 'r') as json_file:
                self.data = json.load(json_file)
        except json.JSONDecodeError:
            return f"El archivo '{self.filename}' no contiene un JSON válido."
        except Exception as e:
            return f"Error inesperado al cargar el archivo: {e}"
        return None

    def obtener_dato(self, key):
        if self.data is None:
            return None, "Los datos no han sido cargados. Llame a cargar_dato() primero."
        if key in self.data:
            return self.data[key], None
        else:
            return None, f"La clave '{key}' no se encuentra en {self.filename}"

    def imprimir_valor(self, key, value):
        print(f"Valor de '{key}': {value}")

    def imprimir_error(self, message):
        print(f"Error: {message}")

    def validar_argumentos(self, argumentos):
        if len(argumentos) > 2:
            return None, "Demasiados argumentos. Uso correcto: python app.py [clave]"
        if len(argumentos) == 2:
            clave = argumentos[1]
            if not clave.strip():
                return None, "La clave no puede estar vacía."
            return clave, None
        return "token1", None

# ============================= BRANCHING ==============================

def branching_main():
    #Muestra version actual del programa
    if "-v" in sys.argv:
        mostrar_version()

    json_file = "sitedata.json"
    data_handler = JSONDataHandler(json_file)

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

# =========================== ORIGINAL PROCEDURAL ======================

def original_main():

    #Muestra version actual del programa
    if "-v" in sys.argv:
        mostrar_version()


    json_file = "sitedata.json"
    default_key = "token1"

    if len(sys.argv) > 2:
        print("Error: Demasiados argumentos. Uso correcto: python app.py [clave]")
        return

    key = sys.argv[1] if len(sys.argv) == 2 else default_key

    if not os.path.exists(json_file):
        print(f"Error: El archivo '{json_file}' no existe.")
        return

    try:
        with open(json_file, 'r') as json_file_obj:
            data = json.load(json_file_obj)
    except json.JSONDecodeError:
        print(f"Error: El archivo '{json_file}' no contiene un JSON válido.")
        return
    except Exception as e:
        print(f"Error inesperado al cargar el archivo: {e}")
        return

    if key in data:
        print(f"[Original] Valor de '{key}': {data[key]}")
    else:
        print(f"[Original] La clave '{key}' no se encuentra en {json_file}")

# =========================== MAIN SELECCIONADOR ========================

if __name__ == "__main__":
    if USAR_BRANCHING:
        branching_main()
    else:
        original_main()