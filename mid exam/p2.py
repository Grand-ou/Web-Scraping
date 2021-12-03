n = int(input())
k = int(input())
cntA = 0
cnta = 0
cnt1 = 1

for i in range(1, n + 1):
    num = i + k - 1
    row = ''
    if i % 3 == 1:
        ordi = ord('A')
        temp = cntA
        for j in range(temp, temp + num):
            cnt = j % 26
            row += chr(ordi + cnt)
            cntA += 1

    elif i % 3 == 2:
        ordi = ord('a')
        temp = cnta
        for j in range(temp, temp + num):
            cnt = j % 26
            row += chr(ordi + cnt)
            cnta += 1
    else:
        ordi = ord('0')
        temp = cnt1
        for j in range(temp, temp + num):
            cnt = j % 10
            row += chr(ordi + cnt)
            cnt1 += 1
    print(row)