# In this program we check what type of year what we set

a = int(input("Set year "))

if (a % 4) == 0 and (a % 100) != 0 or (a % 400) == 0:
    print("Leep-year")
else:
    print("Ordinary year")

