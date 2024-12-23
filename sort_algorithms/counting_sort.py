#Cложность алгоритма:
# Лучший случай: O(n + k)
# Средний случай: O(n + k)
# Худший случай: O(n + k)
# Пространственная сложность: O(n + k)
# Линейная сложность: O(n) (подсчёт элементов)
# Логарифмическая сложность: Нет


from visual import visual_sorting
import logging
import matplotlib.pyplot as plt

def counting_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки подсчётом с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков
    """
    logging.info(f"Начальный массив: {arr}")

    max_val = max(arr)  # Находим максимальное значение
    min_val = min(arr)  # Находим минимальное значение
    range_of_elements = max_val - min_val + 1  # Диапазон элементов

    count = [0] * range_of_elements  # Массив для подсчета количества элементов
    output = [0] * len(arr)  # Массив для отсортированных элементов

    iteration = 0

    # Подсчёт количества вхождений каждого элемента
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        iteration += 1
        visual_sorting(count, f"Итерация {iteration}: подсчёт", iteration, update_rate, enable_visualization)

    # Изменяем массив count так, чтобы каждый элемент содержал сумму предыдущих
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        iteration += 1
        visual_sorting(count, f"Итерация {iteration}: модификация счётчика", iteration, update_rate, enable_visualization)

    # Заполняем выходной массив
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        iteration += 1
        visual_sorting(output, f"Итерация {iteration}: построение выходного массива", iteration, update_rate, enable_visualization)

    # Копируем отсортированный массив обратно в arr
    for i in range(len(arr)):
        arr[i] = output[i]

    logging.info(f"Конечный отсортированный массив: {arr}")
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
