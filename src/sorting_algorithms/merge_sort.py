def merge_sort(arr):
    """
    Сортировка слиянием
    """
    if len(arr) <= 1:
        return arr.copy()

    arr_copy = arr.copy()
    _merge_sort_helper(arr_copy)
    return arr_copy

def _merge_sort_helper(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивная сортировка обеих половин
        _merge_sort_helper(left_half)
        _merge_sort_helper(right_half)

        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверяем, не остались ли элементы в левой половине
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Проверяем, не остались ли элементы в правой половине
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
