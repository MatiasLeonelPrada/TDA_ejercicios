import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo

def es_compatible(grafo, sol_parcial):
    for v in sol_parcial:
        for w in sol_parcial:
            if grafo.estan_conectados(v, w):
                return False
    return True

def no_llega_a_solucion(grafo, sol_parcial, n, v_actual):
    restantes =  n - len(sol_parcial)
    
    if len(sol_parcial) < n and grafo.cantidad_vertices() - v_actual < restantes:
        return True
    return False


def no_adyacentes_rec(grafo, n, sol_parcial, vertices, v_actual):
    if es_compatible(grafo, sol_parcial) and len(sol_parcial) == n:
        return sol_parcial
    if grafo.cantidad_vertices() == v_actual:
        return None
    if not es_compatible(grafo, sol_parcial) or no_llega_a_solucion(grafo, sol_parcial, n, v_actual):
        return None
    sol_parcial.append(vertices[v_actual])
    resultado = no_adyacentes_rec(grafo, n, sol_parcial, vertices, v_actual+1)
    if resultado != None:
        return resultado
    sol_parcial.remove(vertices[v_actual])
    return no_adyacentes_rec(grafo, n, sol_parcial, vertices, v_actual+1)


def no_adyacentes(grafo, n):
    vertices = grafo.obtener_vertices()
    sol_inicial = []
    resultado = no_adyacentes_rec(grafo, n, sol_inicial, vertices, 0)
    return resultado

if __name__ == "__main__":
    g = Grafo()
    g.agregar_vertice(1)
    g.agregar_vertice(2)
    g.agregar_vertice(3)
    g.agregar_vertice(4)
    g.agregar_vertice(5)
    g.agregar_arista(1, 2)
    g.agregar_arista(1, 4)
    g.agregar_arista(2, 3)
    g.agregar_arista(3, 5)
    g.agregar_arista(4, 3)
    print(no_adyacentes(g, 3)) # Debería devolver [2, 4, 5]

    g2 = Grafo()
    g2.agregar_vertice(1)
    g2.agregar_vertice(2)
    g2.agregar_vertice(3)
    g2.agregar_vertice(4)
    g2.agregar_arista(1, 2)
    g2.agregar_arista(1, 4)
    g2.agregar_arista(2, 3)
    g2.agregar_arista(4, 3)
    print(no_adyacentes(g2, 2)) # Debería devolver [2, 4] o [1, 3]

    g3 = Grafo()
    g3.agregar_vertice(1)
    g3.agregar_vertice(2)
    g3.agregar_vertice(3)
    g3.agregar_vertice(4)
    g3.agregar_vertice(5)
    g3.agregar_vertice(6)
    g3.agregar_vertice(7)
    g3.agregar_arista(1, 2)
    g3.agregar_arista(2, 3)
    g3.agregar_arista(4, 3)
    g3.agregar_arista(5, 6)
    g3.agregar_arista(5, 7)
    g3.agregar_arista(4, 7)
    print(no_adyacentes(g3, 4)) # Debería devolver [1, 3, 6, 7] 

