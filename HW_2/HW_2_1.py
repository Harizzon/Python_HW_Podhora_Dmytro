# practice task 1

def task1(x):
    if x % 2 == 0:
        res = "Even"
    else:
        res = "odd"
    return res


# practice task 2

def task2(x):
    if x % 2 != 0 and x % 3 == 0 and x % 5 == 0 and x % 9 != 0:
        result = "Yes"
    else:
        result = "No"
    return result


#  practice task 3

def task3(x):


    import math
    results = []
    for i in range(1, math.ceil(math.sqrt(x) + 1)):
        if not x % i:
            results.append(i)
    results.append(x//i)
    return results

#  practice task 4

def task4(x):
    import math

    results = []
    for i in range(1, math.ceil(math.sqrt(x) + 1)):
        if x % i == 0:
            results.append(i)
            results2 = f"Ranks {len(str(x))}"
    return results, results2

