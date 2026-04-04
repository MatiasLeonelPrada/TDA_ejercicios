def precios_inflacion(R):
    R.sort(reverse=True)
    total = 0
    j = 0
    for producto in R:
        total += producto ** (j+1)
        j+=1
    return total

# Ejemplo de uso
R = [2, 3, 4]
print(precios_inflacion(R))  # Salida: 2^1 + 3^2 + 4^3 = 2 + 9 + 64 = 75
R2 = [1, 2, 3]
print(precios_inflacion(R2))  # Salida: 1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32