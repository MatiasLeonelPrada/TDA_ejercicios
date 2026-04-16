def scheduling(charlas):
    # Ordenar las charlas por hora de finalización
    cant_charlas = len(charlas)
    charlas.sort(key=lambda x: x[1])
    charlas.insert(0, (0, 0, 0))  # Agregar una charla ficticia al inicio para facilitar el manejo de índices
    print(charlas)
    resultado = [0] * (cant_charlas + 1)
    resultado[0] = 0  # No se obtiene ganancia si no se asiste a ninguna charla
    print(resultado)
    superposiciones = crear_superposiciones(charlas, cant_charlas)

    for i in range(1, cant_charlas + 1):
        resultado[i] = max(resultado[i-1], resultado[superposiciones[i]] + charlas[i][2])
    return []

def crear_superposiciones(charlas, cant_charlas):
    superposiciones = [None] * (cant_charlas+1)
    superposiciones[0] = 0
    for i in range(1, cant_charlas + 1):
        superposiciones[i] = 0
        for j in range(i, -1, -1):
            if charlas[j][1] <= charlas[i][0]:  # Si la charla j termina antes de que comience la charla i
                superposiciones[i] = j  # Guardar el índice de la charla j que no se superpone con la charla i
                break
    return superposiciones

    

if __name__ == "__main__":
    # print(scheduling([(9, 11, 20), (5, 8, 15)])) 
    # print(scheduling([(9, 11, 20), (5, 8, 15), (8, 10, 10)])) 
    print(scheduling([(9, 11, 20), (5, 8, 15), (8, 10, 10), (11, 12, 5), (10, 11, 8)])) 