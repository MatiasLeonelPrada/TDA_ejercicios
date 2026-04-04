from Grafo import Grafo


if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_arista("A", "B", 1)
    grafo.agregar_arista("B", "C", 1)
    grafo

def es_conexo(grafo):
    visitados = set()

    for v in grafo.obtener_vertices():
        if v not in visitados:
            dfs(grafo, v, visitados)
        if visitados != set(grafo.obtener_vertices()):
            return False
    return True

def dfs(g, v, visitados):
    visitados.add(v)
    for w in g.obtener_adyacentes(v):
        if w not in visitados:
            dfs(g, w, visitados)
