def operaciones(k):
    cant_operaciones = [None] * (k + 1)
    cant_operaciones[0] = 0
    if k >= 1:
        cant_operaciones[1] = 1
    if k >= 2:
        cant_operaciones[2] = 2
    for i in range(3, k + 1):
        if (i % 2) == 0:
            cant_operaciones[i] = min(cant_operaciones[i // 2], cant_operaciones[i - 1]) + 1
        else:
            cant_operaciones[i] = cant_operaciones[i - 1] + 1

    min_operaciones = cant_operaciones[k]
    return obtener_operaciones(cant_operaciones, k, min_operaciones)

def obtener_operaciones(cant_operaciones, k, min_operaciones):
    resultado = []
    i = k
    while i > 0:
        if cant_operaciones[i] == min_operaciones:
            if (i % 2) == 0:
                min_operaciones -= 1
                i = i // 2
                resultado.append('por2')
            else:
                min_operaciones -= 1
                i = i - 1
                resultado.append('mas1')
    return(list(reversed(resultado)))

if __name__ == "__main__":
    # print(operaciones(1))  # Debería imprimir 1
    # print(operaciones(2))  # Debería imprimir 2
    # print(operaciones(3))  # Debería imprimir 3
    # print(operaciones(4))  # Debería imprimir 3
    # print(operaciones(5))  # Debería imprimir 4
    print(operaciones(10)) # Debería imprimir 5
    print(operaciones(20)) # Debería imprimir 6 
    # print(operaciones(8)) # Debería imprimir 4