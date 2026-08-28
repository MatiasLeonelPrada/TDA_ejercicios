def bodegon_dinamico(P, W):
    n = len(P)
    # Crear una tabla para almacenar los resultados de subproblemas
    MATRIX = [[0 for j in range(W + 1)] for i in range(n + 1)]
    for i in range(1, n+1):
        personas = P[i-1]
        for lugares in range(W+1):
            if lugares >= personas:
                MATRIX[i][lugares] = max(MATRIX[i-1][lugares], MATRIX[i-1][lugares-personas]+personas)
            else:
                MATRIX[i][lugares] = MATRIX[i-1][lugares]
    return reconstruir_solucion(MATRIX, P, W)

def reconstruir_solucion(MATRIX, P, W):
    solucion = []
    i = len(P)
    j = W
    for i in range(len(P), 0, -1):
        if MATRIX[i][j] != MATRIX[i-1][j]:
            solucion.append(P[i-1])  # Agregar el VALOR grupo de personas incluido a la solución
            j -= P[i-1]  # Reducir el VALOR restante por el peso del objeto incluido
        
    solucion.reverse()
    return solucion

if __name__ == "__main__":
    P = [10, 7, 5, 13]
    W = 16
    print(bodegon_dinamico(P, W)) # Debería devolver [0, 2] o [2, 0] (tomar los objetos 0 y 2 da una ganancia de 15 sin superar el peso máximo)
    P = [2, 3, 6, 5]
    W = 6
    print(bodegon_dinamico(P, W)) # Debería devolver [1, 0] o [0, 1] (tomar los objetos 0 y 1 da una ganancia de 5 sin superar el peso máximo)
    P = [6]
    W = 7
    print(bodegon_dinamico(P, W)) 
    P = [5, 6]
    W = 12
    print(bodegon_dinamico(P, W))