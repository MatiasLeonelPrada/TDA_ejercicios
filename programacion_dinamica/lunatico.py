def obtener_indices_ganancias(pagas_del_dia, ganancias):
    # Se agrega un 0 al inicio para evitar problemas de índices negativos
    paga = [0] + pagas_del_dia
    ganancias_ext = [0] + ganancias
    
    dias = []
    i = len(paga) - 1
    
    #Itero a lo sumo pagas veces
    for _ in range(len(paga)):
        if i <= 0:
            break
        # Verificar si se seleccionó el día i
        elif i == 1 and paga[1] == ganancias_ext[1]:
            # verificar si se seleccionó solo arr[0]
            dias.append(0)
            break
        elif i >= 2 and paga[i] == paga[i-2] + ganancias_ext[i]:
            dias.append(i - 1)  # -1 porque extendimos con 0 al inicio
            i -= 2
        else:
            i -= 1
    
    return list(reversed(dias))


def lunatico_el_vago(trabajos):
    if len(trabajos) == 0:
        return []
    if len(trabajos) == 1:
        return [0]
    if len(trabajos) == 2:
        return [0] if trabajos[0] >= trabajos[1] else [1]
    
    n = len(trabajos)
    paga_del_dia = [None] * n 
    paga_del_dia[0] = trabajos[0]
    paga_del_dia[1] = max(trabajos[0], trabajos[1])
    
    for i in range(2, n):
        paga_del_dia[i] = max(paga_del_dia[i-1], paga_del_dia[i-2] + trabajos[i])
    
    return obtener_indices_ganancias(paga_del_dia, trabajos)


def lunatico(ganancias):
    #resolver dos casos - sin último día y sin primer día
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [0]
    if len(ganancias) == 2:
        return [0] if ganancias[0] >= ganancias[1] else [1]
    
    # Caso 1: resolver sin el último día (ganancias[0:n-1])
    resultado1 = lunatico_el_vago(ganancias[:-1])
    paga1 = sum(ganancias[i] for i in resultado1) if resultado1 else 0
    
    # Caso 2: resolver sin el primer día (ganancias[1:n])
    resultado2_relativo = lunatico_el_vago(ganancias[1:])
    # sumar 1 a cada índice para obtener los índices relativos al arreglo original
    resultado2 = [i + 1 for i in resultado2_relativo] if resultado2_relativo else []
    paga2 = sum(ganancias[i] for i in resultado2) if resultado2 else 0
    
    # Retornar la solución con mayor paga
    if paga1 >= paga2:
        return resultado1
    else:
        return resultado2


if __name__ == "__main__":
    print(lunatico([]))  # debería imprimir []
    print(lunatico([100]))  # debería imprimir [0]
    print(lunatico([100, 5]))  # debería imprimir [0]
    print(lunatico([100, 5, 50]))  # debería imprimir [0]
    print(lunatico([100, 5, 50, 1]))  # debería imprimir [0, 2]
    print(lunatico([100, 5, 50, 1, 1, 200]))  # debería imprimir [2, 5]
    print(lunatico([100, 5, 50, 1, 1, 200, 300]))  # debería imprimir [2, 4, 6]
    print(lunatico([100, 5, 50, 1, 1, 200, 300, 400]))  # debería imprimir [2, 5, 7]
    print(lunatico([10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]))  # debería imprimir [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]