import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo

def crear_red_flujo(miembros, s, t):
    #creo grafo dirigido:
    grafo = Grafo(True)
    clubes = []
    partidos = []

    grafo.agregar_vertice(s)
    grafo.agregar_vertice(t)

    for miembro in miembros:
        grafo.agregar_vertice(miembro.nombre)

        vertices = grafo.obtener_vertices()
        for club in miembro.clubes:
            if club not in vertices:
                grafo.agregar_vertice(club)
                clubes.append(club)
            grafo.agregar_arista(club, miembro.nombre) # cada miembro puede tener varios clubes, pero cada club solo puede tener un representante.
        
        if miembro.partido_politico not in vertices:
            grafo.agregar_vertice(miembro.partido_politico)
            partidos.append(miembro.partido_politico)
        grafo.agregar_arista(miembro.nombre, miembro.partido_politico)

    for club in clubes:
        grafo.agregar_arista(s, club)

    capacidad = len(miembros) // 2
    for partido in partidos:
        grafo.agregar_arista(partido, t, capacidad) # cada partido politico no puede tener más de n/2 miembros.

    return grafo

def representantes(miembros):

    s = "Sumidero"
    t = "Fuente"
    grafo = crear_red_flujo(miembros, s, t)
    ff = flujo(grafo, s, t)
    print(ff)
    representantes_dict = {}
        
    clubes = set()
    clubes_representados = set()
    for miembro in miembros:
        for club in miembro.clubes:
            clubes.add(club)

    for arista in ff:
        if arista[0] in clubes:
            if ff[arista] == 1:
                representantes_dict[arista[1]] = arista[0]
                clubes_representados.add(arista[0])

    if clubes_representados != clubes:
        return None

    return representantes_dict

# def representantes(miembros):

#     s = "Sumidero"
#     t = "Fuente"
#     grafo = crear_red_flujo(miembros, s, t)
#     ff = flujo(grafo, s, t)
#     representantes_dict = {}
        
#     clubes = set()
#     for miembro in miembros:
#         for club in miembro.clubes:
#             clubes.add(club)

#     clubes_representados = set()
#     for arista in ff:
#         if arista[0] in clubes:
#             if ff[arista] > 1:
#                 representantes_dict[arista[1]] = arista[0]
#                 clubes_representados.add(arista[0])

#     if clubes_representados != clubes:
#         return None

#     return representantes_dict