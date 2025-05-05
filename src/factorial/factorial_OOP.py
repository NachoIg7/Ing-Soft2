class Factorial:
    # Constructor de la clase que inicializa el rango de cálculo
    def __init__(self):
        self.fact = 1  # Variable para almacenar el factorial

    # Método para calcular el factorial de un número
    def calculate(self, num):
        if num < 0:
            print(f"El factorial de {num} no existe, ya que es un número negativo.")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    # Método para calcular los factoriales en un rango [min, max]
    def run(self, min, max):
        if min > max:
            print("El valor mínimo no puede ser mayor que el máximo.")
            return

        # Calcular y mostrar los factoriales en el rango
        for i in range(min, max + 1):
            print(f"El factorial de {i} es: {self.calculate(i)}")


# Función principal que ejecuta el programa
def main():
    import sys

    # Verifica si se pasó un argumento en la línea de comandos
    if len(sys.argv) == 1:
        # Si no se pasa argumento, solicita el rango al usuario
        num_input = input("Debe ingresar un rango para calcular los factoriales (min-max): ")
        # Procesar la entrada
        if '-' in num_input:
            min_value, max_value = num_input.split('-')
            if min_value.isdigit() and max_value.isdigit():
                min_value, max_value = int(min_value), int(max_value)
                factorial_obj = Factorial()  # Crear un objeto de la clase Factorial
                factorial_obj.run(min_value, max_value)
            else:
                print("Por favor, ingrese un rango válido con números enteros.")
        else:
            print("Formato de rango incorrecto. Debe ser en el formato min-max.")
            sys.exit()
    else:
        # Si se pasa un argumento, usa el rango proporcionado
        num_input = sys.argv[1]
        if '-' in num_input:
            min_value, max_value = num_input.split('-')
            if min_value.isdigit() and max_value.isdigit():
                min_value, max_value = int(min_value), int(max_value)
                factorial_obj = Factorial()  # Crear un objeto de la clase Factorial
                factorial_obj.run(min_value, max_value)
            else:
                print("Por favor, ingrese un rango válido con números enteros.")
                sys.exit()
        else:
            print("Formato de rango incorrecto. Debe ser en el formato min-max.")
            sys.exit()


# Llamar a la función principal
if __name__ == "__main__":
    main()