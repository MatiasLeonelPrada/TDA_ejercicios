def escalones(n):
    pasos_escalera = [None] * (n + 1)
    pasos_escalera[0] = 0
    if n >= 1:
        pasos_escalera[1] = 1
    if n >= 2:
        pasos_escalera[2] = 2
    if n >= 3:
        pasos_escalera[3] = 4
    for i in range(4, n + 1):
        pasos_escalera[i] = pasos_escalera[i-1] + pasos_escalera[i-2] + pasos_escalera[i-3]
    return pasos_escalera[n]

if __name__ == "__main__":
    print(escalones(1))  # Debería imprimir 1
    print(escalones(2))  # Debería imprimir 2
    print(escalones(3))  # Debería imprimir 4
    print(escalones(4))  # Debería imprimir 7
    print(escalones(5))  # Debería imprimir 13
    print(escalones(10)) # Debería imprimir 274