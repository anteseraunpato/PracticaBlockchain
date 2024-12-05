import tkinter as tk
from tkinter import ttk, messagebox
from blockchain import Bloque
from nodo_blockchain import NodoBlockchain

# Crear nodos de blockchain
nodo_1 = NodoBlockchain("Nodo 1")
nodo_2 = NodoBlockchain("Nodo 2")

# Agregar bloques iniciales a Nodo 1
nodo_1.blockchain.agregar_bloque("Transacción 1: Juan envió 1 BTC a María")
nodo_1.blockchain.agregar_bloque("Transacción 2: María envió 0.5 BTC a Luis")

# Funciones para la interfaz gráfica
def mostrar_bloques(nodo, text_widget):
    """Muestra los bloques de un nodo en un widget de texto."""
    text_widget.delete(1.0, tk.END)
    for bloque in nodo.blockchain.cadena:
        text_widget.insert(
            tk.END,
            f"Índice: {bloque.index}\n"
            f"Datos: {bloque.datos}\n"
            f"Hash: {bloque.hash}\n"
            f"Previo Hash: {bloque.previo_hash}\n\n"
        )

def sincronizar_cadenas():
    """Sincroniza la cadena de Nodo 2 con la de Nodo 1."""
    nodo_2.recibir_cadena(nodo_1.blockchain.cadena)
    mostrar_bloques(nodo_1, text_nodo_1)
    mostrar_bloques(nodo_2, text_nodo_2)
    messagebox.showinfo("Sincronización", "Nodo 2 se ha sincronizado con Nodo 1.")

def agregar_bloque_nodo_1():
    """Agrega un nuevo bloque al Nodo 1."""
    datos = entrada_datos.get()
    if datos.strip() == "":
        messagebox.showerror("Error", "Los datos no pueden estar vacíos.")
        return
    nodo_1.blockchain.agregar_bloque(datos)
    mostrar_bloques(nodo_1, text_nodo_1)
    entrada_datos.delete(0, tk.END)

def verificar_integridad_nodo_1():
    """Verifica la integridad de la cadena en Nodo 1."""
    es_valida = nodo_1.blockchain.verificar_integridad()
    if es_valida:
        messagebox.showinfo("Validación", "La cadena de Nodo 1 es válida.")
    else:
        messagebox.showerror("Validación", "La cadena de Nodo 1 está corrupta.")
        

def manipular_nodo_2():
    """Manipula directamente la cadena de Nodo 2, causando una ruptura en su integridad."""
    datos = "Bloque inválido: Manipulación directa"
    ultimo_bloque = nodo_2.blockchain.cadena[-1]
    bloque_invalido = Bloque(
        index=len(nodo_2.blockchain.cadena),
        datos=datos,
        previo_hash="manipulacion_invalida",  # Hash previo falso
        dificultad=nodo_2.blockchain.dificultad,
    )
    nodo_2.blockchain.cadena.append(bloque_invalido)
    mostrar_bloques(nodo_2, text_nodo_2)
    messagebox.showinfo("Manipulación", "Se ha agregado un bloque inválido a Nodo 2.")

def verificar_integridad_nodo_2():
    """Verifica la integridad de la cadena en Nodo 2."""
    es_valida = nodo_2.blockchain.verificar_integridad()
    if es_valida:
        messagebox.showinfo("Validación", "La cadena de Nodo 2 es válida.")
    else:
        messagebox.showerror("Validación", "La cadena de Nodo 2 está corrupta.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Blockchain Descentralizado con Validación")
ventana.geometry("900x700")
ventana.configure(bg="#f5f5f5")

# Estilo con ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Arial", 12), background="#f5f5f5")
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TEntry", font=("Arial", 10))

# Etiqueta y área de texto para Nodo 1
label_nodo_1 = ttk.Label(ventana, text="Nodo 1", font=("Arial", 14, "bold"))
label_nodo_1.pack(pady=5)
text_nodo_1 = tk.Text(ventana, height=12, width=85, bg="#ffffff", fg="#333333", font=("Arial", 10), relief="solid", borderwidth=1)
text_nodo_1.pack(pady=5)

# Entrada de datos para agregar un bloque al Nodo 1
frame_agregar = ttk.Frame(ventana)
frame_agregar.pack(pady=10)

entrada_datos = ttk.Entry(frame_agregar, width=50)
entrada_datos.pack(side=tk.LEFT, padx=5)
boton_agregar = ttk.Button(frame_agregar, text="Agregar Bloque a Nodo 1", command=agregar_bloque_nodo_1)
boton_agregar.pack(side=tk.LEFT)





# Etiqueta y área de texto para Nodo 2
label_nodo_2 = ttk.Label(ventana, text="Nodo 2", font=("Arial", 14, "bold"))
label_nodo_2.pack(pady=5)
text_nodo_2 = tk.Text(ventana, height=12, width=85, bg="#ffffff", fg="#333333", font=("Arial", 10), relief="solid", borderwidth=1)
text_nodo_2.pack(pady=5)

# Botones para sincronización y validación
frame_acciones = ttk.Frame(ventana)
frame_acciones.pack(pady=10)

boton_sincronizar = ttk.Button(frame_acciones, text="Sincronizar Nodo 2 con Nodo 1", command=sincronizar_cadenas)
boton_sincronizar.pack(side=tk.LEFT, padx=5)

boton_validar_nodo_1 = ttk.Button(frame_acciones, text="Verificar integridad Nodo 1", command=verificar_integridad_nodo_1)
boton_validar_nodo_1.pack(side=tk.LEFT, padx=5)

boton_validar_nodo_2 = ttk.Button(frame_acciones, text="Verificar integridad Nodo 2", command=verificar_integridad_nodo_2)
boton_validar_nodo_2.pack(side=tk.LEFT, padx=5)

boton_manipular_nodo_2 = ttk.Button(frame_acciones, text="Manipular Nodo 2", command=manipular_nodo_2)
boton_manipular_nodo_2.pack(side=tk.LEFT, padx=5)


# Mostrar bloques iniciales
mostrar_bloques(nodo_1, text_nodo_1)
mostrar_bloques(nodo_2, text_nodo_2)

# Ejecutar la ventana
ventana.mainloop()
