from Grafo import Grafo

def a_n_aristas(grafo, v, n):
    # 'Implementar un algoritmo que reciba un grafo dirigido, un vértice V y un número N, 
    # y devuelva una lista con todos los vértices que se encuentren a exactamente N aristas 
    # de distancia del vértice V. Indicar el tipo de recorrido utilizado y el orden del algoritmo. Justificar.
    visitados = set()
    resultado = []
    cola = [v]
    padres = {v: None}
    orden = {v: 0}
    visitados.add(v)
    while len(cola) > 0:
        actual = cola.pop(0)
        for adyacente in grafo.obtener_adyacentes(actual):
            if adyacente not in visitados:
                visitados.add(adyacente)
                padres[adyacente] = actual
                orden[adyacente] = orden[actual] + 1
                if orden[adyacente] == n:
                    resultado.append(adyacente)
                cola.append(adyacente)
    if orden[v] == n:
        resultado.append(v)
    return resultado

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    grafo = Grafo(dirigido=True)
    grafo2 = Grafo(vertices=['A', 'B'],dirigido=True)
    for vertice in vertices:
        grafo.agregar_vertice(vertice)
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'D')
    grafo.agregar_arista('A', 'E')
    grafo.agregar_arista('B', 'C')
    grafo.agregar_arista('D', 'E')
    print(a_n_aristas(grafo, 'A', 1)) # Debería imprimir ['B', 'D', 'E']
    print(a_n_aristas(grafo, 'A', 2)) # Debería imprimir ['C']
    print(a_n_aristas(grafo2, 'A', 1)) # Debería imprimir []
    print(a_n_aristas(grafo2, 'A', 0)) # Debería imprimir ['A']
    print(a_n_aristas(grafo2, 'B', 0)) # Debería imprimir ['B']

