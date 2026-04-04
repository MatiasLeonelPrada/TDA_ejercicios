# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, 
# por encima del cual se rompen. Implementar un algoritmo greedy que, 
# teniendo una lista de pesos de n productos comprados, encuentre la mejor forma 
# de distribuir los productos en la menor cantidad posible de bolsas. 
# Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 
# y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado 
# encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.


def bolsas(capacidad, productos):
    resultado = []
    actual = []
    bolsa = [actual, capacidad]
    productos.sort(reverse=True)
    while len(productos) > 0:
        productos_restantes = productos.copy()
        for producto in productos_restantes:
            if bolsa[1] == 0:
                break
            if producto <= bolsa[1]:
                bolsa[0].append(producto)
                bolsa[1] -= producto
                productos.remove(producto)
        resultado.append(bolsa[0])
        bolsa = [[], capacidad]
        

    return resultado

if __name__ == "__main__":
    capacidad = 5
    capacidad_2 = 10
    productos = [ 4, 2, 1, 3, 5 ]
    productos_2 =  [ 4, 2, 1, 3, 5, 6, 7, 8, 9, 10 ]
    print(bolsas(capacidad, productos))
    print(bolsas(capacidad_2, productos_2))