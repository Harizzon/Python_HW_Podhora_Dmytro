from time import time


# "List Comprehension" is much faster then simple cycle for with append
def odds(y):
    time_start = time()
    odds = [x ** 3 for x in range(y) if x % 2 != 0]
    time_end = time()
    alert1 = print(f'Python finishes "List Comprehension" in {time_end - time_start}')
    squares = []
    time_start1 = time()
    for q in range(y):
        if q % 2 != 0:
            squares.append(q ** 2)
    time_end1 = time()
    alert2 = print(f'Python finishes usual cycle for with append in {time_end1 - time_start1}')
    return odds, alert1, squares, alert2


x = odds(50000)
print(x)
