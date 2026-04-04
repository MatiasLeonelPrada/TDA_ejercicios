from Grafo import Grafo

def componente_bipartita(grafo, v, visitados, grupo):
    visitados.add(v)
    for adyacente in grafo.obtener_adyacentes(v):
        if adyacente in visitados:
            if grupo[adyacente] == grupo[v]:
                return False
        else:
            grupo[adyacente] = 1 - grupo[v]
            if not componente_bipartita(grafo, adyacente, visitados, grupo):
                return False
    return True

def es_bipartito(grafo):
    visitados = set()
    grupo = {}
    for vertice in grafo.obtener_vertices():
        if vertice not in visitados:
            grupo[vertice] = 0
            if not componente_bipartita(grafo, vertice, visitados, grupo):
                return False
    return True
    

if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "A")
    grafo.agregar_arista("A", "C")
    print(es_bipartito(grafo)) # Debería imprimir False, ya que el ciclo A-C-D-A tiene longitud impar, lo que impide que el grafo sea bipartito.
    grafo2 = Grafo()
    grafo2.agregar_vertice("A")
    grafo2.agregar_vertice("B")
    grafo2.agregar_vertice("C")
    grafo2.agregar_arista("A", "B")
    grafo2.agregar_arista("B", "C")
    print(es_bipartito(grafo2)) # Debería imprimir True, ya que el grafo es un camino A-B-C, de longitud par, lo que permite que sea bipartito.