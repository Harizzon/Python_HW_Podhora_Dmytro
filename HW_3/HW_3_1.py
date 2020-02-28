
list1 = []
f = open("D:\Courses\Python_HW1\prac3_1.py", 'r')
for line in f:
    list1.append(line)
list1.reverse()
for i in list1:
    print(i)

f.close()


# without revers

# list1 = []
# f = open("D:\Courses\Python_HW1\prac3_1.py", 'r')
# for line in f:
#    list1.append(line)

# for i in list1:
#    print(i)

# f.close()
