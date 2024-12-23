#Cложность алгоритма:
# Лучший случай: O(n log n) (в зависимости от разрывов)
# Средний случай: O(n log² n)
# Худший случай: O(n²)
# Пространственная сложность: O(1)
# Линейная сложность: Нет
# Логарифмическая сложность: O(log n) (в зависимости от последовательности разрывов)

from visual import visual_sorting
import logging
import time
import matplotlib.pyplot as plt

def shell_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки Шелла (Shell Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")
    start_time = time.time()

    n = len(arr)
    gap = n // 2  # Начальный разрыв
    iteration = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Сдвигаем элементы вправо, чтобы вставить текущий элемент на нужную позицию
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                iteration += 1
                visual_sorting(arr, f"Итерация {iteration}: сортировка с разрывом {gap}", iteration, update_rate, enable_visualization)
            arr[j] = temp
        gap //= 2  # Уменьшаем разрыв

    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
