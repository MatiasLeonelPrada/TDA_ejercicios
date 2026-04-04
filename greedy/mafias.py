# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    resultado = []
    pedidos_sorted = sorted(pedidos, key=lambda x: x[1])
    if len(pedidos_sorted) == 0:
        return resultado
    resultado.append(pedidos_sorted[0])
    for pedido in pedidos_sorted:
        if pedido[0] >= resultado[-1][1]:
            resultado.append(pedido)
    return resultado


if __name__ == "__main__":
    pedidos = [(0, 5), (1, 4), (2, 6), (7, 10), (8, 9)]
    pedidos_2 = [(0, 3), (1, 2), (4, 6), (5, 7), (8, 10)]
    pedidos_3 = [(0, 2), (1, 3), (4, 5), (6, 8), (7, 9)]    
    print(asignar_mafias(pedidos))
    print(asignar_mafias(pedidos_2))
    print(asignar_mafias(pedidos_3))