def mochila(elementos, W):
    n = len(elementos)
    # Crear una tabla para almacenar los resultados de subproblemas
    MATRIX = [[0 for j in range(W + 1)] for i in range(n + 1)]
    for i in range(1, n+1):
        valor, peso = elementos[i-1]
        for lugares in range(W+1):
            if lugares >= peso:
                MATRIX[i][lugares] = max(MATRIX[i-1][lugares], MATRIX[i-1][lugares-peso]+valor)
            else:
                MATRIX[i][lugares] = MATRIX[i-1][lugares]
    return reconstruir_solucion(MATRIX, elementos, W)

def reconstruir_solucion(MATRIX, elementos, W):
    solucion = []
    i = len(elementos)
    j = W
    for i in range(len(elementos), 0, -1):
        if MATRIX[i][j] != MATRIX[i-1][j]:
            solucion.append(elementos[i-1])  # Agregar el elemento incluido a la solución (i-1)
            j -= elementos[i-1][1]  # Reducir el valor restante por el peso del elemento incluido
        
    solucion.reverse()
    return solucion

if __name__ == "__main__":
    elementos = [(10, 10), (7, 7), (10, 5), (13, 13)]
    W = 16
    print(mochila(elementos, W)) # Debería devolver [0, 2]
    elementos = [(2, 2), (3, 3), (6, 6), (5, 5)]
    W = 6
    print(mochila(elementos, W)) # Debería devolver [1, 0] o [0, 1] (tomar los objetos 0 y 1 da una ganancia de 5 sin superar el peso máximo)
    elementos = [(6, 6)]
    W = 7
    print(mochila(elementos, W)) 
    elementos = [(5, 5), (6, 6)]
    W = 12
    print(mochila(elementos, W))