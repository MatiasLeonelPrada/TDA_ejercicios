
def intercalar_ordenado(left, right):
    sorted_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Agregar elementos restantes
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

def merge_sort_rec(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort_rec(arr[:mid])
    right = merge_sort_rec(arr[mid:])
    return intercalar_ordenado(left, right)

def merge_sort(arr):
    return merge_sort_rec(arr)

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    print(merge_sort(arr))
