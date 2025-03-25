#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Función para validar y extraer el rango
def get_range(value):
    if '-' in value:
        start, end = value.split('-')
        if start.isdigit() and end.isdigit():
            return int(start), int(end)
        else:
            print("Por favor, ingrese un rango válido con números enteros.")
            return None
    else:
        print("Por favor, ingrese un rango en el formato desde-hasta (ej. 4-8).")
        return None

# Verificar si se pasó un argumento en la línea de comandos
if len(sys.argv) == 1:
    # Si no se pasa argumento, solicita el rango al usuario
    num_input = input("Debe ingresar un rango (desde-hasta) para calcular los factoriales: ")
    
    # Verificar si el input tiene formato correcto
    range_values = get_range(num_input)
    if range_values:
        start, end = range_values
    else:
        sys.exit()
else:
    # Si se pasa argumento, usa el rango proporcionado
    num_input = sys.argv[1]
    
    # Verificar si el argumento tiene formato correcto
    range_values = get_range(num_input)
    if range_values:
        start, end = range_values
    else:
        sys.exit()

# Calcular y mostrar los factoriales en el rango
for i in range(start, end + 1):
    print(f"El factorial de {i} es: {factorial(i)}")