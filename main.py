import timeit
import random
from tabulate import tabulate


def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data[:])
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Повертаємо індекс знайденого елемента
    return -1  # Якщо елемент не знайдений

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Обчислюємо позицію за формулою інтерполяції
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # Якщо елемент не знайдений


def insertion_sort(lst):
    # Проходимо по всіх елементах починаючи з другого
    for i in range(1, len(lst)):
        key = lst[i]  # поточний елемент
        j = i - 1
        # Зсуваємо елементи масиву, які більші за поточний
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key  # Вставляємо поточний елемент на відповідне місце
    return lst



def merge_sort(arr):
    # Базовий випадок: масив довжини 1 або менше вже відсортований
    if len(arr) <= 1:
        return arr

    # Знаходимо середину масиву
    mid = len(arr) // 2

    # Рекурсивно сортуємо ліву та праву половини
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Об'єднуємо відсортовані половини
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Зливаємо два масиви
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Додаємо залишки елементів з лівого або правого масиву, якщо такі є
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Заміна елементів
                swapped = True
        if not swapped:  # Якщо на даному проході не було замін, завершити роботу
            break
    return arr

# Впровадження Shell Sort
# Сортування Шелла - це вдосконалена версія сортування вставками, яка використовує інтервали для покращення швидкості
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Початковий інтервал
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Зменшення інтервалу
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Заміна елементів
    return arr

# Функція для вимірювання часу виконання функції
def measure_time(func, *args):
    start_time = timeit.default_timer()
    result = func(*args)
    end_time = timeit.default_timer()
    exec_time = end_time - start_time
    return result, exec_time

# Генеруємо випадкові дані для тестування
data_smallest = [random.randint(0, 1_000) for _ in range(10)]
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_big = [random.randint(0, 1_000) for _ in range(1_000)]
data_largest = [random.randint(0, 1_000) for _ in range(10_000)]

# Генерація частково відсортованих даних
data_almost_sorted = sorted(data_largest)
data_almost_sorted[int(len(data_almost_sorted) * 0.9):] = reversed(data_almost_sorted[int(len(data_almost_sorted) * 0.9):])

# Генерація реверсивно відсортованих даних
data_reversed = list(reversed(data_largest))

# Функція для знаходження елементів, які є тільки в одному масиві
def unique_elements(arrA, arrB):
    setA = set(arrA)
    setB = set(arrB)
    
    # Елементи, які є тільки в A
    unique_in_A = setA - setB
    
    # Елементи, які є тільки в B
    unique_in_B = setB - setA
    
    # Об'єднуємо ці елементи
    result = list(unique_in_A.union(unique_in_B))
    
    return result

# Знаходження унікальних елементів між масивами data_smallest і data_small
unique_smallest_and_small = unique_elements(data_smallest, data_small)

# Виведення результатів
print("data_smallest:", data_smallest)
print("data_small:", data_small)
print("Елементи, що присутні тільки в data_smallest або тільки в data_small:", unique_smallest_and_small)

test_data = [
    ("Random Smallest", data_smallest),
    ("Random Small", data_small),
    ("Random Big", data_big),
    ("Random Largest", data_largest),
    ("Almost Sorted", data_almost_sorted),
    ("Reversed", data_reversed)
]

search_functions = [
    ("Linear Search", linear_search),
    ("Interpolation Search", interpolation_search)
]

search_target = random.randint(0, 1_000)  # Випадкове число для пошуку
pre_sort_search_table = []
headers_search = ["Search Algorithm", "Array Type", "Target Found", "Time (s)"]

for search_name, search_func in search_functions:
    for array_name, data in test_data:
        _, exec_time = measure_time(search_func, data.copy(), search_target)
        found = search_func(data.copy(), search_target) != -1
        pre_sort_search_table.append([search_name, array_name, found, f"{exec_time:.6f}"])

print("\nПошук у невідсортованих масивах:")
print(tabulate(pre_sort_search_table, headers=headers_search, tablefmt="github"))

sorting_functions = [
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Timsort (built-in sorted)", sorted),
    ("Bubble Sort", bubble_sort),
    ("Shell Sort", shell_sort),
    ("Selection Sort", selection_sort)
]

# Проведення тестування та виведення результатів
sorted_data = [(name, sorted(data.copy())) for name, data in test_data]  # Копія для сортування
table = []
headers_sort = ["Sorting Algorithm"] + [name for name, _ in test_data]

for sort_name, sort_func in sorting_functions:
    row = [sort_name]
    for _, data in test_data:
        _, exec_time = measure_time(sort_func, data.copy())  # Використовуємо копію масиву для збереження оригінальних даних
        row.append(f"{exec_time:.6f}")
    table.append(row)

print("\nРезультати сортування:")
print(tabulate(table, headers=headers_sort, tablefmt="github"))

# Пошук у відсортованих масивах
post_sort_search_table = []

for search_name, search_func in search_functions:
    for array_name, data in sorted_data:
        _, exec_time = measure_time(search_func, data.copy(), search_target)
        found = search_func(data.copy(), search_target) != -1
        post_sort_search_table.append([search_name, array_name, found, f"{exec_time:.6f}"])

print("\nПошук у відсортованих масивах:")
print(tabulate(post_sort_search_table, headers=headers_search, tablefmt="github"))