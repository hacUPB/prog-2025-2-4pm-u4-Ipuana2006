
'''
# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)
# coordenada[0] = 43.9 ERROR porque la tupla es inmutable.
print(coordenada)

# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242

# Indexación (similar a las listas)
print(coordenada[0])  # 33.9425
print(avion_info[-1])  # 242 (pasajeros)

# Slicing
print(avion_info[0:2])  # ("Boeing 787", "Dreamliner")

# Desempaquetado de tuplas
fabricante, modelo, año, capacidad = avion_info
print(f"El {fabricante} {modelo} se lanzó en {año}")

# Desempaquetado con *
lat, lon = coordenada
print(f"Latitud: {lat}, Longitud: {lon}")
'''
listas_detuplas = [(0,0),(3,5),(8,3)]
print(listas_detuplas)
listas_detuplas.append((45,6))
print(listas_detuplas)
listas_detuplas[0] = (1,1)
print(listas_detuplas)
listas_detuplas[2] = "palabra"
print(listas_detuplas)

tupla_delistas = ([2,4,3],[9,6,12])
tupla_delistas[1][0] = 18
print(tupla_delistas)

numeros = (2,34,56,12,4)
if 12 in numeros:
    print("El 12 esta en la lista")
else:
    print("Valor no encontrado")
