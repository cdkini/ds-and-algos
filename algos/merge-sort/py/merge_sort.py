def merge(arrA, arrB):
    res = [0 for _ in range(len(arrA)+len(arrB))]
    a = 0
    b = 0
    i = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            res[i] = arrA[a]
            a += 1
        else:
            res[i] = arrB[b]
            b += 1
        i += 1

    while a < len(arrA):
        res[i] = arrA[a]
        a += 1
        i += 1

    while b < len(arrB):
        res[i] = arrB[b]
        b += 1
        i += 1

    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))
