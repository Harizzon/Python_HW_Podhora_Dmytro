l = [12, 13, 17, 2, 56, 78, 876, 1, 4, 9, 0]


# main problem in this version of FizzBuzz is:
# You need to set number for Fizz and for Buzz in the function
def fizzbuzz(n, f=3, b=5):
    """
    You can set Fizz and Buzz. Parameters by default Fizz = 3 and Buzz = 5
    :param n: number
    :param f: Fizz
    :param b: Buzz
    :return: string with FizzBuzz
    """
    if n % f == 0 and n % b == 0:
        return 'FizzBuzz'
    elif n % f == 0:
        return 'Fizz'
    elif n % b == 0:
        return 'Buzz'
    else:
        return str(n)
help(fizzbuzz)

print(list(map(fizzbuzz, l)))
