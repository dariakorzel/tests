def runner_up_score(n):
    my_list = list(n)
    results = []
    for element in my_list:
        if 2 < element < 10:
            results.append(element)
            results.sort()

    print(results[-2])