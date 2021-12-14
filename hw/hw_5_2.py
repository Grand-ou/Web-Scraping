line = input()
line = line.split(' ')
x = int(line[0])-1
y = int(line[1])-1
def many(x, y):
    z = x + y
    r = 1
    for i in range(1, z+1):
        r *= i
    for i in range(1, x+1):
        r /= i
    for i in range(1, y+1):
        r /= i
    return r
line = input().split(' ')
x1 = int(line[0])
y1 = int(line[1])

x2 = x - x1
y2 = y - y1
re = many(x, y) - (many(x1, y1) * many(x2, y2))
print(int(re))