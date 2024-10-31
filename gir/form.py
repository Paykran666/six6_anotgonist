import random

# Генерируем два списка случайных чисел
list1 = [random.randint(1, 10) for _ in range(5)]
list2 = [random.randint(1, 10) for _ in range(5)]

print("Список 1:", list1)
print("Список 2:", list2)

# 1. Создание списка, содержащего все элементы обоих списков
list3_all = list1 + list2
print("Список 3 (все элементы):", list3_all)

# 2. Создание списка, содержащего все элементы без повторений
list3_unique = list(set(list1 + list2))
print("Список 3 (без повторений):", list3_unique)

# 3. Создание списка, содержащего только общие элементы
list3_common = list(set(list1) & set(list2))
print("Список 3 (общие элементы):", list3_common)

# 4. Создание списка, содержащего только уникальные элементы
list3_unique_each = list(set(list1) ^ set(list2))
print("Список 3 (уникальные элементы):", list3_unique_each)

# 5. Создание списка, содержащего минимальное и максимальное значения
list3_min_max = [min(list1), max(list1), min(list2), max(list2)]
print("Список 3 (минимальное и максимальное):", list3_min_max)



