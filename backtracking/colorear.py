import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo

def es_compatible(grafo, ultimo, colores):
    for w in grafo.obtener_adyacentes(ultimo):
        if w in colores and colores[w] == colores[ultimo]:
            return False
    return True

def colorear_rec(grafo, n, vertices, colores, idx_act):
    if idx_act == len(vertices) and len(colores.keys()) == len(vertices):
        return True
    v_act = vertices[idx_act]
    for color in range(n):
        colores[v_act] = color
        if es_compatible(grafo, v_act, colores):
            if colorear_rec(grafo, n, vertices, colores, idx_act+1):
                return True
    del colores[v_act]
    return False
        


def colorear(grafo, n):
    vertices = grafo.obtener_vertices()
    colores = {}
    if colorear_rec(grafo, n, vertices, colores, 0):
        return True
    return False


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
    # print(colorear(g, 3)) # Debería devolver True
    # print(colorear(g, 2)) # Debería devolver True
    # print(colorear(g, 1)) # Debería devolver False

    g2 = Grafo()
    g2.agregar_vertice(1)
    g2.agregar_vertice(2)
    g2.agregar_vertice(3)
    g2.agregar_vertice(4)
    g2.agregar_vertice(5)
    g2.agregar_arista(1, 2)
    g2.agregar_arista(1, 3)
    g2.agregar_arista(2, 4)
    g2.agregar_arista(3, 4)
    g2.agregar_arista(4, 1)
    g2.agregar_arista(4, 5)
    print(colorear(g2, 3)) # Debería devolver True
    print(colorear(g2, 2)) # Debería devolver False