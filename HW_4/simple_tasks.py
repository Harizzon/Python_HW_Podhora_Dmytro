# task 1
def task1(x, y):
    """
    This is simple function shows what number is bigger
    :param x: integer number
    :param y: integer number
    :return: string
    """
    try:
        if x > y:
            print(f"The {x} is bigger")
        else:
            print(f"The {y} is bigger")
    except UnboundLocalError:
        print("Unbound Local Error,please use only integer number ")
    except TypeError:
        print("Type Error, please use only integer number")
    except SyntaxError:
        print("Syntax Error, please use integer number, such as 13")


# task 2
def task2(a, b, c):
    if c <= b <= a:
        print(a, b, c, sep=" ")
    elif c <= a <= b:
        print(b, a, c, sep=" ")
    elif b <= c <= a:
        print(a, c, b, sep=" ")
    elif a <= c <= b:
        print(b, c, a, sep=" ")
    elif a <= b <= c:
        print(c, b, a, sep=" ")
    elif b <= a <= c:
        print(c, a, b, sep=" ")


# task 3
def task3(x):
    if x // 1 == x and x // x == 1 and type(x) == int:
        print(f"Number {x} is integer")
    else:
        print(f"Number {x} is float")


# or
def task3_1(x):
    return not x % 1


# or

def task3_2(x):
    try:
        return int(x) == float(x)
    except ValueError:
        return -1


# task 4
def task4(*args):
    for x in args:
        if x % 2 != 0 and x % 3 == 0:
            print(x)
        else:
            print("No appropriate numbers")


# task 5

# for number in range(101):
#     if (10 < number <= 90) and number % 2 != 0 and number % 7 != 0:
#         print(number, end="\t")

# or

# from random import randint
#
# x = randint(0, 101)
# if (10 < x <= 90) and x % 2 != 0 and x % 7 != 0:
#     print(f"\n {x}")
# else:
#     print("\nNo suitable numbers")

# task 6

from random import randint

l = [x for x in range(randint(6, 66))]
i = 0
results = []
while i < len(l):
    results.append(f"Num {i} we meet {l.count(i)}", )
    i += 1
# print(results)

# or

res1 = []
l1 = [66, 25, 333, 333, 1, 1234, 566, 25, 333, 333, 1, 1234, 566, 25, 333, 333, 1, 1234, 566, 25, 333, 333, 1, 1234, 5]
for x in l1:
    res1.append(f'We meet {x}, {l1.count(x)} times')
# print(set(res1))

# task 7

# l_list = []
# while True:
#     ent_number = int(input("Enter the integer number, please "))
#     l_list.append(ent_number)
#     if ent_number > 1000:
#         print(f"Sum of numbers {sum(l_list)}")
#         print(f"Average {sum(l_list) / len(l_list)}")
#         print(f"Max number {max(l_list)}")
#         print(f"Min number {min(l_list)}")
#         break

# task 8

# double_list = [x*2 for x in range(66)]
# print(double_list)
#
# # or
# print([x*2 for x in range(13)])
