import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafos.Grafo import Grafo

# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):

    personas = set()
    for a, b in conocidos:
        personas.add(a)
        personas.add(b)

    grafo = Grafo()
    for persona in personas:
        grafo.agregar_vertice(persona)
    for a, b in conocidos:
        grafo.agregar_arista(a, b)

    resultado = []


    while True:

        resultado = []
        for persona in grafo.obtener_vertices():
            if len(grafo.obtener_adyacentes(persona)) < 4:
                resultado.append(persona)
        
        if len(resultado) == 0:
            break

        for persona in resultado:
            grafo.borrar_vertice(persona)

    return grafo.obtener_vertices()


if __name__ == "__main__":
    # conocidos = [("A", "B"), ("B", "C"), ("B", "D"), ("B", "E"), ("C", "D"), ("D", "E"), ("E", "F"), ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("E", "J"), ("E", "K"), ("E", "L"), ("E", "M"), ("E", "N")]
    # print(obtener_invitados(conocidos))
    # conocidos1 = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')]
    # print(obtener_invitados(conocidos1))
    conocidos2 = [('0', '6'), ('1', '10'), ('10', '0'), ('11', '2'), ('12', '0'), ('13', '2'), ('9', '3'), ('14', '4'), ('15', '3'), ('15', '5'), ('15', '7'), ('2', '4'), ('2', '8'), ('2', '9'), ('3', '2'), ('3', '5'), ('3', '7'), ('4', '1'), ('4', '13'), ('9', '15'), ('5', '11'), ('5', '6'), ('5', '9'), ('6', '12'), ('6', '3'), ('6', '8'), ('9', '7'), ('7', '6'), ('7', '8'), ('8', '13'), ('8', '3'), ('8', '9'), ('9', '11')]
    print(obtener_invitados(conocidos2))