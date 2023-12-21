def binary_search(arr, value):
    min = 0
    max = len(arr) - 1
    while(min <= max):
        midpoint = (max - min) // 2 + min
        if(arr[midpoint] > value):
            max = midpoint - 1
        elif(arr[midpoint] < value):
            min = midpoint + 1
        else:
            # print(f"Индекс искомого числа {midpoint}")
            return midpoint

    return -1

array = [1, 3, 4, 6, 7, 8, 10, 13, 14]
print(binary_search(array, 4))