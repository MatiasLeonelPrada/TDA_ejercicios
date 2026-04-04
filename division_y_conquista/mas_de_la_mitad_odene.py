def mas_de_la_mitad_rec(arr, start, end, counts=None):
    if counts is None:
        counts = {arr[i]: 0 for i in range(start, end+1)}
    
    # Caso base: contar el elemento
    if start == end:
        counts[arr[start]] = counts[arr[start]] + 1
        return arr[start], counts[arr[start]]
    
    # Divide
    mid = (start + end) // 2
    left_res, count_left = mas_de_la_mitad_rec(arr, start, mid, counts)
    right_res, count_right = mas_de_la_mitad_rec(arr, mid + 1, end, counts)

    if counts[left_res] >= counts[right_res]:
        return left_res, counts[left_res]
    else:
        return right_res, counts[right_res]

def mas_de_la_mitad(arr):
    size = len(arr)
    if size == 0:
        return False
    elif size == 1:
        return True
    candidato, apariciones = mas_de_la_mitad_rec(arr, 0, size - 1)

    if apariciones > size//2:
        return True
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 2, 2]
    arr_2 = [1, 2, 3, 4, 5]
    arr_3 = [1, 1, 1, 2, 3]
    arr_4 =[]
    arr_5 = [1]
    print(mas_de_la_mitad(arr))
    print(mas_de_la_mitad(arr_2))
    print(mas_de_la_mitad(arr_3))
    print(mas_de_la_mitad(arr_4))
    print(mas_de_la_mitad(arr_5))