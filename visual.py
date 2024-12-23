import matplotlib.pyplot as plt

def visual_sorting(arr, title, iteration=0, update_rate=10, enable_visualization=True):
    """
    Функция для визуализации процесса сортировки с использованием matplotlib

    Parameters:
    - arr: массив для сортировки
    - title: заголовок для отображения на графике
    - iteration: текущая итерация
    - update_rate: частота обновления графика
    - enable_visualization: флаг для включения/выключения визуализации
    """
    if not enable_visualization:
        return

    # Обновляем график только через определённое количество итераций
    if iteration % update_rate == 0:
        plt.clf()  # Очищаем текущий график
        plt.bar(range(len(arr)), arr, color='blue')  # Построение графика
        plt.title(title)  # Устанавливаем заголовок
        plt.pause(0.01)  # Включаем паузу для отображения обновлений

def finalize_visualization(enable_visualization=True):
    """
    Функция для завершения визуализации с блокировкой, если она включена.

    Parameters:
    - enable_visualization: флаг для включения/выключения визуализации
    """
    if enable_visualization:
        plt.show(block=True)  # Отображаем финальный график
