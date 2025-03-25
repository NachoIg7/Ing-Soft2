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

# Verificar si se pasó un argumento en la línea de comandos
if len(sys.argv) == 1:
    # Si no se pasa argumento, solicita el número al usuario
    num_input = input("Debe ingresar un número para calcular el factorial: ")
    
    # Verificar si el input es un número entero
    if num_input.isdigit():
        num = int(num_input)
    else:
        print("Por favor, ingrese un número entero válido.")
        sys.exit()
else:
    # Si se pasa argumento, usa el número proporcionado
    num_input = sys.argv[1]
    
    # Verificar si el argumento es un número entero
    if num_input.isdigit():
        num = int(num_input)
    else:
        print("Por favor, ingrese un número entero válido.")
        sys.exit()

print(f"El factorial de {num} es: {factorial(num)}")