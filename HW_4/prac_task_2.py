import random
sur_name = ["Herrington", "Li", "Zane", "Darkholme", "Dirk"]
name = ["Billy", "Danny", "Irwing", "Ioka", "Van"]

i = 0
names = []

x = random.randint(0, 5)
y = random.randint(0, 5)
# crating persons
while i < 50:
    names.append(random.choice(name) + " " + random.choice(sur_name))
    i += 1

# counting
count_names = []
for name in names:
    count = names.count(name)
    count_names.append(f"We've met {name}, {str(count)} times.")
persons_met = set(count_names)
print(persons_met)
