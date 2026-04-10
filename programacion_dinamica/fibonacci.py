def fibonacci(n):
    FIBO = [None] * (n + 1)
    FIBO[0] = 0
    FIBO[1] = 1
    for i in range(2, n+1):
        FIBO[i] = FIBO[i-1] + FIBO[i-2]
    return FIBO[n]

def fibonacci_dinamico(n):
    anterior = 1
    anterior_nuevo = 1
    for i in range(2, n+1):
        actual = anterior + anterior_nuevo
        anterior = anterior_nuevo
        anterior_nuevo = actual
    return anterior_nuevo



if __name__ == "__main__":
    # print(fibonacci(1))  # Debería imprimir 1
    # print(fibonacci(2))  # Debería imprimir 1
    # print(fibonacci(3))  # Debería imprimir 2
    # print(fibonacci(4))  # Debería imprimir 3
    # print(fibonacci(5))  # Debería imprimir 5
    # print(fibonacci(10)) # Debería imprimir 55

    print(fibonacci_dinamico(0)) # Debería imprimir 0
    print(fibonacci_dinamico(1))  # Debería imprimir 1
    print(fibonacci_dinamico(2))  # Debería imprimir 2
    print(fibonacci_dinamico(3))  # Debería imprimir 3
    print(fibonacci_dinamico(4))  # Debería imprimir 5
    print(fibonacci_dinamico(5))  # Debería imprimir 8
    print(fibonacci_dinamico(6)) # Debería imprimir 13