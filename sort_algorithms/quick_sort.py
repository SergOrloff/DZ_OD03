#Cложность алгоритма:
# Лучший случай: O(n log n)
# Средний случай: O(n log n)
# Худший случай: O(n²)
# Пространственная сложность: O(log n) (в среднем), O(n) (в худшем случае)
# Линейная сложность: O(n) (разбиение массива)
# Логарифмическая сложность: O(log n) (количество уровней рекурсии)

from visual import visual_sorting
import matplotlib.pyplot as plt


def quick_sort(arr, start=0, end=None, iteration=0, enable_visualization=True, update_rate=10):
    """
    Реализация быстрой сортировки (Quick Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - start: начальный индекс
    - end: конечный индекс
    - iteration: текущая итерация
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков
    """
    if end is None:
        end = len(arr) - 1  # Определяем конец массива, если он не указан

    if start >= end:
        return iteration  # Базовый случай для завершения рекурсии

    pivot_index = partition(arr, start, end)  # Опорный элемент для разделения массива
    iteration += 1
    visual_sorting(arr, f"Разделение по опорному элементу {arr[pivot_index]}", iteration, update_rate,
                      enable_visualization)

    # Рекурсивно сортируем левую и правую части
    iteration = quick_sort(arr, start, pivot_index - 1, iteration, enable_visualization, update_rate)
    iteration = quick_sort(arr, pivot_index + 1, end, iteration, enable_visualization, update_rate)

    return iteration


def partition(arr, start, end):
    """
    Функция для разделения массива относительно опорного элемента (pivot).

    Parameters:
    - arr: массив для сортировки
    - start: начальный индекс
    - end: конечный индекс
    """
    pivot = arr[end]  # Опорный элемент — последний элемент массива
    i = start - 1  # Индекс меньшего элемента

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Обмен элементов

    arr[i + 1], arr[end] = arr[end], arr[i + 1]  # Помещаем опорный элемент на своё место
    return i + 1  # Возвращаем индекс опорного элемента


def finalize_visualization(enable_visualization=True):
    """
    Финализирует визуализацию (если включена).

    Parameters:
    - enable_visualization: флаг для включения/выключения визуализации
    """
    if enable_visualization:
        plt.show(block=True)
