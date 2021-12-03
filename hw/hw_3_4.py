n = int(input())
l = -1
ls = []
t = True
f = False
for i in range(n):
    row = input()
    row = row.split(' ')
    if l != -1 and l != len(row):
        print(-1)
        t = False
        break
    l = len(row)
    ls.append(row)
x = len(ls)
y = len(ls[0])



if t :
    ye = True
    if len(ls) == len(ls[0]):
        
        for i in range(x):
            for j in range(y):
                if ls[i][j] != ls[j][i]:
                    ye = False
        if ye:
            print(135)
            f = True
        if not f:
            ye =True
            for i in range(x):
                for j in range(y):
                    if ls[i][j] != ls[i][y-j-1]:
                        ye =False
            if ye:
                
                print(90)
                f = True
    if not f:
        ye =True
        for i in range(x):
            for j in range(y):
                # print(ls[i][j] , ls[i][y-j-1], y, j)
                if ls[i][j] != ls[i][y-j-1]:
                    ye =False
        if ye:
            print(90)
            # print('hi')
            f = True
    if not f:
        ye =True
        if len(ls) == len(ls[0]):
            
            for i in range(x):
                for j in range(y):
                    if ls[i][j] != ls[x - i -1][y - j - 1]:
                        ye =False
            if ye:
                print(45)
                f = True
    if not f:
        ye =True
        for i in range(x):
            for j in range(y):
                if ls[i][j] != ls[x-i-1][j]:
                    ye =False
        if ye:
            print(0)
            f = True
if not f:
    print(-1)
