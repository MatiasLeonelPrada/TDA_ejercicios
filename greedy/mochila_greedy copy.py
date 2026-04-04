def ordenar_por_mayor_valor(elementos):
    return sorted(elementos, key=lambda e: e[0], reverse=True)

def ordenar_por_mayor_relacion_valor_peso(elementos):
    return sorted(elementos, key=lambda e: e[0] / e[1], reverse=True)

def mochila_greedy(elementos, W, ordenamiento):
    elementos_ord = ordenamiento(elementos)
    capacidad_usada = 0
    valor_obtenido = 0
    
    for valor, peso in elementos_ord:
        if peso + capacidad_usada <= W:
            capacidad_usada += peso
            valor_obtenido += valor
    return valor_obtenido

def mochila_greedy_mejor(elementos, W):
    por_valor = mochila_greedy(elementos, W, ordenar_por_mayor_valor)
    por_valor_peso = mochila_greedy(elementos, W, ordenar_por_mayor_relacion_valor_peso)
    return max(por_valor, por_valor_peso)

if __name__ == "__main__":
    elementos = [(60, 5), (100, 10), (120, 8)]
    elementos2 = [(100, 100), (1, 1), (50, 10), (70, 5)]
    elementos3 = [(10000, 11), (1, 10)]
    W = 10
    W2 = 110
    # print(mochila_greedy(elementos, W, ordenar_por_mayor_valor))
    # print(mochila_greedy(elementos, W, ordenar_por_menor_peso))
    # print(mochila_greedy(elementos, W, ordenar_por_mayor_relacion_valor_peso))
    # print(mochila_greedy(elementos2, W2, ordenar_por_mayor_relacion_valor_peso))
    # print(mochila_greedy(elementos2, W2, ordenar_por_mayor_valor))
    # print(mochila_greedy_mejor(elementos, W))

    print(mochila_greedy_mejor(elementos2, W2))
    print(mochila_greedy_mejor(elementos3, W))
