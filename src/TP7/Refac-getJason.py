import json
import sys

class JSONDataHandler:
    """Clase Singleton para manejar la lectura y búsqueda en archivos JSON"""
    
    _instance = None
    
    def __new__(cls, filename="sitedata.json"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.filename = filename
            cls._instance.data = None
        return cls._instance
    
    def load_data(self):
        """Carga los datos del archivo JSON"""
        try:
            with open(self.filename, 'r') as json_file:
                self.data = json.load(json_file)
            return True
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo '{self.filename}' no existe.")
        except json.JSONDecodeError:
            raise ValueError(f"El archivo '{self.filename}' no contiene un JSON válido.")
        except Exception as e:
            raise Exception(f"Error inesperado al cargar el archivo: {e}")
    
    def get_value(self, key):
        """Obtiene un valor del JSON por su clave"""
        if self.data is None:
            self.load_data()
        
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(f"La clave '{key}' no se encuentra en {self.filename}")

class JSONDataPrinter:
    """Clase para manejar la presentación de los resultados (también Singleton)"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def print_success(key, value):
        """Muestra un mensaje de éxito"""
        print(f"Valor de '{key}': {value}")
    
    @staticmethod
    def print_error(message):
        """Muestra un mensaje de error"""
        print(f"Error: {message}")

def main():
    # Configuración inicial
    default_key = "token1"
    
    # Obtener la clave desde argumentos, por defecto 'token1'
    key = sys.argv[1] if len(sys.argv) > 1 else default_key
    
    # Obtener las instancias Singleton
    data_handler = JSONDataHandler()
    printer = JSONDataPrinter()
    
    try:
        # Obtener y mostrar el valor
        value = data_handler.get_value(key)
        printer.print_success(key, value)
        
    except (FileNotFoundError, ValueError, KeyError, Exception) as e:
        printer.print_error(str(e))

if __name__ == "__main__":
    main()