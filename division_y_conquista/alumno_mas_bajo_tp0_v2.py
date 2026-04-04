class Alumno:
    def __init__(self, nombre: str, altura: float):
        self.nombre = nombre
        self.altura = altura

    def __repr__(self):
        return f"Alumno(nombre={self.nombre!r}, altura={self.altura})"


def indice_mas_bajo_rec(alumnos, inicio, fin):
    if inicio == fin:
        return inicio
    medio = (inicio + fin) // 2
    if (alumnos[medio].altura < alumnos[medio+1].altura):
        if (medio > 0 and alumnos[medio].altura > alumnos[medio-1].altura):
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

    altura_actual = alumnos[indice].altura
    if len_alumnos == 1:
        return True
    if indice == 0:
        return altura_actual < alumnos[indice+1].altura
    if indice == len_alumnos - 1:
        return altura_actual < alumnos[indice-1].altura
    return altura_actual < alumnos[indice - 1].altura and altura_actual < alumnos[indice + 1].altura



if __name__ == "__main__":
    alumnos = [
        Alumno("Juan", 1.2),
        Alumno("María", 1.15),
        Alumno("Pedro", 1.14),
        Alumno("Ana", 1.12),
        Alumno("Luis", 1.02),
        Alumno("Sofía", 0.98),
        Alumno("Carlos", 1.18),
        Alumno("Lucía", 1.23),
    ]

    alumnos_2 = [
        Alumno("Juan", 1.2),
        Alumno("María", 1.15),
        Alumno("Pedro", 1.14),
        Alumno("Ana", 1.12),
        Alumno("Luis", 1.02),
        Alumno("Sofía", 0.98),
        Alumno("Carlos", 0.97),
        Alumno("Lucía", 1.23),
    ]

    for lista in (alumnos, alumnos_2):
        i = indice_mas_bajo(lista)
        print("indice", i)
        if i >= 0 and validar_mas_bajo(lista, i):
            print(f"El alumno más bajo es: {lista[i].nombre} con {lista[i].altura} metros.")
        else:
            print("No se pudo determinar el alumno más bajo.")
