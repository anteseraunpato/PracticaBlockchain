import hashlib

class Bloque:
    def __init__(self, index, datos, previo_hash, dificultad):
        self.index = index
        self.datos = datos
        self.previo_hash = previo_hash
        self.nonce = 0
        self.hash, self.nonce = self.prueba_de_trabajo(dificultad)

    def generar_hash(self, nonce):
        contenido = f"{self.index}{self.datos}{self.previo_hash}{nonce}"
        return hashlib.sha256(contenido.encode()).hexdigest()

    def prueba_de_trabajo(self, dificultad):
        nonce = 0
        while True:
            hash_temp = self.generar_hash(nonce)
            if hash_temp[:dificultad] == "0" * dificultad:
                return hash_temp, nonce
            nonce += 1
            
    


class Blockchain:
    def __init__(self, dificultad=2):
        self.cadena = []
        self.dificultad = dificultad
        self.crear_bloque_inicial()

    def crear_bloque_inicial(self):
        bloque_inicial = Bloque(0, "Bloque inicial", "0", self.dificultad)
        self.cadena.append(bloque_inicial)

    def agregar_bloque(self, datos):
        previo_bloque = self.cadena[-1]
        nuevo_bloque = Bloque(len(self.cadena), datos, previo_bloque.hash, self.dificultad)
        self.cadena.append(nuevo_bloque)

    def verificar_integridad(self):
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_prev = self.cadena[i - 1]
            if bloque_actual.previo_hash != bloque_prev.hash:
                return False
        return True

# Crear una instancia de la blockchain y agregar bloques
mi_blockchain = Blockchain()
mi_blockchain.agregar_bloque("Transacción 1: Juan envió 5 BTC a María")
mi_blockchain.agregar_bloque("Transacción 2: María envió 2 BTC a Luis")

# Imprimir los bloques y verificar la integridad
for bloque in mi_blockchain.cadena:
    print(f"Índice: {bloque.index}, Datos: {bloque.datos}, Hash: {bloque.hash}")

print(f"¿La cadena es válida? {mi_blockchain.verificar_integridad()}")

