money = [500, 100, 10, 1]

given_bills = {500: '0', 100: "0", 10: "0", 1: "0"}
w_money = total_money = int(input())

while w_money > 0:
    for x in money:
        if (w_money // x) > 0:
            rez = w_money // x
            given_bills[x] = rez
            w_money -= rez * x
print(f"""
We've given to the client this amount of money {total_money}
500 bills: {given_bills[500]},
100 bills: {given_bills[100]},
10 bills:  {given_bills[10]},
1 bills:   {given_bills[1]}

""")
