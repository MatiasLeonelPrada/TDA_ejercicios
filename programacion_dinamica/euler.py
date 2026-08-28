import math


def euler(n):
    e = [None] * (n + 1)
    e[0] = 1
    e[1] = 2
    for i in range(2, n+1):
        e[i] = e[i-1] + 1/math.factorial(i)
    return e[i]

if __name__ == "__main__":
    print(euler(3)) # Debería imprimir 
    # print(euler(20)) 