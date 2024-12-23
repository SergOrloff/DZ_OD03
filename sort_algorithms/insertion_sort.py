#Cложность алгоритма:
# Лучший случай: O(n) (если массив почти отсортирован)
# Средний случай: O(n²)
# Худший случай: O(n²)
# Пространственная сложность: O(1)
# Линейная сложность: O(n) в лучшем случае
# Логарифмическая сложность: Нет

from visual import visual_sorting
import logging
import time
import matplotlib.pyplot as plt

def insertion_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки вставками с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков
    """
    logging.info(f"Начальный массив: {arr}")  # Логирование начального массива
    start_time = time.time()  # Замер времени начала сортировки

    iteration = 0
    for i in range(1, len(arr)):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Сдвигаем элементы вправо
            j -= 1
            iteration += 1
            visual_sorting(arr, f"Итерация {i}: вставка элемента {key}", iteration, update_rate, enable_visualization)
        arr[j + 1] = key

    end_time = time.time()  # Замер времени окончания сортировки
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
