def precios_inflacion(R):
    R.sort(reverse=True)
    total = 0
    j = 0
    for producto in R:
        total += producto ** (j+1)
        j+=1
    return total
