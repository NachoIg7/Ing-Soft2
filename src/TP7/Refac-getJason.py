import json
import sys

class JSONDataHandler:
    """Clase para manejar la lectura y búsqueda en archivos JSON"""
    
    def __init__(self, filename="sitedata.json"):
        """Inicializa el manejador con el nombre del archivo JSON"""
        self.filename = filename
        self.data = None
    
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
            raise ValueError("Los datos no han sido cargados. Llame a load_data() primero.")
        
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(f"La clave '{key}' no se encuentra en {self.filename}")

class JSONDataPrinter:
    """Clase para manejar la presentación de los resultados"""
    
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
    json_file = "sitedata.json"
    default_key = "token1"
    
    # Obtener la clave desde argumentos, por defecto 'token1'
    key = sys.argv[1] if len(sys.argv) > 1 else default_key
    
    # Crear instancias de las clases
    data_handler = JSONDataHandler(json_file)
    printer = JSONDataPrinter()
    
    try:
        # Cargar y procesar los datos
        data_handler.load_data()
        value = data_handler.get_value(key)
        printer.print_success(key, value)
        
    except (FileNotFoundError, ValueError, KeyError, Exception) as e:
        printer.print_error(str(e))

if __name__ == "__main__":
    main()