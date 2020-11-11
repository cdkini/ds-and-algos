def cyclic_sort(array):
    if not array or len(array) <= 1:
        return array

    i = 0
    while i < len(array):
        while array[i] != i:
            temp = array[i]
            array[i], array[temp] = array[temp], array[i]
        i += 1

    return array

