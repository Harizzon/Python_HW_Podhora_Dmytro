name1, name2 = input("Enter name of first player "), input("Enter name of second player ")
print('You have 10 sticks, you can take from 1 to 3 sticks,'
      'the  person who take the last stick lose.\n'
      f'We have two players. Player {name1.title()} you can start.')
sticks = 10
while True:
    x1 = int(input(f"Enter number from 1 to 3, {name1.title()}. Remaining {sticks}. "))
    sticks -= x1
    x2 = int(input(f"{name2.title()}, please enter the number Remaining {sticks}. "))
    sticks -= x2
    if sticks - x1 == 0:
        print(f"Congratulation {name1.title()}, you WIN")
        break
    elif sticks - x2 == 0:
        print(f"Congratulations {name2.title()}, you WIN")
        break