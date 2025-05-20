
import json
import sys

# Archivo JSON fijo
JSON_FILE = "sitedata.json"

# Obtener la clave desde argumentos, por defecto 'token1'
clave = sys.argv[1] if len(sys.argv) > 1 else "token1"

try:
    # Abrir y leer el contenido del archivo JSON
    with open(JSON_FILE, 'r') as json_file:
        data = json.load(json_file)

    # Intentar recuperar el valor de la clave
    if clave in data:
        print(f"Valor de '{clave}': {data[clave]}")
    else:
        print(f" La clave '{clave}' no se encuentra en {JSON_FILE}")

except FileNotFoundError:
    print(f" Error: El archivo '{JSON_FILE}' no existe.")
except json.JSONDecodeError:
    print(f" Error: El archivo '{JSON_FILE}' no contiene un JSON válido.")
except Exception as e:
    print(f" Error inesperado: {e}")