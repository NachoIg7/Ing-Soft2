# Provea una clase ping que luego de creada al ser invocada con un método 
# “execute(string)” realice 10 intentos de ping a la dirección IP contenida en 
# “string” (argumento pasado), la clase solo debe funcionar si la dirección IP 
# provista comienza con “192.”. Provea un método executefree(string) que haga 
# lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy 
# cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a 
# www.google.com usando el método executefree de ping y re-envie a execute 
# de la clase ping en cualquier otro caso. (Modele la solución como un patrón 
# proxy). 

import os

class Ping:
    def execute(self, ip_address):
        if not ip_address.startswith("192."):
            print (f"Direccion IP no permitida: {ip_address}")
            return
            print (f"Haciendo ping a {ip_address} (10 intentos)...")
            os.system(f"ping -n 10 {ip_address}")
    
    def executefree(self, ip_address):
        print (f"Haciendo ping a {ip_address} (10 intentos)...")
        os.system(f"ping -n 10 {ip_address}")

class Pingproxy:
    def __init__(self):
        self.ping = Ping()
    
    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            print ("Interceptando: Redirigiendo a www.google.com usando ejecuteFree")
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)


# Ejemplo de uso
if __name__ == "__main__":
    proxy = Pingproxy()
    ips = [
        "192.168.1.1", 
        "192.168.0.254", 
        "10.0.0.1", 
        "192.0.0.1", 
        "8.8.8.8"
    ]

    for ip in ips:
        proxy.execute(ip)