python = {'ivanov','petrov','sidorov', 'pepe', "frog"}
front_end = {'ivanov','moxov','goroxov', "frog"}
full_stack ={'ivanov', 'pepe', "frog"}
java = {'ivanov','moxov','goroxov', 'pepe', "frog"}
# print(python - java) # Разность множеств
# print(python | front_end) # Объединение множеств
# print(python & java) # Пересечение множеств
print(f"Students who learning in all groups {python & java & full_stack & java}")
print(f"Students who is not learning in Front End {(python-front_end)}")
print(f'Students who learning Python and Java{python | java}')