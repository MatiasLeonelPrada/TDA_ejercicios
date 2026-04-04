
# [1, 2, 1, 2, 3] -> false
# [1, 1, 2, 3] -> false
# [1, 2, 3, 1, 1, 1] -> true
# [1] -> true

def mas_de_la_mitad_rec(arr, start, end):
    if start == end:
        return arr[start], 1
    
    mid = (start + end) // 2
    left_res, left_count = mas_de_la_mitad_rec(arr, start, mid)
    right_res, right_count  = mas_de_la_mitad_rec(arr, mid + 1, end)

    if right_res == left_res:
        return left_res, left_count + right_count
    else:
        return obtener_max_apariciones(arr, start, end, left_res, right_res)
    
def obtener_max_apariciones(arr, start, end, left_res, right_res):
    counts = {left_res: 0, right_res: 0}
    for i in range(start, end+1):
        if arr[i] == left_res:
            counts[left_res]+=1
        elif arr[i] == right_res:
            counts[right_res]+=1
    
    if counts[left_res] >= counts[right_res]:
        return left_res, counts[left_res]
    else:
        return right_res, counts[right_res]


def mas_de_la_mitad(arr):
    size = len(arr)
    candidato, apariciones = mas_de_la_mitad_rec(arr, 0, size - 1)

    if apariciones > size//2:
        return True
    return False


if __name__ == "__main__":
    print(mas_de_la_mitad([1, 2, 1, 2, 3])) # Debería imprimir False
    print(mas_de_la_mitad([1, 1, 2, 3])) # Debería imprimir False
    print(mas_de_la_mitad([1, 2, 3, 1, 1, 1])) # Debería imprimir True
    print(mas_de_la_mitad([1, 1, 3, 2, 3, 1])) # Debería imprimir False
    print(mas_de_la_mitad([1, 1, 1, 2, 3, 1])) # Debería imprimir True
    print(mas_de_la_mitad([1])) # Debería imprimir True



