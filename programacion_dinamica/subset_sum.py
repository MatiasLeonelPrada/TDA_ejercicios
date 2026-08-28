def subset_sum(elementos, v):
    n = len(elementos)
    # Crear una tabla para almacenar los resultados de subproblemas
    MATRIX = [[0 for j in range(v + 1)] for i in range(n + 1)]
    for i in range(1, n+1):
        elemento = elementos[i-1]
        for lugar in range(v+1):
            if lugar >= elemento:
                MATRIX[i][lugar] = max(MATRIX[i-1][lugar], MATRIX[i-1][lugar-elemento]+elemento)
            else:
                MATRIX[i][lugar] = MATRIX[i-1][lugar]
    return reconstruir_solucion(MATRIX, elementos, v)

def reconstruir_solucion(MATRIX, elementos, v):
    solucion = []
    i = len(elementos)
    j = v
    for i in range(len(elementos), 0, -1):
        if MATRIX[i][j] != MATRIX[i-1][j]:
            solucion.append(elementos[i-1])
            j -= elementos[i-1]

    solucion.reverse()
    return solucion

if __name__ == "__main__":
    P = [10, 7, 5, 13]
    W = 16
    print(subset_sum(P, W)) # Debería devolver [0, 2] o [2, 0] (tomar los objetos 0 y 2 da una ganancia de 15 sin superar el peso máximo)
    P = [2, 3, 6, 5]
    W = 6
    print(subset_sum(P, W)) # Debería devolver [1, 0] o [0, 1] (tomar los objetos 0 y 1 da una ganancia de 5 sin superar el peso máximo)
    P = [6]
    W = 7
    print(subset_sum(P, W)) 
    P = [5, 6]
    W = 12
    print(subset_sum(P, W))