# Modifique el programa IS2_taller_scanner.py para que además la secuencia de 
# barrido de radios que tiene incluya la sintonía de una serie de frecuencias 
# memorizadas tanto de AM como de FM. Las frecuencias estarán etiquetadas 
# como M1, M2, M3 y M4. Cada memoria podrá corresponder a una radio de AM 
# o de FM en sus respectivas frecuencias específicas. En cada ciclo de barrido se 
# barrerán las cuatro memorias.

import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state con memorias
#*--------------------------------------------------------------------

# State base class
class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

# Implementa cómo barrer las estaciones de AM
class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
        self.memory_pos = 0

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan(self):
        super().scan()
        self.scan_memories()

    def scan_memories(self):
        print("Sintonizando memorias:")
        for label, (band, freq) in self.radio.memories.items():
            if band == "AM":
                print(f" - Memoria {label}: {freq} {band}")

# Implementa cómo barrer las estaciones de FM
class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"
        self.memory_pos = 0

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan(self):
        super().scan()
        self.scan_memories()

    def scan_memories(self):
        print("Sintonizando memorias:")
        for label, (band, freq) in self.radio.memories.items():
            if band == "FM":
                print(f" - Memoria {label}: {freq} {band}")

# Construye la radio con todas sus formas de sintonía
class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate  # Inicialmente en FM

        # Definir memorias con etiqueta y (banda, frecuencia)
        self.memories = {
            "M1": ("AM", "1250"),
            "M2": ("FM", "89.1"),
            "M3": ("AM", "1380"),
            "M4": ("FM", "103.9")
        }

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


#---------------------
if __name__ == "__main__":
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()