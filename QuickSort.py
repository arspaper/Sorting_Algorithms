"""
Также использует стратегию "разделяй и властвуй". Алгоритм выбирает опорный элемент и переупорядочивает элементы так,
что все меньшие опорного оказываются перед ним, а все большие — после. Затем рекурсивно применяется к подмассивам.

Худший случай:
O(n^2).
Это случается при неудачном выборе опорного элемента
или, например, когда массив уже отсортирован.

Лучший случай:
O(nlogn).
Это достигается, когда массив уже отсортирован.
Каждый элемент требует только одного сравнения.

Оптимизация:
Использование "медианы трех" для выбора опорного элемента,
также для небольших подмассивов можно переключиться на сортировку вставками.
"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def sortQCK(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        sortQCK(arr, low, pi - 1)
        sortQCK(arr, pi + 1, high)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)