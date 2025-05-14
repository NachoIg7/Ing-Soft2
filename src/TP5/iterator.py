# Implemente una clase bajo el patrón iterator que almacene una cadena de 
# caracteres y permita recorrerla en sentido directo y reverso.


class StringIterator:
    def __init__(self, text):
        # Constructor que recibe la cadena de texto a iterar
        self.text = text
        self.index = 0  # Posición actual del recorrido

    def __iter__(self):
        # Hace que este objeto sea un iterador válido
        return self

    def __next__(self):
        # Devuelve el próximo carácter en la cadena
        if self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1  # Avanza al siguiente carácter
            return char
        else:
            # Si llegó al final, lanza la excepción para terminar el bucle
            raise StopIteration

    def reset(self):
        # Reinicia la posición para poder recorrer desde el principio otra vez
        self.index = 0

    def reverse_iter(self):
        # Iterador reverso usando un generador (yield)
        for char in reversed(self.text):
            yield char


# =====================
#  Ejemplo de uso
# =====================

# Crear el iterador con la cadena "Nacho"
iterator = StringIterator("Patrones")

# Recorrer en sentido directo
print("Recorrido directo:")
for char in iterator:
    print(char)

# Reiniciar iterador
iterator.reset()

# Recorrer en sentido reverso
print("\nRecorrido reverso:")
for char in iterator.reverse_iter():
    print(char)