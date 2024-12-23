import tkinter as tk
from tkinter import ttk
import logging
from sort_algorithms.bubble_sort import bubble_sort
from sort_algorithms.selection_sort import selection_sort
from sort_algorithms.quick_sort import quick_sort, finalize_visualization
from sort_algorithms.insertion_sort import insertion_sort
from sort_algorithms.merge_sort import merge_sort
from sort_algorithms.heap_sort import heap_sort
from sort_algorithms.counting_sort import counting_sort
from sort_algorithms.radix_sort import radix_sort
from sort_algorithms.cocktail_shaker_sort import cocktail_shaker_sort
from sort_algorithms.shell_sort import shell_sort

arrays = {
    "Bubble Sort (Сортировка пузырьком)": [64, 34, 25, 12, 22, 11, 90],
    "Selection Sort (Сортировка выбором)": [64, 25, 12, 22, 11],
    "Quick Sort (Быстрая сортировка)": [3, 6, 8, 10, 1, 2, 1],
    "Insertion Sort (Сортировка вставками)": [12, 11, 13, 5, 6],
    "Merge Sort (Сортировка слиянием)": [12, 11, 13, 5, 6, 7],
    "Heap Sort (Пирамидальная сортировка)": [12, 11, 13, 5, 6, 7],
    "Counting Sort (Подсчетная сортировка)": [4, 2, 2, 8, 3, 3, 1],
    "Radix Sort (Поразрядная сортировка)": [170, 45, 75, 90, 802, 24, 2, 66],
    "Cocktail Shaker Sort (Шейкерная сортировка)": [5, 1, 4, 2, 8, 0, 2],
    "Shell Sort (Сортировка Шелла)": [12, 34, 54, 2, 3],
}

# Функция для настройки уровня логирования
def set_logging_level(level):
    """
    Устанавливает уровень логирования в зависимости от выбора пользователя
    """
    logging.getLogger().setLevel(level)
    logging.info(f"Уровень логирования установлен на: {logging.getLevelName(level)}")

# Функция для запуска выбранного алгоритма
def run_selected_sort():
    """
    Запускает выбранный алгоритм сортировки и применяет к нему визуализацию
    """
    selected_algorithm = algorithm_var.get()
    enable_visualization = visualization_var.get()
    update_rate = int(update_rate_var.get())  # Частота обновления графика

    logging.info(f"Запуск {selected_algorithm} с визуализацией={enable_visualization} и update_rate={update_rate}")

    # Копируем массив для сортировки, чтобы не изменять оригинальный массив
    array = arrays[selected_algorithm].copy()

    # Определяем, какой алгоритм был выбран, и вызываем соответствующую функцию
    if selected_algorithm == "Bubble Sort (Сортировка пузырьком)":
        bubble_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Selection Sort (Сортировка выбором)":
        selection_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Quick Sort (Быстрая сортировка)":
        quick_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Insertion Sort (Сортировка вставками)":
        insertion_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Merge Sort (Сортировка слиянием)":
        merge_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Heap Sort (Пирамидальная сортировка)":
        heap_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Counting Sort (Подсчетная сортировка)":
        counting_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Radix Sort (Поразрядная сортировка)":
        radix_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Cocktail Shaker Sort (Шейкерная сортировка)":
        cocktail_shaker_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)
    elif selected_algorithm == "Shell Sort (Сортировка Шелла)":
        shell_sort(array, enable_visualization=enable_visualization, update_rate=update_rate)

# Создание графического интерфейса с помощью Tkinter
root = tk.Tk()
root.title("Sorting Algorithms")

# Увеличиваем размер окна
root.geometry("735x450")

# Добавляем иконку в заголовок окна (замените путь на иконку, если она есть)
root.iconbitmap("ico/sort.ico")  # Если у вас есть иконка, раскомментируйте эту строку

# Задаем фон
root.configure(bg="#ADFF2F")

# Фрейм для размещения всех элементов
main_frame = ttk.Frame(root, padding="10 10 10 10", relief="groove")
main_frame.pack(fill="both", expand=True)

