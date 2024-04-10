"""
Это алгоритм "разделяй и властвуй", который разделяет массив на две части, рекурсивно сортирует их,
а затем сливает в один отсортированный массив. Он обеспечивает стабильное время выполнения
O(nlogn) для любых данных.

Худший и лучший случаи:
O(nlogn).
Сортировка слиянием всегда работает с этой сложностью,
так как она делит массив пополам и сливает их.

Оптимизация:
Для небольших подмассивов (например, менее 10-15 элементов) может быть эффективнее переключиться
на сортировку вставками, которая работает быстрее на малых наборах данных.
"""


def merge(A, start, mid, end):
    left = A[start:mid]
    right = A[mid:end]
    k = start
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1


def sortMRG(A, start=0, end=None):
    if end is None:
        end = len(A)
    if end - start > 1:
        mid = (start + end) // 2
        sortMRG(A, start, mid)
        sortMRG(A, mid, end)
        merge(A, start, mid, end)
    return A


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr