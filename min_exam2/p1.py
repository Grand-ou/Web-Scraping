def count_price(guest):

    import math

    total_cost = 0

    def seven_cost(a, b, c):
        cost = count_cost(a) + count_cost(b) + count_cost(c)
        return cost

    def count_cost(p):
        cost = 699
        if p[0] == 'O':
            cost -= 100
        for i in p :
            if i == '7':
                cost -= 70
        if int(p[7:]) % 7 == 0:
            cost -= 77
        if cost < 0:
            cost = 0
        return cost

    def group_cost(a, b, c):
        cost = 699 * 3
        if a[0] == 'O':
            cost -= 100
        if b[0] == 'O':
            cost -= 100
        if c[0] == 'O':
            cost -= 100
        if a[1] == b[1] and b[1] == c[1]:
            cost *= 0.8
        if a[0] != b[0] and a[0] != c[0] and c[0] != b[0] :
            cost *= 0.8
        
        return cost



    p1 = guest[0]
    p2 = guest[1]
    p3 = guest[2]

    if group_cost(p1, p2, p3) < seven_cost(p1, p2, p3):
        return math.ceil(group_cost(p1, p2, p3))
    else:
        return math.ceil(seven_cost(p1, p2, p3))