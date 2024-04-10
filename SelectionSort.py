"""
В этом алгоритме на каждом шаге ищется минимальный (или максимальный) элемент из неотсортированной части массива
и обменивается с первым неотсортированным элементом. Он неэффективен для больших списков.

Худший и лучший случаи:
O(n^2).
Алгоритм всегда проходит через каждый элемент,
чтобы найти минимальный и переместить его в начало неотсортированной части.

Оптимизация:
Эффективных оптимизаций для этого алгоритма практически нет,
так как его основная идея требует полного обхода массива.
"""


def sortSLC(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr