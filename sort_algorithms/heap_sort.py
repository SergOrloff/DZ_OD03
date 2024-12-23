#Cложность алгоритма:
# Лучший случай: O(n log n)
# Средний случай: O(n log n)
# Худший случай: O(n log n)
# Пространственная сложность: O(1)
# Линейная сложность: Нет
# Логарифмическая сложность: O(log n) (операции вставки/извлечения в куче)


from visual import visual_sorting
import logging
import matplotlib.pyplot as plt
import time

def heap_sort(arr, enable_visualization=True, update_rate=10):
    """
    Реализация пирамидальной сортировки (Heap Sort) с визуализацией и логированием.

    Parameters:
    - arr: массив для сортировки
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления графиков
    """
    logging.info(f"Начальный массив: {arr}")
    start_time = time.time()

    n = len(arr)
    iteration = 0  # Счётчик итераций

    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, iteration, enable_visualization, update_rate)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        logging.debug(f"Перемещение элемента {arr[i]} в конец массива")
        iteration += 1
        visual_sorting(arr, f"Итерация {iteration}: перемещение корня", iteration, update_rate, enable_visualization)
        heapify(arr, i, 0, iteration, enable_visualization, update_rate)

    end_time = time.time()  # Конец отсчета времени
    logging.info(f"Время выполнения: {end_time - start_time:.4f} секунд")
    visual_sorting(arr, "Конечный отсортированный массив", iteration, update_rate=1, enable_visualization=enable_visualization)
    plt.show(block=True) if enable_visualization else None
    return arr

def heapify(arr, n, i, iteration, enable_visualization=True, update_rate=10):
    """
    Функция для преобразования поддерева с корнем в элементе i в кучу.

    Parameters:
    - arr: массив
    - n: размер кучи
    - i: индекс корня поддерева
    - iteration: текущая итерация для визуализации
    - enable_visualization: включать/выключать визуализацию
    - update_rate: частота обновления визуализации
    """
    largest = i  # Инициализация наибольшего элемента как корня
    left = 2 * i + 1  # Левый дочерний элемент
    right = 2 * i + 2  # Правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний элемент больше наибольшего элемента
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        logging.debug(f"Обмен элементов: {arr[i]} и {arr[largest]}")
        iteration += 1
        visual_sorting(arr, f"Итерация {iteration}: heapify", iteration, update_rate, enable_visualization)
        heapify(arr, n, largest, iteration, enable_visualization, update_rate)
