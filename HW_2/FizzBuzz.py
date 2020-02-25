a = int(input("Fizz "))
b = int(input("Buzz "))
c = int(input("number "))

i = 1
results = []
while i <= c:
    if i % a == 0 and i % b == 0:
        results.append("FB")
    elif i % a == 0:
        results.append("F")
    elif i % b == 0:
        results.append("B")
    else:
        results.append(i)
    i += 1
print(results)