def cambio(monedas, monto):
    cant = [0] * (monto + 1)
    for monto_actual in range(1, monto + 1):
        min = monto_actual
        for moneda in monedas:
            if moneda > monto_actual: continue
            cantidad = 1 + cant[monto_actual - moneda]
            if cantidad < min:
                min = cantidad
        cant[monto_actual] = min
    return reconstruir_camino(monedas, monto, cant)

def reconstruir_camino(monedas, monto, cant):
    solucion = []
    monto_restante = monto
    while monto_restante > 0:
        for moneda in monedas:
            if moneda > monto_restante: continue
            if cant[monto_restante] == 1 + cant[monto_restante - moneda]:
                solucion.append(moneda)
                monto_restante -= moneda
    return solucion



if __name__ == "__main__":
    # print(cambio([1, 3, 4], 6))  # debería imprimir 2 (2 monedas de 3)
    # print(cambio([1, 3, 4], 7))  # debería imprimir 2 (1 moneda de 3 y 1 moneda de 4)
    # print(cambio([1, 3, 4], 8))  # debería imprimir 2 (2 monedas de 4)
    # print(cambio([1, 3, 4], 9))  # debería imprimir 3 (3 monedas de 3)
    # print(cambio([1, 3, 4], 10)) # debería imprimir 3 (2 monedas de 3 y 1 moneda de 4)
    # print(cambio([1, 3, 4], 11)) # debería imprimir 3 (1 moneda de 3 y 2 monedas de 4)
    # print(cambio([1, 3, 4], 12)) # debería imprimir 3 (3 monedas de 4)
    # print(cambio([1, 3, 4], 13)) # debería imprimir 4 (1 moneda de 1 y 3 monedas de 4)
    # print(cambio([1, 3, 4], 14)) # debería imprimir 4 (2 monedas de 3 y 2 monedas de 4)

    print(cambio([1, 6, 5, 10], 11)) # debería imprimir 2 (1 moneda de 6 y 1 moneda de 5)

