def parte_entera_raiz(n):
    if n < 2:
        return n
    
    inicio = 0
    fin = n // 2 + 1

    res = buscar_parte_entera_rec(inicio, fin, n)
    return res

def buscar_parte_entera_rec(inicio, fin, n):
    if inicio >= fin:
        return inicio - 1
    medio = (inicio + fin) // 2
    if (medio ** 2 <= n):
        return buscar_parte_entera_rec(medio + 1, fin, n)
    else:
        return buscar_parte_entera_rec(inicio, medio, n)

if __name__ == "__main__":
    print(parte_entera_raiz(16)) # Debería imprimir 4
    print(parte_entera_raiz(15)) # Debería imprimir 3
    print(parte_entera_raiz(1)) # Debería imprimir 1
    print(parte_entera_raiz(0)) # Debería imprimir 0
    print(parte_entera_raiz(9999999999)) # Debería imprimir 1000