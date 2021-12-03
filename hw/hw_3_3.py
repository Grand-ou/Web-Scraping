def printm(map):
    for i in range(len(map)):
        if i != 0:
            print('\n', end='')
        for j in range(len(map[0])):
            
            if map[i][j] == 1:
                print('Ｏ', end='')
            elif map[i][j] == 0:
                print('＊', end='')

                
def paint(i, j, a, b, map):
    z = 1
    temp = i
    i = min(i, a)
    a = max(i, a, temp)
    temp = j
    j = min(j, b)
    b = max(j, b, temp)
    # print(i, j, a, b)
    if i == a:

        for n in range(j, b+1, z):

            map[i][n] = 0
    elif j == b:
        for n in range(i, a+1, z):
            map[n][j] = 0
    else:
        for n in range(abs(a-i)):
            map[i+n][j+n] = 0
    return map


line = input()
line = line.split(' ')
x = int(line[0])
y = int(line[1])
num = int(line[2])
map = [[1 for i in range(y)] for j in range(x)]

a = -1
b = -1

for n in range(num):
    co = input()
    coor = co.split(' ')
    i = x - int(coor[1]) - 1
    j = int(coor[0])
    
    if a == -1 and b == -1:
        map[i][j] = 0

    else:
        map = paint(i, j, a, b, map)
    a = i
    b = j

printm(map)
