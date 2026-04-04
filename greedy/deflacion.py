def precios_deflacion(R):
    R.sort()
    total = 0
    j = 0
    for producto in R:
        total += producto / (2 ** (j))
        j+=1
    return total


if __name__ == "__main__":
    R = [30, 20, 100, 50, 20, 10, 60, 40, 80, 90]
    print(precios_deflacion(R))

    R = [3, 2, 1, 4, 5]
    print(precios_deflacion(R))