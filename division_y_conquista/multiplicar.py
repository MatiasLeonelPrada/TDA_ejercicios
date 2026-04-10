def multiplicar(a, b):
    if a < 10 or b < 10:
        return a * b
    n = max(len(str(a)), len(str(b)))
    m = n // 2
    A = a // (10**m)
    B = a % (10**m)
    C = b // (10**m)
    D = b % (10**m)
    AC = multiplicar(A, C)
    BD = multiplicar(B, D)
    AB_CD = multiplicar(A + B, C + D)
    AD_BC = AB_CD - AC - BD
    return (AC * (10**(2*m))) + (AD_BC * (10**m)) + BD

def partir_num(numero):
    num_str = str(numero)
    n = len(num_str)
    
    mitad = n // 2
    
    if n == 1:
        return 0, numero
        
    A = int(num_str[:mitad]) # Mitad izquierda
    B = int(num_str[mitad:]) # Mitad derecha
    
    return A, B

if __name__ == "__main__":
    # num1 = 1111
    # num2 = 2222
    
    # A1, B1 = partir_num(num1)
    # A2, B2 = partir_num(num2)
    
    # print(f"Partes de {num1}: A={A1}, B={B1}")
    # print(f"Partes de {num2}: A={A2}, B={B2}")

    # resultado = multiplicar(num1, num2)
    # print(f"Resultado de multiplicar {num1} y {num2}: {resultado}")

    num1 = 1234
    num2 = 5678
    resultado = multiplicar(num1, num2)
    print(f"Resultado de multiplicar {num1} y {num2}: {resultado}")