#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función para calcular el factorial
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
        if value.startswith('-'):  # Caso de rango -hasta
            end = value[1:]
            if end.isdigit():
                return 1, int(end)
            else:
                print("Por favor, ingrese un número válido después del guión.")
                return None
        elif value.endswith('-'):  # Caso de rango desde-
            start = value[:-1]
            if start.isdigit():
                return int(start), 60
            else:
                print("Por favor, ingrese un número válido antes del guión.")
                return None
        else:  # Caso de rango desde-hasta
            start, end = value.split('-')
            if start.isdigit() and end.isdigit():
                return int(start), int(end)
            else:
                print("Por favor, ingrese un rango válido en formato desde-hasta (ej. 4-8).")
                return None
    else:
        print("Por favor, ingrese un rango en el formato adecuado.")
        return None

# Verificar si se pasó un argumento en la línea de comandos
if len(sys.argv) == 1:
    # Si no se pasa argumento, solicita el rango al usuario
    num_input = input("Debe ingresar un rango para calcular los factoriales: ")
    
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