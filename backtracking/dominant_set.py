import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo

# Verifico que cada vértice esté en visitados O sea adyacente a un vértice en visitados
def es_dominant_set(grafo, visitados):
	for v in grafo.obtener_vertices():
		# El vértice debe estar en el conjunto O debe tener un adyacente en el conjunto
		if v not in visitados:
			# Si no está en visitados, verificar que tenga al menos un adyacente en visitados
			adyacentes = grafo.obtener_adyacentes(v)
			if not any(adj in visitados for adj in adyacentes):
				return False  # Vértice no dominado
	return True  # Todos los vértices están dominados

def dominant_set_rec(graph, vertices, visitados, idx_act, min):

    if len(vertices) == idx_act:
        if es_dominant_set(graph, visitados):
            if len(visitados) < len(min) or len(min) == 0:
                return visitados.copy()
        return min
    
    if len(visitados) > len(min) and len(min) > 0:
        return min

    v_act = vertices[idx_act]
    visitados.append(v_act)
    # Pruebo incluyendo el vértice
    min = dominant_set_rec(graph, vertices, visitados, idx_act+1, min)
    visitados.pop()
    # Pruebo sin incluir el vértice
    min = dominant_set_rec(graph, vertices, visitados, idx_act+1, min)
	
    return min
	

def dominanting_set_min(grafo):
    vertices = grafo.obtener_vertices()
    visitados = []
    min = []

    resultado = dominant_set_rec(grafo, vertices, visitados, 0, min)

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

    print(dominanting_set_min(g)) # Debería devolver [1, 4] o [4]

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

    print(dominanting_set_min(g2)) # Debería devolver [4, 5]

    g3 = Grafo()
    g3.agregar_vertice(1)
    g3.agregar_vertice(2)
    g3.agregar_vertice(3)

    g3.agregar_arista(1, 2)
    g3.agregar_arista(2, 3)
    g3.agregar_arista(3, 1)

    print(dominanting_set_min(g3)) # Debería devolver [1]