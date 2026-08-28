import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo

# Verifico que cada vértice esté en visitados O sea adyacente a un vértice en visitados
def es_independent_set(grafo, visitados):
    for v in visitados:
        for w in grafo.obtener_adyacentes(v):
            if w in visitados:
                return False
    return True

#Si ya no llego con los elementos restantes de mi camino actual, hago una poda
def ya_no_llego(max, visitados, idx_act, vertices):
    if len(max) > len(vertices)-idx_act + len(visitados)  and len(max) > 0:
        return True
    False
            

def independent_set_rec(graph, vertices, visitados, idx_act, max):

    if len(vertices) == idx_act:
        if es_independent_set(graph, visitados):
            if len(visitados) > len(max) or len(max) == 0:
                return visitados.copy()
        return max
    
    if ya_no_llego(max, visitados, idx_act, vertices):
        return max

    v_act = vertices[idx_act]
    visitados.append(v_act)
    # Pruebo incluyendo el vértice
    max = independent_set_rec(graph, vertices, visitados, idx_act+1, max)
    visitados.pop()
    # Pruebo sin incluir el vértice
    max = independent_set_rec(graph, vertices, visitados, idx_act+1, max)
	
    return max
	

def independent_set_max(grafo):
    vertices = grafo.obtener_vertices()
    visitados = []
    max = []

    resultado = independent_set_rec(grafo, vertices, visitados, 0, max)

    return resultado




if __name__ == "__main__":
    g = Grafo()
    g.agregar_vertice(1)
    g.agregar_vertice(2)
    g.agregar_vertice(3)
    g.agregar_vertice(4)
    g.agregar_vertice(5)
    g.agregar_arista(1, 2)
    g.agregar_arista(1, 3)
    g.agregar_arista(2, 4)
    g.agregar_arista(3, 4)
    g.agregar_arista(4, 5)

    print(independent_set_max(g)) # Debería devolver [1, 4] o [4]

    # g = Grafo()
    # g.agregar_vertice(1)
    # g.agregar_vertice(2)
    # g.agregar_vertice(3)
    # g.agregar_vertice(4)
    # g.agregar_vertice(5)
    # g.agregar_arista(1, 2)
    # g.agregar_arista(1, 3)
    # g.agregar_arista(2, 4)
    # g.agregar_arista(3, 4)
    # g.agregar_arista(4, 5)

    # print(independent_set_max(g)) # Debería devolver [1, 4] o [4]

    g2 = Grafo()
    g2.agregar_vertice(1)
    g2.agregar_vertice(2)
    g2.agregar_vertice(3)
    g2.agregar_vertice(4)
    g2.agregar_vertice(5)
    g2.agregar_vertice(6)
    g2.agregar_vertice(7)
    g2.agregar_vertice(8)
    g2.agregar_arista(1, 4)
    g2.agregar_arista(2, 4)
    g2.agregar_arista(3, 4)
    g2.agregar_arista(4, 5)
    g2.agregar_arista(5, 6)
    g2.agregar_arista(5, 7)
    g2.agregar_arista(5, 8)

    print(independent_set_max(g2)) # Debería devolver [1, 2, 3, 6, 7, 8]

    # g3 = Grafo()
    # g3.agregar_vertice(1)
    # g3.agregar_vertice(2)
    # g3.agregar_vertice(3)

    # g3.agregar_arista(1, 2)
    # g3.agregar_arista(2, 3)
    # g3.agregar_arista(3, 1)

    # print(independent_set_max(g3)) # Debería devolver [1]