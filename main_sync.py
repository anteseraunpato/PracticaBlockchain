from nodo_blockchain import NodoBlockchain  # Importa NodoBlockchain desde nodo_blockchain.py


# Crear nodos de blockchain
nodo_1 = NodoBlockchain("Nodo 1")
nodo_2 = NodoBlockchain("Nodo 2")

# Agregar bloques al Nodo 1
nodo_1.blockchain.agregar_bloque("Transacción 1: Juan envió 1 BTC a María")
nodo_1.blockchain.agregar_bloque("Transacción 2: María envió 0.5 BTC a Luis")

# Nodo 2 tiene una cadena más corta
print(f"Cadena Nodo 1: {len(nodo_1.blockchain.cadena)} bloques")
print(f"Cadena Nodo 2: {len(nodo_2.blockchain.cadena)} bloques")

# Sincronizar Nodo 2 con Nodo 1
nodo_2.recibir_cadena(nodo_1.blockchain.cadena)

# Verificar que Nodo 2 se haya actualizado
print(f"Cadena Nodo 2 después de sincronización: {len(nodo_2.blockchain.cadena)} bloques")


