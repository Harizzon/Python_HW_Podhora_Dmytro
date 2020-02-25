a, b, c = int(input("Fizz ")), int(input("Buzz ")), int(input("number "))
results = []
for i in range(1, c+1):
    if i % a == 0 and i % b == 0:
        results.append("FB")
    elif i % a == 0:
        results.append("F")
    elif i % b == 0:
        results.append("B")
    else:
        results.append(i)
print(results)