
n = int(input())
line = [[1]]
for i in range(1, n):
    line.append([])
    line[i].append(1)
    for j in range(1, i):
        line[i].append(line[i-1][j] + line[i-1][j-1])
    line[i].append(1)
print('[', end = '')
count = 0
for i in line:
    if count != 0:
        print(', ' , end = '')
    count += 1
    print('[', end = '')
    cnt = 0
    for j in i:
        if cnt != 0:
            print(', ' , end = '')
        cnt += 1
        print(j, end = '')
    print(']', end = '')
print(']', end = '')

