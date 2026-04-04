def bifurcaciones_con_patrulla(ciudades):
    if not ciudades:
        return []
        
    distancia_maxima = 50
    moviles = []
    ciudades.sort(key=lambda x: x[1])
    
    cubierto_hasta = -1
    pueblo_a_cubrir = ciudades[0]
    
    for i in range(len(ciudades)):
        km_actual = ciudades[i][1]
        if km_actual <= cubierto_hasta:
            continue
            
        if pueblo_a_cubrir[1] <= cubierto_hasta:
            pueblo_a_cubrir = ciudades[i]
            
        if km_actual > pueblo_a_cubrir[1] + distancia_maxima:
            patrullero = ciudades[i-1]
            moviles.append(patrullero)
            cubierto_hasta = patrullero[1] + distancia_maxima
            if km_actual > cubierto_hasta:
                pueblo_a_cubrir = ciudades[i]

    if ciudades[-1][1] > cubierto_hasta:
        moviles.append(ciudades[-1])
        
    return moviles

if __name__ == "__main__":
    ciudades = [('a', 10), ('b', 30), ('c', 31), ('d', 37), ('e', 40), ('f', 42), ('g', 59)]
    print(bifurcaciones_con_patrulla(ciudades))
    ciudades2 = [('a', 50), ('b', 100), ('c', 150)]
    print(bifurcaciones_con_patrulla(ciudades2))
    ciudades3 = [('a', 51), ('b', 100), ('c', 149), ('d', 801), ('e', 850), ('f', 899)]
    print(bifurcaciones_con_patrulla(ciudades3))
    ciudades4 = [('Castelli', 185), ('Gral Guido', 242), ('Lezama', 156), ('Maipú', 270), ('Sevigne', 194)]
    print(bifurcaciones_con_patrulla(ciudades4))
    ciudades5 = [('a', 50), ('b', 150), ('c', 250)]
    print(bifurcaciones_con_patrulla(ciudades5))
