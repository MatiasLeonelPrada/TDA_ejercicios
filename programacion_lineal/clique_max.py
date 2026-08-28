import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo
import pulp
from pulp import LpAffineExpression as Sumatoria


def clique_max(grafo):
    vertices = grafo.obtener_vertices()
    variables = dict()
    # defino una variable binaria para cada vertice del grafo, que indica si el vertice esta incluido en la solucion o no
    for i in range(len(vertices)):
        v = vertices[i]
        variables[v] = pulp.LpVariable("y" + str(i), cat="Binary")
        
    problem = pulp.LpProblem("vertex_cover", pulp.LpMaximize)
    for i in range(len(vertices)):
        v = vertices[i]
        ady = grafo.obtener_adyacentes(v)
        suma_ady = Sumatoria([(variables[w], 1) for w in ady])
        suma_vertices = Sumatoria([(variables[w], 1) for w in vertices])
        
        #defino big M como el numero de vertices adyacentes a v para cada paso
        M = len(vertices) - 1
        problem += variables[v] + suma_ady >= suma_vertices - M * (1 - variables[v])

    problem += Sumatoria([(variables[v], 1) for v in vertices])
    problem.solve()

    # print(list(map(lambda yi: pulp.value(yi), variables.values())))
    return [v for v in vertices if int(pulp.value(variables[v])) != 0]
    

if __name__ == "__main__":

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


    # print(clique_max(g)) # Debería devolver [1, 2] o [1, 3] o [2, 4] o [3, 4] o [4, 5]

    # g2 = Grafo()
    # g2.agregar_vertice(1)
    # g2.agregar_vertice(2)
    # g2.agregar_vertice(3)
    # g2.agregar_vertice(4)
    # g2.agregar_vertice(5)
    # g2.agregar_vertice(6)
    # g2.agregar_vertice(7)
    # g2.agregar_vertice(8)
    # g2.agregar_arista(1, 4)
    # g2.agregar_arista(2, 4)
    # g2.agregar_arista(3, 4)
    # g2.agregar_arista(4, 5)
    # g2.agregar_arista(5, 6)
    # g2.agregar_arista(5, 7)
    # g2.agregar_arista(5, 8)

    # print(clique_max(g2)) # Debería devolver [1, 4] o [2, 4] o [3, 4] o [4, 5] o [5, 6] o [5, 7] o [5, 8]

    # g3 = Grafo()
    # g3.agregar_vertice(1)
    # g3.agregar_vertice(2)
    # g3.agregar_vertice(3)

    # g3.agregar_arista(1, 2)
    # g3.agregar_arista(2, 3)
    # g3.agregar_arista(3, 1)

    # print(clique_max(g3)) # Debería devolver [1, 2, 3]

    g4 = Grafo()
    g4.agregar_vertice(1)
    g4.agregar_vertice(2)
    g4.agregar_vertice(3)
    g4.agregar_vertice(4)
    g4.agregar_vertice(5)
    g4.agregar_vertice(6)
    g4.agregar_arista(1, 5)
    g4.agregar_arista(1, 2)
    g4.agregar_arista(2, 3)
    g4.agregar_arista(5, 2)
    g4.agregar_arista(5, 4)
    g4.agregar_arista(4, 3)
    g4.agregar_arista(6, 4)

    print(clique_max(g4)) # Debería devolver [1, 2, 5] 