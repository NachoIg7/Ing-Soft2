# Modifique el programa IS2_taller_memory.py para que la clase tenga la 
# capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar los 
# mismos en cualquier orden de ser necesario. El método undo deberá tener un 
# argumento adicional indicando si se desea recuperar el inmediato anterior (0) y 
# los anteriores a el (1,2,3).

import os

#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo mejorado
#*-------------------------------------------------------------------

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def __init__(self):
        self.mementos = []  # lista para guardar los estados

    def save(self, writer):
        # Guarda un nuevo estado
        if len(self.mementos) >= 4:
            self.mementos.pop(0)  # Si hay más de 4, elimina el más viejo
        self.mementos.append(writer.save())

    def undo(self, writer, index):
        if index < 0 or index >= len(self.mementos):
            print(f"Índice {index} inválido. Estados guardados: {len(self.mementos)}")
        else:
            writer.undo(self.mementos[index])


if __name__ == '__main__':
    
    print("Crea un objeto que gestionará las versiones anteriores")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("\nSe graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Y un extra más para completar los 4 estados\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional IV (este eliminará el primero)")
    writer.write("Sobreescribiendo el más viejo\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se muestran los estados guardados disponibles:")
    for i, m in enumerate(caretaker.mementos):
        print(f"[{i}] {m.content}")

    print("\nElige qué estado recuperar (0 a 3): ")
    opcion = int(input())

    print(f"\nRecuperando estado {opcion}...")
    caretaker.undo(writer, opcion)

    print("Contenido actual del archivo simulado:")
    print(writer.content + "\n")