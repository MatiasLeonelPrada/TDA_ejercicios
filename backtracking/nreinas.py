def es_valida(tablero, fila, columna):
    # Verificar la columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verificar la diagonal superior izquierda
    for i in range(fila, -1, -1):
        if tablero[i][columna] == 1:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, len(tablero))):
        if tablero[i][j] == 1:
            return False

    return True

def nreinas(n):
    if n <= 0:
        return []
    if n == 1:
        return [(0, 0)]
    if n == 2 or n == 3:
        return []
    return [(0, 0)]