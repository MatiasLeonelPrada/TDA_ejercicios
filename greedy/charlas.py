


def charlas(horarios):
    resultado = []
    if not horarios:
        return resultado
    horarios_ordenados = sorted(horarios, key=lambda x: x[1])
    resultado.append(horarios_ordenados[0])
    for horario in horarios_ordenados:
        if horario[0] >= resultado[-1][1]:
            resultado.append(horario)
    return resultado

# Ejemplo de uso
horarios = [(1, 3), (2, 5), (4, 6), (6, 7)]
print(charlas(horarios))  # Salida: [(1, 3), (4, 6), (6, 7)] 
horarios2 = [(1, 2), (2, 3), (3, 4), (4, 5)]
print(charlas(horarios2))  # Salida: [(1, 2), (2, 3), (3, 4), (4, 5)]   
