from Grafo import *
import csv
import sys

"""
Imprime los nombres de las ciudades recibidas en orden en el formato esperado.
"""
def imprimir(orden, costo = None):
    long = len(orden)
    for i in range(long):
        if i == long - 1:
            print("{}".format(orden[i]), end = "")
            break
        print("{} -> ".format(orden[i]), end = "")
    if costo:
        print("\nCosto total: {}".format(costo))

"""
Interfaz del programa.
"""
def traemelaco(ar_csv, kml):
    dic_ciudades = {}
    grafo = Grafo()
    grafo_dirigido = Grafo(None, True)
    with open(ar_csv, 'r') as ciudades:
        lector = csv.reader(ciudades)
        cant_ciudades = int(next(ciudades))
        for linea in range(cant_ciudades):
            ciudad, lat, long = next(lector)
            dic_ciudades[ciudad] = (long, lat)
            grafo.agregar_vertice(ciudad)
            grafo_dirigido.agregar_vertice(ciudad)
        cant_aristas = int(next(ciudades))
        for linea in range (cant_aristas):
            ciudad_1, ciudad_2, peso = next(lector)
            grafo.agregar_arista(ciudad_1, ciudad_2, int(peso))
            
    linea = sys.stdin.readline()
    while linea != '\n':
        linea = linea.rstrip('\n')
        param = linea.split(" ")
        if "ir" in param:
            if len(param) != 3:
                raise Exception('Cantidad de parametros erronea')
            orden, costo = camino_minimo(grafo, param[1][:-1], param[2])
            imprimir(orden, costo)
        elif "viaje" in param:
            if len(param) != 3:
                raise Exception('Cantidad de parametros erronea')
            if "aproximado," in param:
                orden, costo = viajante_aproximado(grafo, param[2])
            elif "optimo," in param:
                orden, costo = viajante_optimo(grafo, param[2])
            else:
                raise Exception('Parametro no reconocido')
            imprimir(orden, costo)
        elif "reducir_caminos" in param:
            if len(param) != 2:
                raise Exception('Cantidad de parametros erronea')
            arbol = arbol_tendido_minimo(grafo)
            print("Peso total: {}".format(arbol.obtener_peso_total()))
            salida = []
            arbol.recorrido_dfs(salida)
            with open(param[1], 'w', newline = '') as ciudades_arbol:
                escritor = csv.writer(ciudades_arbol, dialect = 'excel', lineterminator = '\r')
                escritor.writerows(salida)
        elif "itinerario" in param:
            if len(param) != 2:
                raise Exception('Cantidad de parametros erronea')
            with open(param[1], 'r') as recomendaciones:
                lector = csv.reader(recomendaciones)
                for ciudad1, ciudad2 in lector:
                    grafo_dirigido.agregar_arista(ciudad1, ciudad2)
                orden = orden_topologico(grafo_dirigido)
                print(imprimir(orden))
        if "reducir_caminos" not in param:
            with open(kml, 'w') as mapa:
                cant = len(orden)
                mapa.write(iniciar_kml(kml, linea))
                for i in range(cant):
                    mapa.write(agregar_vertice_kml(orden[i], dic_ciudades[orden[i]]))
                    if not i == cant - 1:
                        mapa.write(agregar_arista_kml(dic_ciudades[orden[i]], dic_ciudades[orden[i + 1]]))
                mapa.write(finalizar_kml())
        linea = sys.stdin.readline()
#------------------------------FUNCIONES PARA CREAR ARCHIVO KML------------------------------------------------
def iniciar_kml(ruta, comando):
    return '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://earth.google.com/kml/2.1">\n\t <Document>\n\t\t<name>{}</name>\n\t\t<description>{}</description>\n'.format(ruta, comando)

def finalizar_kml():
    return "\t</Document>\n</kml>"
    
def agregar_vertice_kml(vertice, coordenadas):
    return '\t\t<Placemark>\n\t\t\t<name>{}</name>\n\t\t\t<Point>\n\t\t\t\t<coordinates>{}, {}</coordinates>\n\t\t\t</Point>\n\t\t</Placemark>\n'.format(vertice, coordenadas[0], coordenadas[1])
    
def agregar_arista_kml(coord1, coord2):
    return '\t<Placemark>\n\t\t<LineString>\n\t\t\t<coordinates>{}, {} {}, {}</coordinates>\n\t\t</LineString>\n\t</Placemark>\n'.format(coord1[0], coord1[1], coord2[0], coord2[1])