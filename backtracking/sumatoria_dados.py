def sumatoria_dados_rec(n, s, cant_restante, sol_parcial, resultados, num_actual):
    if cant_restante == 0 and sum(sol_parcial) == s:
        resultados.append(sol_parcial.copy())
        return resultados
    
    if cant_restante == 0 or sum(sol_parcial) > s:
        return resultados
    
    if sum(sol_parcial) + cant_restante * 1 > s:
        return resultados
    if sum(sol_parcial) + cant_restante * 6 < s:
        return resultados

    for i in range(1, 7):
        if cant_restante > 0 and sum(sol_parcial) + i <= s:
            sol_parcial.append(i)
            sumatoria_dados_rec(n, s, cant_restante - 1, sol_parcial, resultados, i)
            sol_parcial.pop()

    return resultados

def sumatoria_dados(n, s):
    if n == 0:
        return []
    resultado = []
    sol_parcial = []
    sumatoria_dados_rec(n, s, n, sol_parcial, resultado, 1)
    return resultado


if __name__ == "__main__":
    s = 7
    n = 2
    print(sumatoria_dados(n, s)) # Debería devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]

    # s2 = 14
    # n2 = 2
    # print(sumatoria_dados(n2, s2)) # Debería devolver []

    # s3 = 7
    # n3 = 7
    # print(sumatoria_dados(n3, s)) # Debería devolver []

    # s4 = 6
    # n4 = 3
    # print(sumatoria_dados(n4, s)) # Debería devolver [[1, 2, 3]]