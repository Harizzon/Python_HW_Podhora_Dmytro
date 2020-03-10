# task briliant 
def bril(x):
    i = 1
    b = x -2
    while (i <= x):
        if i < x:
            print(" " * int(((x - i)/2)) + "*" * i +" " * int(((x - i) / 2)))
            i += 2
        elif i == x:
            print("*" * i)
            i += 2
    while b > 0:
        print(" " * int(((x - b)/2)) + "*" * b +" " * int(((b - i) / 2)))
        b -= 2
bril(11)

# Task 2 from project Euler
l1 = [1, 2]
i = 2
n = 1
while i < 400:
    l1.append(l1[i - 1] + l1[i - 2])
    i += 1
res = filter(lambda x: x % 2 == 0, l1)
# print(list(res))
