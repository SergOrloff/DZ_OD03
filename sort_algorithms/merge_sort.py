#Cложность алгоритма:
# Лучший случай: O(n log n)
# Средний случай: O(n log n)
# Худший случай: O(n log n)
# Пространственная сложность: O(n)
# Линейная сложность: O(n) (слияние)
# Логарифмическая сложность: O(log n) (деление массива)

from visual import visual_sorting
import logging
import time
import matplotlib.pyplot as plt

def merge_sort(arr, enable_visualization=True, update_rate=10, iteration=0):
    """
    Реализация сортировки слиянием с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков
    - iteration: текущая итерация для визуализации
    """
    logging.info(f"Начальный массив: {arr}")  # Логирование начального состояния массива
    start_time = time.time()  # Замер времени начала сортировки

    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        L = arr[:mid]  # Левая часть
        R = arr[mid:]  # Правая часть

        # Рекурсивно сортируем левую и правую части
        iteration = merge_sort(L, enable_visualization, update_rate, iteration)
        iteration = merge_sort(R, enable_visualization, update_rate, iteration)

        # Слияние отсортированных частей
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            iteration += 1
            visual_sorting(arr, f"Итерация {iteration}: слияние", iteration, update_rate, enable_visualization)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            iteration += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            iteration += 1

    end_time = time.time()  # Конец отсчета времени
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None  # Финальная визуализация
    return iteration
