def cobertura(casas, R, K):
    antenas = []
    if len(casas) == 0:
        return antenas
    casas.sort()
    actual = casas[0]+R
    antenas.append(actual)

    for i in range(len(casas)):
        if actual - R <= casas[i] <= actual + R:
            continue
        actual = casas[i] + R
        antenas.append(actual)

    return antenas

if __name__ == "__main__":
    # casas = [10, 14]
    # R = 3
    # K = 1000
    # print(cobertura(casas, R, K))

    # casas1 = [150, 50, 100]
    # R1 = 50
    # K1 = 1000
    # print(cobertura(casas1, R1, K1))

    # casas2 = [50, 150, 105]
    # R2 = 50
    # K2 = 1000
    # print(cobertura(casas2, R2, K2))

    casas3 = [51, 107, 844, 802, 151, 902]
    R3 = 50
    K3 = 1000
    print(cobertura(casas3, R3, K3))