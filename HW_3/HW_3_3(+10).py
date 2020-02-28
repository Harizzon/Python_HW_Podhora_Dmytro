money = [500, 100, 10, 20, 1]
money.reverse()
given_bills = {500: '0', 100: "0", 20: "0", 10: "0", 1: "0"}
w_money = total_money = int(input())

while w_money > 0:
    for x in money:
        if x == 1 or x == 10 or x == 20:
            if (w_money // x) > 0:
                rez = w_money // x
                if rez >= 10:
                    rez = 10
                    given_bills[x] = 10
                else:
                    rez = w_money // x
                w_money -= x * rez
        else:
            if (w_money // x) > 0:
                rez = w_money // x
                w_money -= rez * x
                given_bills[x] = rez

print(f"""
We've given to the client this amount of money {total_money}
500 bills: {given_bills[500]},
100 bills: {given_bills[100]},
20 bills:  {given_bills[20]},
10 bills:  {given_bills[10]},
1 bills:   {given_bills[1]}

""")
