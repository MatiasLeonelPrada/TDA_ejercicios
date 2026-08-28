from typing import List

import pulp
from pulp import LpAffineExpression as Sumatoria



def juan_el_vago(trabajos):
    y = []
    for i in range(len(trabajos)):
        y.append(pulp.LpVariable("y" + str(i), cat="Binary"))

    problem = pulp.LpProblem("products", pulp.LpMaximize)
    for i in range(len(y)-1):
        problem += y[i]+ y[i+1]  <= 1
    problem += Sumatoria([(y[i], trabajos[i]) for i in range(len(y))])

    problem.solve()
    result =list(map(lambda yi: pulp.value(yi), y))
    return [i for i in range(len(result)) if int(result[i]) != 0]
    

if __name__ == "__main__":

    print(juan_el_vago([100, 5]))  # debería imprimir [0]
    print(juan_el_vago([100, 5, 50]))  # debería imprimir [0, 2]
    print(juan_el_vago([100, 5, 50, 1]))  # debería imprimir [0, 2]
    print(juan_el_vago([100, 5, 50, 1, 1, 200]))  # debería imprimir [0, 2, 5]
    print(juan_el_vago([100, 5, 50, 1, 1, 200, 300]))  # debería imprimir [0, 2, 4, 6]
    # print(juan_el_vago([100, 5, 50, 1, 1, 200, 300, 400]))  # debería imprimir [0, 2, 5, 7]
    # print("Peso usado:", sum([pesos[i] * y[i] for i in range(len(y))]))
    # print("Valor obtenido:", sum([trabajos[i] * y[i] for i in range(len(y))]))
