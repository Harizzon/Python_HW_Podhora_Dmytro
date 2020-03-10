# students = {"Alex": 21, "John": 12, "Sam": 211, "Swan": 133, "Nick": 666}
# dict_1 = dict(Nick=21, Sam=12, Vlad=122)
# max_point = []
# res= 0
# for key, value in students.items():
#     if value > res:
#         res = 0
#         res += value
#         max_point.clear()
#         max_point.append(f"Max point is {value} for student {key}")
#     elif value < res:
#         res = 0
#         res += value
#         max_point.clear()
#         max_point.append(f"Max point is {value} for student {key}")
# # print(max_point)
stud = dict.fromkeys((["Ivanov", "Petrov", "Smirmof"]))

stud["Ivanov"] = (9, 10, 7)
stud["Petrov"] = (7, 10, 9)
stud["Smirmof"] = (6, 6, 6)

# stud_res = dict.fromkeys((["Ivanov", "Petrov", "Smirmof"]))
avar_val=dict()
for students in stud:
    avar_val[students] = sum(stud[students]) / len(stud[students])

max_point = []
res= 0

for key, value in avar_val.items():
    if value > res:
        res = 0
        res += value
        max_point.clear()
        max_point.append(f"Max point is {value} for student {key}")
    elif value < res:
        res = 0
        res += value
        max_point.clear()
        max_point.append(f"Max point is {value} for student {key}")
print(max_point)