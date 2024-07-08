from collections import deque

def encontrar_camino_optimo(laberinto, entrada, salida):
    def es_valido(x, y):  #función para saber si la posición es correcta, es decir si está dentro de los límites y no es una pared
        return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0

    # Los movimientos posibles son: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Inicializacion de la cola y el conjunto de celdas o puntos visitados
    cola = deque([(entrada, [entrada])])
    visitados = set()
    visitados.add(entrada)
    
    while cola:
        (x, y), camino = cola.popleft()  #Eliminar y obtener el primero
        
        if (x, y) == salida:
            return camino
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny) and (nx, ny) not in visitados:
                visitados.add((nx, ny))
                cola.append(((nx, ny), camino + [(nx, ny)]))
    
    return None  # Para si no hay camino

# Ejemplo de uso
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
entrada = (0, 0)
salida = (4, 4)

camino_optimo = encontrar_camino_optimo(laberinto, entrada, salida)
print(camino_optimo)
