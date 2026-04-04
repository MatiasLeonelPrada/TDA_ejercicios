def indice_mas_bajo_rec(alumnos, inicio, fin):
    if inicio == fin:
        return inicio
    medio = (inicio + fin) // 2
    if (alumnos[medio]['altura'] < alumnos[medio+1]['altura']):
        if (medio > 0 and alumnos[medio]['altura'] > alumnos[medio-1]['altura']):
            return indice_mas_bajo_rec(alumnos, inicio, medio-1)
        return medio
    else:
        return indice_mas_bajo_rec(alumnos, medio+1, fin)

def indice_mas_bajo(alumnos):
    cant_alumnos = len(alumnos)
    index_mas_bajo = indice_mas_bajo_rec(alumnos, 0, cant_alumnos - 1)

    return index_mas_bajo


def validar_mas_bajo(alumnos, indice):
    len_alumnos = len(alumnos)
    if indice < 0 or indice >= len_alumnos:
        return False

    altura_actual = alumnos[indice]['altura']
    if len_alumnos == 1:
        return True
    if indice == 0:
        return altura_actual < alumnos[indice+1]['altura']
    if indice == len_alumnos - 1:
        return altura_actual < alumnos[indice-1]['altura']
    return altura_actual < alumnos[indice - 1]['altura'] and altura_actual < alumnos[indice + 1]['altura']



if __name__ == "__main__":  
    alumnos = [
        {"nombre": "Juan", "altura": 1.2},
        {"nombre": "María", "altura": 1.15},
        {"nombre": "Pedro", "altura": 1.14},
        {"nombre": "Ana", "altura": 1.12},
        {"nombre": "Luis", "altura": 1.02},
        {"nombre": "Sofía", "altura": 0.98},
        {"nombre": "Carlos", "altura": 1.18},
        {"nombre": "Lucía", "altura": 1.23}
    ]

    alumnos_2 = [
        {"nombre": "Juan", "altura": 1.2},
        {"nombre": "María", "altura": 1.15},
        {"nombre": "Pedro", "altura": 1.14},
        {"nombre": "Ana", "altura": 1.12},
        {"nombre": "Luis", "altura": 1.02},
        {"nombre": "Sofía", "altura": 0.98},
        {"nombre": "Carlos", "altura": 0.97},
        {"nombre": "Lucía", "altura": 1.23}
    ]

    indice = indice_mas_bajo(alumnos)
    indice_2 = indice_mas_bajo(alumnos_2)
    print("indice", indice)
    print("indice_2", indice_2)
    if validar_mas_bajo(alumnos, indice):
        print(f"El alumno más bajo es: {alumnos[indice]['nombre']} con una altura de {alumnos[indice]['altura']} metros.")
    else:
        print("No se pudo determinar el alumno más bajo.")

    if validar_mas_bajo(alumnos_2, indice_2):
        print(f"El alumno más bajo es: {alumnos_2[indice_2]['nombre']} con una altura de {alumnos_2[indice_2]['altura']} metros.")
    else:
        print("No se pudo determinar el alumno más bajo.")