#Cложность алгоритма: O(n^2)
# Лучший случай: O(n) (если массив отсортирован)
# Средний случай: O(n²)
# Худший случай: O(n²)
# Пространственная сложность: O(1)
# Линейная сложность: O(n) в лучшем случае
# Логарифмическая сложность: Нет

from visual import visual_sorting
import logging
import time
import matplotlib.pyplot as plt

def bubble_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация сортировки пузырьком с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков (раз в N итераций)
    """
    n = len(arr)
    logging.info(f"Начальный массив: {arr}")

    start_time = time.time()  # Замер времени начала сортировки

    iteration = 0  # Для отслеживания количества итераций
    for i in range(n):
        swapped = False  # Флаг для отслеживания перестановок
        logging.debug(f"Начало {i + 1}-й итерации. Массив: {arr}")

        for j in range(0, n - i - 1):
            iteration += 1  # Увеличиваем счётчик итераций
            logging.debug(f"Сравнение элементов {arr[j]} и {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                logging.debug(f"Обмен элементов {arr[j]} и {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Установка флага, так как произошла перестановка

                # Визуализируем текущее состояние массива после обмена
                visual_sorting(arr, f"Итерация {i + 1}, обмен {arr[j]} и {arr[j + 1]}", iteration, update_rate, enable_visualization)

        if not swapped:
            logging.info(f"Массив отсортирован досрочно на {i + 1}-й итерации.")
            break

    end_time = time.time()  # Замер времени окончания сортировки
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")

    # Финальная визуализация
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr
