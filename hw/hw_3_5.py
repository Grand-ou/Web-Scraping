
def win(nums):
    ls = [50 for i in range(len(nums))]
    ls[len(ls) - 1] = 0
    d = [50 for i in range(len(nums))]
    for i in range(len(nums)-2, -1, -1):
        for j in range(i + 1, len(ls)):
            if ls[j] + 1 < ls[i]:
                ls[i] = ls[j] + 1
                d[i] = j
    path = []
    rounds = ls[0]
    t = True
    k = d[0]
    while k == 50:
        path.append(d[k])
        k = d[k]
    return [rounds, path]