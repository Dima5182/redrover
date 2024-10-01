def sum_ignore_non_numbers(items):
    '''
    Суммирует все числа из списка, игнорирую нечисловые значения.

    :param items: Список с различными типами данных.
    :return: Сумма чисел из списка.
    '''

    total = 0
    for i in items:
        if isinstance(i, (int, float)):
            total = total + i
    return total

def is_triangle(a, b, c):
    '''
    Проверяет возможность создания треугольника с заданными длинами сторон.

    :param a: Длина 1ой стороны треугольника.
    :param b: Длина 2ой стороны треугольника.
    :param c: Длина 3ей стороны треугольника.
    :return: True если возможно создать треугольник, False если невозможно создать треугольник
    '''

    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def average(*args):
    '''
    Считает среднее арифметическое произвольного количества чисел.

    :param args: Произвольное количество чисел.
    :return: Среднее арифметическое значение.
    '''

    count = 0
    total = 0
    for i in args:
        count = count + 1
        total = total + i
    if count > 1:
        return total / count
    elif count == 0:
        return 0

def common_strings(list1, list2, ignore_case=True):
    '''
    Проверяет совпадение строк в 2ух списках взависимости от переданного параметра ignore_case.

    :param list1: Первый список строк.
    :param list2: Второй список строк.
    :param ignore_case: Параметр для игнорирования или учета регистра строк.
    :return: Список совпадающих строк.
    '''

    list_common = []
    if ignore_case == True:
        for i in list1:
            if i.lower() in list2:
                list_common.append(i.lower())
    elif ignore_case == False:
        for i in list1:
            if i in list2:
                list_common.append(i)
    return list_common