numbers = [1, 3, 4, 6, 7, 8]
new_sum = 0
for i in numbers:
    new_sum += i
print(new_sum)

i = 0
new_sum = 0
while i <= len(numbers):
    for i in numbers:
        new_sum += i

print(new_sum)