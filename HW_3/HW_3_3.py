results = []
a= int(input())
b = int(input())


# open file to take the numbers
f = open('D:\Courses\Python_HW1\\numbers.txt', 'r')
l = [line.strip() for line in f]

# We're making conversion from str to int
# also we can do it in this ways:

# L = [[map(int, i.split())] for i in l]

# values = []
# for string in l:
#     for value in string.split():
#         values.append(int(value))

# I've used this method
l_int = [int(k) for i in l  for k in i.split(" ")]

# FizzBuzz
for i in l_int:
    if int(i) % a == 0 and int(i) % b == 0:
        results.append("FB")
    elif int(i) % a == 0:
        results.append("F")
    elif int(i) % b == 0:
        results.append("B")
    else:
        results.append(int(i))
print(results)



#saving results
save_res = open('D:\Courses\Python_HW1\\results.txt', 'w')
for index in results:
    save_res.write(str(index) + "\t")
save_res.close()


f.close()

