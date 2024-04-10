"""
Этот алгоритм подходит для сортировки целых чисел в определенном диапазоне. Он подсчитывает количество каждого элемента
и использует эту информацию для расположения каждого элемента непосредственно в его конечное место в
отсортированном массиве. Эффективен для сортировки малых чисел.

Худший и лучший случаи:
O(n + k).
Где k — диапазон чисел. Эффективность зависит от размера диапазона значений.

Оптимизация:
Можно уменьшить k, если возможно, например, когда известно, что диапазон чисел ограничен.
Также важно правильно управлять памятью для хранения подсчетов.
"""


def sortCNT(arr):
    if not arr:
        return arr
    max_val = arr[0]
    for item in arr:
        if item > max_val:
            max_val = item
    count_arr = [0] * (max_val + 1)
    for item in arr:
        count_arr[item] += 1

    sorted_arr = []
    for i in range(len(count_arr)):
        sorted_arr.extend([i] * count_arr[i])

    return sorted_arr


def counting_sort(arr):
    arr = arr.copy()
    max_val = max(arr)
    count_arr = [0] * (max_val+1)
    for item in arr:
        count_arr[item] += 1
    index = 0
    for i in range(len(count_arr)):
        while count_arr[i] > 0:
            arr[index] = i
            index += 1
            count_arr[i] -= 1
    return arr