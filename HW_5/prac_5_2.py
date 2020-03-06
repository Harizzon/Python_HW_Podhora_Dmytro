with open('D:\Courses\Python_HW1\eng_string.txt', 'r') as eng_str:
    for x in eng_str:
        l = str(x)
new_l = l.split(" ")
print()


# simple function with "while"
def count(x):
    i = 0
    result = []

    while i < len(new_l):
        result.append(f"We've met {new_l[i].upper()}: {new_l.count(new_l[i])}")
        i += 1
    return set(result)


# print(list(map(count, new_l)))


# using module collections
from collections import Counter

counted_words = Counter(new_l)
# print(counted_words)

# using dictionary
array_d = {}.fromkeys(new_l, 0)
for a in new_l:
    array_d[a] += 1

# print(array_d)

