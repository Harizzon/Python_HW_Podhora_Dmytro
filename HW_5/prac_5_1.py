def to_lower(string):

    print(str(string).lower())

def to_upper(string):
    print(str(string).upper())
list_lower = ["DFSDFDS", 'SDFFDSADS', "qwWERTTY", 'QWErtYU']
list_upper = ['dfdf', 'dfsds', 'sanbox', 'qwerty']

def square(x):
    return x**2
# list_new = [12, 11, 22, 155, 21]
# print(list(map(lambda x: x**2, list_new)))

def is_Prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return n**2
prime_num = list(range(0, 30))
prime_sum = list(map(is_Prime, prime_num))
print(prime_sum)