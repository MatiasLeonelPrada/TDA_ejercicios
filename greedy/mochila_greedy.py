IDX_VALOR = 0
IDX_PESO = 1


def ordenar_por_mayor_valor(elementos):
    return sorted(elementos, key=lambda e: e[IDX_VALOR], reverse=True)


def ordenar_por_menor_peso(elementos):
    return sorted(elementos, key=lambda e: e[IDX_PESO])


def ordenar_por_mayor_relacion_valor_peso(elementos):
    return sorted(elementos, key=lambda e: e[IDX_VALOR]/e[IDX_PESO], reverse=True)


def mochila_greedy(elementos, W, ordenamiento):
    elementos_ord = ordenamiento(elementos)
    print(elementos_ord)
    capacidad_usada = 0
    valor_obtenido = 0
    for elem in elementos_ord:
        if elem[IDX_PESO] + capacidad_usada > W:
            continue
        capacidad_usada += elem[IDX_PESO]
        valor_obtenido += elem[IDX_VALOR]
    return valor_obtenido

if __name__ == "__main__":
    elementos = [(60, 5), (100, 10), (120, 8)]
    elementos2 = [(100, 100), (1, 1), (50, 10), (70, 5)]
    W = 10
    W2 = 110
    # print(mochila_greedy(elementos, W, ordenar_por_mayor_valor))
    # print(mochila_greedy(elementos, W, ordenar_por_menor_peso))
    # print(mochila_greedy(elementos, W, ordenar_por_mayor_relacion_valor_peso))
    print(mochila_greedy(elementos2, W2, ordenar_por_mayor_relacion_valor_peso))
    print(mochila_greedy(elementos2, W2, ordenar_por_mayor_valor))
