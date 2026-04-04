def bifurcaciones_con_patrulla(ciudades):
    distancia_maxima = 50
    cobertura = []
    nro_ciudades = len(ciudades)
    for i in range(nro_ciudades):
        ciudad_actual, km = ciudades[i]
        limite_inferior = km - distancia_maxima
        limite_superior = km + distancia_maxima
        cant_ciudades_cubiertas = 0
        for ciudad in ciudades:
            if ciudad[0] == ciudad_actual:
                continue
            if limite_inferior <= ciudad[1] <= limite_superior:
                cant_ciudades_cubiertas += 1
        cobertura.append(((ciudad_actual, km), cant_ciudades_cubiertas))
        if cant_ciudades_cubiertas == len(ciudades) - 1:
            break
    
    cobertura.sort(key=lambda x: x[1], reverse=True)  # Ordenar por cantidad de ciudades cubiertas
    # print(cobertura)
    resultado = []
    cobertura_total = 0
    # print(nro_ciudades)
    for ciudad, cant in cobertura:
        cobertura_total += cant
        if cobertura_total <= nro_ciudades:
            resultado.append(ciudad)
            #nro_ciudades -= 1
        

    return resultado

if __name__ == "__main__":
    # ciudades = [('a', 10), ('b', 30), ('c', 31), ('d', 37), ('e', 40), ('f', 42), ('g', 59)]
    # print(bifurcaciones_con_patrulla(ciudades))
    # ciudades2 = [('a', 50), ('b', 100), ('c', 150)]
    # print(bifurcaciones_con_patrulla(ciudades2))
    ciudades3 = [('a', 51), ('b', 100), ('c', 149), ('d', 801), ('e', 850), ('f', 899)]
    print(bifurcaciones_con_patrulla(ciudades3))
    ciudades4 = [('Castelli', 185), ('Gral Guido', 242), ('Lezama', 156), ('Maipú', 270), ('Sevigne', 194)]
    print(bifurcaciones_con_patrulla(ciudades4))
