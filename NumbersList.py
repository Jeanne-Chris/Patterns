def find_distinct_numbers(distinct_input):
    result = []
    for n in distinct_input:
        if distinct_input.count(n) == 1:
            result.append(n)
    return print(result)


def find_double_numbers(double_input):
    result = []
    for n in double_input:
        if double_input.count(n) == 2:
            result.append(n)
            result.sort()
    return print(result)


def find_multiple_numbers(multiple_input):
    result = []
    for n in multiple_input:
        if multiple_input.count(n) >= 3:
            result.append(n)
            result.sort()
    return print(result)


find_distinct_numbers([12, 7, 5, 80, 3, 80, 5, 7, 12, 2, 60, 7, 60])
find_double_numbers([4, 7, 5, 8, 9, 8, 5, 7, 4, 2, 6, 7, 6])
find_multiple_numbers([4, 8, 5, 8, 4, 8, 5, 8, 4, 4, 7, 6, 6, 6, 9, 9, 9])
