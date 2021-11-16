# -*- coding: cp1251 -*-


def comparator(a, b):
    return a['age'] < b['age']


def merge_sort(arr, compare=comparator):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# print(merge_sort([{'telephone': '+7-(909)-591-91-17', 'height': '1.86', 'inn': '464635336120', 'passport_number': 289548, 'university': 'Санкт-Петербургский государственный политехнический университет', 'age': 29, 'academic_degree': 'Магистр', 'worldview': 'Буддизм', 'address': 'ул. Богоявленская 568'}, {'telephone': '+7-(968)-105-45-80', 'height': 0.46, 'inn': '409425782961', 'passport_number': 754910, 'university': 'Бауманское МГТУ', 'age': 38, 'academic_degree': 'Доктор наук', 'worldview': 'Пантеизм', 'address': 'Аллея Петропавловская 279'}]))
