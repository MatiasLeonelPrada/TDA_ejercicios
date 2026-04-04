from Grafo import Grafo

def encontrar_ciclo(g):
    '''
    Devuelve una lista de vertices que conforman el ciclo. En el segundo ejemplo, 
    debería devolver [A, B, C] (o [B, C, A], etc...). 
    Si no hay ciclo, debe devolver None. 
    '''
    visitados = set()
    padre = {}

    for v in g.obtener_vertices():
        if v not in visitados:
            padre[v] = None
            ciclo = dfs_busca_ciclo(g, v, visitados, padre)
            if ciclo:
                return ciclo
    return None

def dfs_busca_ciclo(g, v, visitados, padre):
    visitados.add(v)
    for w in g.obtener_adyacentes(v):
        if w not in visitados:
            padre[w] = v
            resultado = dfs_busca_ciclo(g, w, visitados, padre)
            if resultado:
                return resultado
        else:
            #Si adyacente fue visitado y no es el padre de v, entonces hay ciclo
            if padre[v] != w:
                return reconstruir_camino(padre, v, w)

def reconstruir_camino(padre, inicio, fin):
    camino = []
    actual = inicio
    while actual is not None:
        camino.append(actual)
        actual = padre[actual]
    return camino

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
    print(encontrar_ciclo(grafo))




