def sumatorias_n_rec(lista, n, sol_parcial, resultado, num_actual):
    if num_actual == len(lista):
        if sol_parcial and sum(sol_parcial) == n:
            return sol_parcial
        return None

    if sol_parcial and sum(sol_parcial) == n:
        return sol_parcial
    
    if sum(sol_parcial) > n:
        return None

    
    sol_parcial.append(lista[num_actual])
    res_actual = sumatorias_n_rec(lista, n, sol_parcial, resultado, num_actual + 1)
    if res_actual is not None:
        resultado.append(res_actual.copy())
    sol_parcial.remove(lista[num_actual])
    return sumatorias_n_rec(lista, n, sol_parcial, resultado, num_actual + 1)

def sumatorias_n(lista, n):
    if n == 0:
        return [[]]
    resultado = []
    sumatorias_n_rec(lista, n, [], resultado, 0)
    return resultado



if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 8, 9]
    n = 12
    lista.sort() # Ordenamos la lista para evitar combinaciones repetidas
    print(sumatorias_n(lista, n)) # Debería devolver 

    # lista2 = [1, 2, 3]
    # n2 = 14
    # print(sumatorias_n(lista2, n2)) # Debería devolver []

    # lista3 = [1, 2, 3]
    # n3 = 7
    # print(sumatorias_n(lista3, n3)) # Debería devolver []

    # lista4 = [1, 2, 3]
    # n4 = 6
    # print(sumatorias_n(lista4, n4)) # Debería devolver [[1, 2, 3]]