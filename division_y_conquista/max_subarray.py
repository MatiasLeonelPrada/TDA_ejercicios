

def max_subarray(arr):
    if not arr:
        return []
    
    max_sum, start, end  = max_rec_sub_array(arr, 0, len(arr) - 1)

    return arr[start:end+1]


def max_rec_sub_array(arr, start, end):
    if start == end:
        return arr[start], start, end
    
    mid = (start + end) // 2
    left_res = max_rec_sub_array(arr, start, mid)
    right_res = max_rec_sub_array(arr, mid + 1, end)
    cross_res = max_cross_array(arr, start, mid, end) #esta es mi conquista

    # print(max(left_res, right_res, cross_res, key=lambda x: x[0]))
    return max(left_res, right_res, cross_res, key=lambda x: x[0])

def max_cross_array(arr, start, mid, end):

    sum_left = 0
    max_left = 0
    sum = 0
    for i in range(mid, start-1, -1):
        sum += arr[i]
        if sum > sum_left:
            sum_left = sum
            max_left = i

    sum_right = 0
    max_right = 0
    sum = 0
    for i in range(mid+1, end +1):
        sum += arr[i]
        if sum > sum_right:
            sum_right = sum
            max_right = i

    return (sum_left + sum_right, max_left, max_right)




    


if __name__ == "__main__":
    # [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
    # [5, 3, -5, 4, -1] ->  [5, 3]
    # [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
    # [5, -4, 2, 4] -> [5, -4, 2, 4]
    # [-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]
    # print(max_subarray([5, 3, 2, 4, -1]))
    # print(max_subarray([5, 3, -5, 4, -1]))
    # print(max_subarray([5, -4, 2, 4, -1]))
    # print(max_subarray([5, -4, 2, 4]))
    print(max_subarray([-3, 4, -1, 2, 1, -5]))
    # print(max_subarray([5, 3]))