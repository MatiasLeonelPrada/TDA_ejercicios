def juan_el_vago(trabajos):
    # devolver un arreglo de los índices de días a trabajar
    if len(trabajos) == 0:
        return []
    if len(trabajos) == 1:
        return [0]
    if len(trabajos) == 2:
        return [0] if trabajos[0] >= trabajos[1] else [1]
    if len(trabajos) == 3:
        return [0, 2] if trabajos[0] + trabajos[2] >= trabajos[1] else [1]
    n = len(trabajos)
    paga_del_dia = [None] * (n) 
    paga_del_dia[0] = trabajos[0]
    paga_del_dia[1] = trabajos[1]
    paga_del_dia[2] = trabajos[0] + trabajos[2]
    for i in range(3, n):
        paga_del_dia[i] = max(paga_del_dia[i-2], paga_del_dia[i-3]) + trabajos[i]
 
    return(obtener_indices_trabajos(paga_del_dia, trabajos, n, max(paga_del_dia[i], paga_del_dia[i-1])))
    #return max(paga_del_dia[i], paga_del_dia[i-1])

def obtener_indices_trabajos(pagas_del_dia, trabajos, n, max_paga):
    dias = []

    for i in range(n-1, -1, -1):
        if pagas_del_dia[i] == max_paga:
            dias.append(i)
            max_paga -= trabajos[i]
    return(list(reversed(dias)))


if __name__ == "__main__":
    print(juan_el_vago([]))  # debería imprimir []
    print(juan_el_vago([100]))  # debería imprimir [0]
    print(juan_el_vago([100, 5]))  # debería imprimir [0]
    print(juan_el_vago([100, 5, 50]))  # debería imprimir [0, 2]
    print(juan_el_vago([100, 5, 50, 1]))  # debería imprimir [0, 2]
    print(juan_el_vago([100, 5, 50, 1, 1, 200]))  # debería imprimir [0, 2, 5]
    print(juan_el_vago([100, 5, 50, 1, 1, 200, 300]))  # debería imprimir [0, 2, 4, 6]
    print(juan_el_vago([100, 5, 50, 1, 1, 200, 300, 400]))  # debería imprimir [0, 2, 5, 7]
    