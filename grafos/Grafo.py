import random
import math
import heapq
import queue

#--------------------------------------TDA GRAFO--------------------------------------------
class Grafo:
    """
    Constructor del grafo. Permite recibir una lista de vertices a agregar. El grafo es NO DIRIGIDO por default.
    Post: el grafo fue creado.
    """
    def __init__(self, vertices = None, dirigido = False):
        self.dirigido = dirigido
        self.vertices = {}
        self.cantidad = 0
        if vertices:
            for x in vertices:
                self.vertices[x] = {}
            self.cantidad += len(vertices)
    
    """
    Devuelve una representacion del grafo que puede ser impresa por consola.
    Pre: el grafo fue creado.
    Post: se devolvio una representacion en string del grafo.
    """
    def __str__(self):
        return self.obtener_vertices()

    """
    Agrega un vertice al grafo.
    Pre: el grafo fue creado.
    Post: se creo y agrego un vertice nuevo al grafo.
    """
    def agregar_vertice(self, vertice):
        self.vertices[vertice] = {}
        self.cantidad += 1
    
    """
    Borra un vertice del grafo, y todas las aristas que salieran (o llegaran, en caso de un grafo no dirigido) al mismo.
    Pre: el grafo fue creado.
    Post: se elimino un vertice y todas sus aristas.
    """
    def borrar_vertice(self, vertice):
        del self.vertices[vertice]
        for clave in self.vertices.keys():
            if vertice in self.vertices[clave]:
                del self.vertices[clave][vertice]
    
    """
    Agrega una arista entre dos vertices del grafo. El peso es 1 por default.
    Pre: el grafo y los vertices a unir por la arista fueron creados.
    Post: se agrego una arista entre los dos vertices.
    """
    def agregar_arista(self, v_1, v_2, peso = 1):
        if not self.vertice_pertenece(v_1) or not self.vertice_pertenece(v_2):
            return None
        self.vertices[v_1][v_2] = peso
        if not self.dirigido:
            self.vertices[v_2][v_1] = peso
    
    """
    Elimina la arista que conecta los dos vertices recibidos por parametro.
    Pre: el grafo, los vertices y la arista a eliminar fueron creados.
    Post: se borro la arista y los vertices ya no estan conectados.
    """
    def borrar_arista(self, v_1, v_2):
        del self.vertices[v_1][v_2]
        if not self.dirigido:
            del self.vertices[v_2][v_1]

    """
    Devuelve el peso de la arista que une los vertices recibidos por parametro.
    Pre: el grafo, los vertices y la arista fueron creados.
    Post: se devolvio el peso de la arista que une los vertices recibidos por parametro.
    """
    def obtener_peso(self, v_1, v_2):
        if not self.vertice_pertenece(v_1) or not self.vertice_pertenece(v_2):
            return 0
        return self.vertices[v_1][v_2]
    
    """
    Devuelve la suma del peso de todas las aristas del grafo.
    Pre: el grafo fue creado.
    """
    def obtener_peso_total(self):
        peso_total = 0
        vertices = self.obtener_vertices()
        visitados = []
        for v in vertices:
            for ady in self.obtener_adyacentes(v):
                if (v,ady) in visitados or (ady, v) in visitados:
                    continue
                peso_total += self.obtener_peso(v, ady)
                visitados.append((v,ady))
        return peso_total

    """
    Devuelve True si el vertice pertenece al grafo, False en caso contrario.
    Pre: el grafo fue creado.
    """
    def vertice_pertenece(self, vertice):
        return vertice in self.vertices

    """
Devuelve True si existe una arista entre los dos vertices recibidos por parametro, False en caso contrario.
    Pre: el grafo y los vertices fueron creados.
    """
    def estan_conectados(self, v_1, v_2):
        return v_2 in self.vertices[v_1]
    """
    Devuelve una lista con los vertices del grafo.    
    Pre: el grafo fue creado.
    """
    def obtener_vertices(self):
        return list(self.vertices.keys())

    """
    Devuelve un vertice aleatorio del grafo.
    Pre: el grafo fue creado.
    """
    def obtener_aleatorio(self):
        return self.obtener_vertices()[random.randint(0, self.cantidad - 1)]
        
    """
    Devuelve la lista de vertices adyacentes al pasado por parametro.
    Pre: el grafo y el vertice recibido por parametro fueron creados.
    """
    def obtener_adyacentes(self, vertice):
        return list(self.vertices[vertice].keys())
    """
    Devuelve la cantidad de vertices del grafo.
    Pre: el grafo fue creado.
    """
    def cantidad_vertices(self):
        return self.cantidad
    
    """
    Itera el grafo mediante un recorrido dfs.
    Pre: el grafo fue creado, salida es una lista.
    """
    def recorrido_dfs(self, salida):
        visitados = []
        inicio = self.obtener_aleatorio()
        self.recorrido_dfs_rec(inicio, visitados, salida)
    
    def recorrido_dfs_rec(self, inicio, visitados, salida):
        visitados.append(inicio)
        for ady in self.obtener_adyacentes(inicio):
            if not ady in visitados:
                salida.append((inicio, ady, str(self.obtener_peso(inicio, ady))))
                print((inicio, ady, self.obtener_peso(inicio, ady)))
                self.recorrido_dfs_rec(ady, visitados, salida)


