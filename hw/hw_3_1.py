num = int(input())
ls = []
for i in range(num):
    n = input()
    if len(n) < 9:
        continue
    if n[9:len(n)] == '@ntu.edu.tw':
        n = n[0:9]
    if len(n) != 9:
        continue
    n = n[0].upper() + n[1:len(n)]
    if n[0] not in['B', 'R', 'D', 'F'] :
        continue
    if n in ls:
        continue
    ls.append(n)
for i in ls:
    print(i)