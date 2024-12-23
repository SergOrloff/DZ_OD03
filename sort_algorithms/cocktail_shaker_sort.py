#Cложность алгоритма:
# Лучший случай: O(n) (если массив отсортирован)
# Средний случай: O(n²)
# Худший случай: O(n²)
# Пространственная сложность: O(1)
# Линейная сложность: O(n) в лучшем случае
# Логарифмическая сложность: Нет

from visual import visual_sorting
import logging
import matplotlib.pyplot as plt

def cocktail_shaker_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация шейкерной сортировки (Cocktail Shaker Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    logging.info(f"Начальный массив: {arr}")

    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    iteration = 0

    plt.ion() if enable_visualization else None

    while swapped:
        swapped = False

        # Проход слева направо (как в обычной пузырьковой сортировке)
        for i in range(start, end):
            iteration += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                logging.debug(f"Обмен элементов {arr[i]} и {arr[i + 1]}")

            visual_sorting(arr, f"Итерация {iteration}: проход слева направо", iteration, update_rate, enable_visualization)

        if not swapped:
            break

        end -= 1
        swapped = False

        # Проход справа налево (обратный проход)
        for i in range(end - 1, start - 1, -1):
            iteration += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                logging.debug(f"Обмен элементов {arr[i]} и {arr[i + 1]}")

            visual_sorting(arr, f"Итерация {iteration}: проход справа налево", iteration, update_rate, enable_visualization)

        start += 1

    logging.info(f"Конечный отсортированный массив: {arr}")
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
