from Grafo import Grafo

def es_arbol(g):
    '''
    Devuelve True si el grafo es un árbol, False en caso contrario.
    '''
    visitados = set()
    padre = {}

    for v in g.obtener_vertices():
        if v not in visitados:
            padre[v] = None
            ciclo = dfs_busca_ciclo(g, v, visitados, padre)
            if ciclo:
                return False
            if visitados != set(g.obtener_vertices()):
                return False
    return True

def dfs_busca_ciclo(g, v, visitados, padre):
    visitados.add(v)
    for w in g.obtener_adyacentes(v):
        if w not in visitados:
            padre[w] = v
            resultado = dfs_busca_ciclo(g, w, visitados, padre)
            if resultado:
                return False
        else:
            #Si adyacente fue visitado y no es el padre de v, entonces hay ciclo
            if padre[v] != w:
                return True
    return False
            
if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_arista("A", "B", 1)
    grafo.agregar_arista("B", "C", 1)
    grafo.agregar_arista("C", "D", 1)
    grafo.agregar_arista("D", "A", 1)
    print(es_arbol(grafo))
    grafo2 = Grafo()
    grafo2.agregar_vertice("A")
    grafo2.agregar_vertice("B")
    grafo2.agregar_vertice("C")
    grafo2.agregar_arista("A", "B", 1)
    grafo2.agregar_arista("B", "C", 1)
    print(es_arbol(grafo2))
    grafo3 = Grafo()
    grafo3.agregar_vertice("A")
    grafo3.agregar_vertice("B")
    print(es_arbol(grafo3))