import sys
import os
os.system ("cls")
#FUNCIÓN PARA CALCULO DEL FACTORIAL DE "n”
def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
        
    elif n > 1:
        resultado = n * factorial (n-1)
        
    return resultado


try:
    n= int (input("ingrese un numero para calcular su factorial : "))
    
    if  n > 996:
        print ("El numero es demasiado grande")
        sys.exit()
        os.systen("cls")

    r = factorial(n)
    print (f"el factorial de {n} es: {r}")

except Exception as e:
    print (f"Error inesperado: {e}")