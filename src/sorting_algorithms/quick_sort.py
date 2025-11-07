def quick_sort(arr):
    """
    Быстрая сортировка
    """
    if len(arr) <= 1:
        return arr

    arr_copy = arr.copy()
    _quick_sort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def _quick_sort_helper(arr, low, high):
    if low < high:
        # Индекс разделения
        pi = _partition(arr, low, high)

        # Рекурсивно сортируем элементы до и после разделения
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)

def _partition(arr, low, high):
    # Выбираем последний элемент как опорный
    pivot = arr[high]

    # Индекс меньшего элемента (указывает на правильную позицию pivot)
    i = low - 1

    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Помещаем опорный элемент в правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
