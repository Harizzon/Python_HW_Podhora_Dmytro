#      s  m  l  xl  xxl xxxl
# rus  40 42 46 50  54  56
# USA   6  8  12 16  20  24
# italy 38 40 44 48  52
# france 36 38 42 46 50

def sizes(n, counrty):
    """
    You can put size and country
    :param n: s,m,l,xl,xxl
    :param counrty:rus, usa, italy, france
    :return: size
    """
    rus = dict(s=40, m=42, l=46, xl=50, xxl=54)
    usa = dict(s=6, m=8, l=12, xl=16, xxl=20)
    italy = dict(s=38, m=40, l=44, xl=48, xxl=52)
    france = dict(s=36, m=38, l=42, xl=46, xxl=50)
    if counrty == 'rus':
        for keys in rus.keys():
            if keys == n:
                print(rus[n])
        return rus[n]
    elif counrty == 'usa':
        for keys in usa.keys():
            if keys == n:
                print(usa[n])
        return usa[n]
    elif counrty == 'italy':
        for keys in italy.keys():
            if keys == n:
                print(italy[n])
        return italy[n]
    elif counrty == 'france':
        for keys in france.keys():
            if keys == n:
                print(france[n])
            return france[n]
sizes("xxl", "italy")

