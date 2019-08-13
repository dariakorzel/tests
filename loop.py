def square(i):
    return i * i


def numbers(j):
    my_numbers = range(j)
    results = []

    if 20 > j > 0:
        for element in my_numbers:
            results.append(square(element))
        return results
