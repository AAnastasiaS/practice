#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Кейс №1: Сумма отрицательных элементов, расположенных между максимальным и минимальным элементами массива.
Автор: (впишите своё ФИО)
Описание:
- Скрипт запрашивает у пользователя массив чисел (ввод на одной строке через пробел).
- Находит индексы ПЕРВЫХ вхождений максимума и минимума.
- Складывает только отрицательные элементы между ними (не включая сами max/min).
- Печатает подробный результат.
Пример:
Ввод:  5 -1 7 -3 2 -4 10 6
Max=10 на позиции 6, Min=-4 на позиции 5 → элементы между ними: [] → сумма=0
"""
from typing import List, Tuple

def sum_negative_between_min_max(a: List[float]) -> Tuple[float, int, int, float, float, List[float]]:
    if not a:
        raise ValueError("Массив пуст. Введите хотя бы одно число.")
    max_val = max(a)
    min_val = min(a)
    i_max = a.index(max_val)  # индекс первого вхождения максимума
    i_min = a.index(min_val)  # индекс первого вхождения минимума

    left = min(i_max, i_min) + 1
    right = max(i_max, i_min)      # отрезок [left:right) — между max и min

    middle = a[left:right] if left < right else []

    neg_sum = sum(x for x in middle if x < 0)
    return neg_sum, i_max, i_min, max_val, min_val, middle

def main():
    print("КЕЙС №1: Сумма отрицательных элементов между MAX и MIN")
    print("Введите элементы массива на ОДНОЙ строке, через пробел (например: 5 -1 7 -3 2 -4 10 6)")
    line = input("Ввод: ").strip()
    if not line:
        print("Пустой ввод. Завершение.")
        return
    # Преобразуем в список чисел (поддерживает целые и вещественные)
    try:
        arr = [float(x.replace(",", ".")) for x in line.split()]
    except ValueError:
        print("Ошибка: ввод содержит нечисловые значения. Введите числа через пробел.")
        return

    try:
        neg_sum, i_max, i_min, max_val, min_val, middle = sum_negative_between_min_max(arr)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    print("\nРезультаты:")
    print(f"- Массив: {arr}")
    print(f"- Максимум: {max_val} (индекс {i_max})")
    print(f"- Минимум: {min_val} (индекс {i_min})")
    if middle:
        print(f"- Элементы между ними (без max/min): {middle}")
    else:
        print("- Между max и min нет элементов.")
    print(f"- Сумма отрицательных элементов между max и min: {neg_sum}")

if __name__ == "__main__":
    main()
