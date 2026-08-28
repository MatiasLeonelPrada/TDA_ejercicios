def laberinto(matriz):
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return 0
    if len(matriz) == 1 and len(matriz[0]) == 1:
        return matriz[0][0]
    matriz_sol = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    for i in range(0, len(matriz)):
        matriz_sol[i][0] = matriz_sol[i-1][0] + matriz[i][0]
    
    for j in range(0, len(matriz[0])):
        matriz_sol[0][j] = matriz_sol[0][j-1] + matriz[0][j]

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            if i == 0 or j == 0:
                continue
            matriz_sol[i][j] = max(matriz_sol[i-1][j], matriz_sol[i][j-1]) + matriz[i][j]


    return matriz_sol[len(matriz)-1][len(matriz[0])-1]



if __name__ == "__main__":

    # print(laberinto([[0, 1, 0], [0, 1, 0], [0, 0, 0]]))
    # print(laberinto([[0, 10, 0], [0, 1, 0], [0, 6, 0]]))
    # print(laberinto([[0, 10, 0, 1], [0, 1, 0, 8], [0, 6, 100, 0], [0, 0, 0, 0]]))
    print(laberinto([[10, 20]]))

