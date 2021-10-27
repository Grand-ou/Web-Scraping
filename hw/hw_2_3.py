num = input()
line = num.split(',')
num = int(input())
ind1 = 0
ind2 = 0
for i in range(0, len(line)):
    find = False
    for j in range(i + 1, len(line)):
        if int(line[i]) + int(line[j]) == num:
            ind1 = i
            ind2 = j
            find = True
            break
    if find == True:
        break
print('['+str(ind1) + ', ' + str(ind2)+']')
