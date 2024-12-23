#Cложность алгоритма:
# Лучший случай: O(n * k)
# Средний случай: O(n * k)
# Худший случай: O(n * k)
# Пространственная сложность: O(n + k)
# Линейная сложность: O(n) (по каждому разряду)
# Логарифмическая сложность: Нет напрямую, но может зависеть от вложенного алгоритма

from visual import visual_sorting
import logging
import time
import matplotlib.pyplot as plt

def counting_sort_for_radix(arr, exp, enable_visualization, update_rate, iteration):
    """
    Вспомогательная функция для сортировки поразрядным методом с использованием подсчёта (для каждого разряда).

    Parameters:
    - arr: массив для сортировки
    - exp: текущий разряд для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков
    - iteration: текущая итерация
    """
    n = len(arr)
    output = [0] * n  # Массив для отсортированных элементов
    count = [0] * 10  # Массив для подсчета по текущему разряду

    # Подсчёт количества элементов для текущего разряда
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Изменяем count так, чтобы каждый элемент содержал сумму предыдущих
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Заполняем выходной массив
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        iteration += 1

    # Копируем отсортированный массив обратно в arr
    for i in range(len(arr)):
        arr[i] = output[i]

    return iteration

def radix_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация поразрядной сортировки (Radix Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков
    """
    logging.info(f"Начальный массив: {arr}")
    start_time = time.time()

    max_val = max(arr)  # Находим максимальный элемент массива
    iteration = 0
    exp = 1  # Начинаем с младшего разряда

    while max_val // exp > 0:
        iteration = counting_sort_for_radix(arr, exp, enable_visualization, update_rate, iteration)
        exp *= 10  # Переходим к следующему разряду

    end_time = time.time()
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
