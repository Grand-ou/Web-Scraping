
commodity = {}
customer = {}
read = True
n = 0
m = 0
r = input()
r = r.split()
n = int(r[0]) 
m = int(r[1])
for i in range(n):
    line = input().split(' ')
    commodity[line[0]] = [int(line[1]), []]
for i in range(m):
    line = input().split(' ')
    if line[0] in customer.keys():
        customer[line[0]][1] += int(line[2])
        customer[line[0]][0] += int(line[2])*commodity[line[1]][0]
        if line[1] in customer[line[0]][2].keys():
            customer[line[0]][2][line[1]] += int(line[2])
        else:
            customer[line[0]][2][line[1]] = int(line[2])
            
    else:
        customer[line[0]] = [int(line[2])*commodity[line[1]][0], int(line[2]), {line[1]:int(line[2])}]
    if line[0] in commodity[line[1]][1]:
        pass
    else:
        commodity[line[1]][1].append(line[0])
    # print('HIHI')
    # print(commodity[line[1]][1])
while(read):
    try:
        line = input()
    except:
        break
    line = line.split(' ')
    if line[0] == 'A':
        cnt = customer.get(line[1], 0)
        if cnt == 0:
            print(cnt)
        else:
            print(cnt[0])
        
    if line[0] == 'B':
        cnt = customer.get(line[1], 0)
        if cnt == 0:
            print(cnt)
        else:
            print(cnt[2].get(line[2], 0))
        
    if line[0] == 'C':
        temp = commodity.get(line[1], 'Check again!')
        if temp == 'Check again!':
            print(0)
        elif not temp[1]:
            print(0)
        else:
            cnt = 0
            for i in sorted(commodity.get(line[1], 'Check again!')[1]):
                if cnt != 0:
                    print(',', end='')
                cnt += 1
                print(i, end='')
            print('\n', end='')
                
        
        

    
