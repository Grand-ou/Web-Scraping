n = int(input())
find = True
for i in range(2, int(n/2) + 1):
    if n % i == 0:
        for j in range(2, int(i/2) + 1):
            if i % j == 0:
                # find = False
                break
            if j == int(i/2):
                find = False
    if find == False:
        break
if find == False:
    print('False')
else:
    print('True')