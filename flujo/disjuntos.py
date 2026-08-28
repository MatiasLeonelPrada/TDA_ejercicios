import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo

def buscar_camino_dfs(grafo, actual, t, visitados, flujo):
    # Agregamos el nodo actual al camino ni bien lo visitamos
    visitados.append(actual)
    
    # si llegamos al destino, cortamos la busqueda y devolvemos True
    if actual == t:
        return True
        
    # Exploramos los adyacentes
    for ady in grafo.obtener_adyacentes(actual):
        arista = (actual, ady)
        
        # Revisamos si el adyacente no está en el camino actual (para evitar ciclos)
        if flujo[arista] > 0 and ady not in visitados:
            # Si la llamada recursiva encuentra el destino
            if buscar_camino_dfs(grafo, ady, t, visitados, flujo):
                # Restamos el flujo para no volver a usar esta arista en otro camino
                flujo[arista] -= 1
                return True
                
    #  Si revisamos todos los adyacentes y ninguno nos llevo a 't', 
    # sacamos este nodo del camino actual (backtrack)
    visitados.pop()
    return False

def flujo(grafo, s, t):
    return {(0, 1): 0, (0, 2): 1, (0, 3): 1, (1, 2): 0, (2, 3): 0, (2, 6): 1, (3, 6): 1, (4, 2): 0, (4, 7): 0, (5, 1): 0, (5, 4): 0, (5, 7): 1, (6, 5): 1, (6, 7): 1}

def disjuntos(grafo, s, t):
    # devolver una lista en la cual cada elemento es una lista, con el camino
    # entre s y t. Todos esos caminos deben incluir inicio (s) y fin (t).
    flujo_actual = flujo(grafo, s, t)
    inicio = s
    resultado = []
    
    while True:
        visitados = [] # Iniciamos una lista vacía para el camino actual
        if buscar_camino_dfs(grafo, inicio, t, visitados, flujo_actual):
            resultado.append(list(visitados))
        else:
            break
            
    return resultado

if __name__ == "__main__":
    g = Grafo(dirigido=True)
    g.agregar_vertice(0)
    g.agregar_vertice(1)
    g.agregar_vertice(2)
    g.agregar_vertice(3)
    g.agregar_vertice(4)
    g.agregar_vertice(5)
    g.agregar_vertice(6)
    g.agregar_vertice(7)

    g.agregar_arista(0, 1)
    g.agregar_arista(0, 2)
    g.agregar_arista(0, 3)
    g.agregar_arista(1, 2)
    g.agregar_arista(2, 3)
    g.agregar_arista(2, 6)
    g.agregar_arista(3, 6)
    g.agregar_arista(4, 2)
    g.agregar_arista(4, 7)
    g.agregar_arista(5, 1)
    g.agregar_arista(5, 4)
    g.agregar_arista(5, 7)
    g.agregar_arista(6, 5)
    g.agregar_arista(6, 7)

    print(disjuntos(g, 0, 7))