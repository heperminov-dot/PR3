# підключення необхідної бібліотеки
import numpy as np


# ---------------------- ЗАВДАННЯ 1 ----------------------

def digit_count(K):
    """Повертає кількість цифр додатного числа K"""
    return len(str(abs(K)))


def digit_count_list(list_of_k):
    """Функція для обробки списку чисел відповідно до функції за варіантом"""
    out_data = []
    for k in list_of_k:      # для кожного числа у вхідному списку
        out_data.append(digit_count(k))
    return out_data


def task1_standart():
    """Стандартна версія обробки: цикл + append"""
    in_data = []
    try:
        in_num = int(input("Введіть кількість елементів: "))
        for i in range(in_num):
            temp = int(input(f"{i+1} element: "))
            in_data.append(temp)
    except ValueError:
        print("Помилка введення!")
    else:
        print("Кількість цифр:", digit_count_list(in_data))


def task1_list_comprehension():
    """Обробка з використанням list comprehension"""
    try:
        in_num = int(input("Введіть кількість елементів: "))
        in_data = [int(input(f"{i+1} element: ")) for i in range(in_num)]
    except ValueError:
        print("Помилка введення!")
    else:
        out_data = [digit_count(k) for k in in_data]
        print("Кількість цифр:", out_data)


def task1_lambda():
    """Обробка списку за допомогою lambda + map"""
    try:
        in_data = list(map(lambda e: int(e), input("Enter numbers: ").split()))
    except ValueError:
        print("Помилка введення!")
    else:
        out_data = list(map(lambda k: digit_count(k), in_data))
        print("Кількість цифр:", out_data)


# ---------------------- ЗАВДАННЯ 2 (Matrix10) ----------------------

def matrix10(filename):
    """
    Зчитування матриці розміру M×N з файлу.
    1) Знаходить номер стовпця з мінімальною сумою
    2) Повертає номер стовпця, мінімальну суму та
       матрицю, відсортовану по кожному стовпцю у спадному порядку.
    """

    with open(filename, 'r') as f:
        # перший рядок: M N
        first_line = f.readline().split()
        try:
            M = int(first_line[0])
            N = int(first_line[1])
        except (IndexError, ValueError):
            print("Wrong file format!")
            return -1, -1, None

        # зчитування матриці
        matrix = np.loadtxt(filename, skiprows=1, max_rows=M)
        print("Вхідна матриця:")
        print(matrix)

        # 1) знайти суму кожного стовпця
        col_sums = np.sum(matrix, axis=0)

        # індекс стовпця з мінімальною сумою
        min_col_index = int(np.argmin(col_sums)) + 1  # +1 щоб відповідати умові "номер"
        min_sum_value = float(np.min(col_sums))

        # 2) сортування кожного стовпця у спадному порядку
        sorted_matrix = -np.sort(-matrix, axis=0)

        return min_col_index, min_sum_value, sorted_matrix


def task2():
    """Введення імені файлу, виклик matrix10(), виведення результатів."""
    filename = input("Enter filename (.txt): ")

    min_col, min_sum, sorted_matrix = matrix10(filename)

    print(f"\nНомер стовпця з мінімальною сумою: {min_col}")
    print(f"Мінімальна сума: {min_sum}")
    print("Відсортована матриця (по стовпцях, спадання):")
    print(sorted_matrix)
    