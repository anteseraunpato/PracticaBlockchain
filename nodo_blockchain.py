from blockchain import Blockchain  # Importa la clase Blockchain desde blockchain.py


class NodoBlockchain:
    def __init__(self, nombre):
        self.nombre = nombre
        self.blockchain = Blockchain(dificultad=2)  # Cada nodo tiene su propia blockchain

    def recibir_cadena(self, nueva_cadena):
        """
        Recibe una cadena de otro nodo y verifica si es válida.
        Si es más larga y válida, reemplaza la cadena actual.
        """
        if len(nueva_cadena) > len(self.blockchain.cadena) and self.es_cadena_valida(nueva_cadena):
            self.blockchain.cadena = nueva_cadena
            print(f"{self.nombre}: Cadena sincronizada con nueva cadena más larga.")
        else:
            print(f"{self.nombre}: Cadena recibida no es válida o no es más larga.")

    def es_cadena_valida(self, cadena):
        """
        Verifica si una cadena externa es válida.
        """
        for i in range(1, len(cadena)):
            bloque_actual = cadena[i]
            bloque_prev = cadena[i - 1]
            # Verificar el hash previo
            if bloque_actual.previo_hash != bloque_prev.hash:
                return False
            # Verificar la prueba de trabajo
            if not bloque_actual.hash.startswith("0" * self.blockchain.dificultad):
                return False
        return True
    
    