#--------------------------------BIBLIOTECA DE FUNCIONES--------------------------------------------
def camino_minimo(grafo, origen, destino):
    distancia = {}
    padre = {}
    orden = []
    for v in grafo.obtener_vertices():
        distancia[v] = math.inf
    distancia[origen] = 0
    padre[origen] = None
    heap = []
    heapq.heappush(heap, (distancia[origen], origen))
    while not len(heap) == 0:
        dist, vertice = heapq.heappop(heap)
        if vertice == destino:
            orden = reconstruir(padre, origen, destino)
            return orden, distancia[destino]
        for v in grafo.obtener_adyacentes(vertice):
            if distancia[vertice] + grafo.obtener_peso(vertice, v) < distancia[v]:
                padre[v] = vertice
                distancia[v] = distancia[vertice] + grafo.obtener_peso(vertice, v)
                heapq.heappush(heap, (distancia[v], v))
    return orden, distancia[destino]

def reconstruir(padre, origen, destino):
    orden = []
    reconstruir_recursivo(padre, origen, destino, orden)
    return orden
    
def reconstruir_recursivo(padre, origen, destino, orden):
    if not padre[destino]:
        orden.append(destino)
        return
    reconstruir_recursivo(padre, origen, padre[destino], orden)
    orden.append(destino)
    return orden

def orden_topologico(grafo):
    grados = {}
    for vertice in grafo.obtener_vertices():
        grados[vertice] = 0
    for vertice in grafo.obtener_vertices():
        for v in grafo.obtener_adyacentes(vertice):
            grados[v] += 1
    resultado = []
    cola = queue.Queue()
    for vertice in grafo.obtener_vertices():
        if grados[vertice] == 0:
            cola.put_nowait(vertice)
    while not cola.empty():
        vertice = cola.get_nowait()
        resultado.append(vertice)
        for v in grafo.obtener_adyacentes(vertice):
            grados[v] -= 1
            if grados[v] == 0:
                cola.put_nowait(v)
    return resultado

def arbol_tendido_minimo(grafo):
    inicio = grafo.obtener_aleatorio()
    visitados = []
    visitados.append(inicio)
    heap = []
    for vertice in grafo.obtener_adyacentes(inicio):
        heapq.heappush(heap, (grafo.obtener_peso(inicio, vertice), (inicio, vertice)))
    arbol = Grafo(grafo.obtener_vertices())
    while not len(heap) == 0:
        peso, tupla = heapq.heappop(heap)
        v, w = tupla
        if w in visitados:
            continue
        arbol.agregar_arista(v, w, peso)
        visitados.append(w)
        for x in grafo.obtener_adyacentes(w):
            heapq.heappush(heap, (grafo.obtener_peso(w, x), (w, x)))
    return arbol

def viajante_aproximado(grafo, origen):
    recorrido = [origen]
    act = origen
    costo = 0
    while not len(recorrido) == len(grafo.obtener_vertices()):
        menor_dist = math.inf
        vert_cercano = None
        for vertice in grafo.obtener_adyacentes(act):
            if vertice in recorrido:
                continue
            dist_act = grafo.obtener_peso(act, vertice)
            if dist_act < menor_dist:
                vert_cercano = vertice
                menor_dist = dist_act
        recorrido.append(vert_cercano)
        costo += menor_dist
        act = vert_cercano
    recorrido.append(origen)
    costo += grafo.obtener_peso(act, origen)
    return recorrido, costo
    
def viajante_optimo(grafo, origen):
    costo = 0
    camino_opt = [origen]
    costo_opt = math.inf
    act = origen
    camino_actual = [origen]
    camino_actual, camino_opt, costo = viajante_recursivo(grafo, origen, act, camino_opt, camino_actual, costo, costo_opt)
    return camino_opt + [origen], costo

def viajante_recursivo(grafo, origen, act, camino_opt, camino_actual, costo, costo_opt):
    if len(camino_actual) == len(grafo.obtener_vertices()):
        costo += grafo.obtener_peso(act, origen)
        if (costo < costo_opt):
            costo_a_devolver = costo
            camino_opt = camino_actual[:]
        else:
            costo_a_devolver = costo_opt
        return camino_actual, camino_opt, costo_a_devolver
    for vertice in grafo.obtener_adyacentes(act):
        if vertice not in camino_actual:
            camino_actual.append(vertice)
            costo += grafo.obtener_peso(act, vertice)
            camino_actual, camino_opt, costo_opt = viajante_recursivo(grafo, origen, vertice , camino_opt, camino_actual, costo, costo_opt)
            # if (costo_actual < costo_opt) :
            #     costo_opt = costo_actual
            #     
                
            #if len(camino_actual) == len(grafo.obtener_vertices()) + 1:
            #    camino_actual.pop()
            pop = camino_actual.pop()
            costo -= grafo.obtener_peso(act, vertice)
        else:
            continue
        #camino_actual.pop()
    #camino_actual.pop()
        #print(camino_opt)
    return camino_actual, camino_opt, costo_opt
        
    
    