# Заголовок
header_label = ttk.Label(main_frame, text="Алгоритмы сортировки", font=("Helvetica", 18, "bold"), background="#ADFF2F")
header_label.grid(column=0, row=0, columnspan=2, pady=(10, 20))

# Устанавливаем стиль для виджетов
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12, "bold"), foreground="#333")
style.configure("TButton", font=("Helvetica", 12, "bold"), background="#5c85d6", foreground="#fff")
style.configure("TCombobox", font=("Helvetica", 12, "bold"), padding=5)
style.configure("TCheckbutton", font=("Helvetica", 12, "bold"), foreground="#333")

# Выпадающий список для выбора алгоритма сортировки
algorithm_var = tk.StringVar()
algorithm_label = ttk.Label(main_frame, text="Выберите алгоритм сортировки:", background="#f8f8f8", font=("Arial", 12, "bold"))
algorithm_label.grid(column=0, row=1, sticky=tk.W, pady=5)

algorithm_menu = ttk.Combobox(main_frame, textvariable=algorithm_var, width=41, font=("Arial", 11, "bold"))
algorithm_menu['values'] = list(arrays.keys())  # Устанавливаем значения для выбора
algorithm_menu.current(0)  # Выбираем первый алгоритм по умолчанию
algorithm_menu.grid(column=1, row=1, pady=5)

# Чекбокс для включения/выключения визуализации
visualization_var = tk.BooleanVar(value=True)
visualization_check = ttk.Checkbutton(main_frame, text="Включить визуализацию", variable=visualization_var)
visualization_check.grid(column=0, row=2, columnspan=2, pady=5)

# Поле для ввода частоты обновления графика
update_rate_var = tk.StringVar(value="5")
update_rate_label = ttk.Label(main_frame, text="Частота обновления графика (N итераций):",
                              background="#f8f8f8", font=("Arial", 12, "bold"))
update_rate_label.grid(column=0, row=3, sticky=tk.W, pady=5)

update_rate_entry = ttk.Entry(main_frame, textvariable=update_rate_var, width=10, font=("Arial", 11, "bold"))
update_rate_entry.grid(column=1, row=3, pady=5)

# Добавляем возможность выбора уровня логирования
log_level_var = tk.StringVar()
log_level_label = ttk.Label(main_frame, text="Выберите уровень логирования:",
                            background="#f8f8f8", font=("Arial", 12, "bold"))
log_level_label.grid(column=0, row=4, sticky=tk.W, pady=5)

log_level_menu = ttk.Combobox(main_frame, textvariable=log_level_var, width=10, font=("Arial", 11, "bold"))
log_level_menu['values'] = ['DEBUG', 'INFO']  # Добавляем значения для уровня логирования
log_level_menu.current(1)  # INFO по умолчанию
log_level_menu.grid(column=1, row=4, pady=5)

# Кнопка для настройки уровня логирования
set_log_button = ttk.Button(main_frame, text="Установить уровень логирования",
                            command=lambda: set_logging_level(getattr(logging, log_level_var.get())))
set_log_button.grid(column=0, row=5, columnspan=2, pady=10)

# Кнопка для запуска сортировки
run_button = ttk.Button(main_frame, text="Запустить сортировку", command=run_selected_sort)
run_button.grid(column=0, row=6, columnspan=2, pady=20)

# Настройка логирования по умолчанию (INFO уровень)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO,
                    handlers=[
                        logging.FileHandler("sorting.log"),
                        logging.StreamHandler()
                    ]
                    )

# Настраиваем стили для кнопок и элементов
style = ttk.Style()
style.configure("TButton", font=("Arial", 11, "bold"), padding=6, background="#4CAF50", foreground="black")  # Изменили цвет текста на черный
style.map("TButton", background=[('active', '#45a049')], foreground=[('active', 'black')])  # Цвет текста при наведении тоже черный

# Запуск главного цикла интерфейса
root.mainloop()
