from random import randint
km = [x * randint(3,97) for x in range(34) if x > 23 ]
time_hours = [x **2 for x in range(16) if x > 5]
speed = [x / y for x in km for y in time_hours if x / y > (sum(km) / sum(time_hours))]
print(speed)
print(len(speed))
