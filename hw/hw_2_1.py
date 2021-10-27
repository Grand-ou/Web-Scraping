num = input()
line = num.split(',')
number = ''
for i in line:
    number += i
num = int(number) + 1
num = str(num)
cnt = 0
print('[', end = '')
for i in num:
    print(i, end = '')
    cnt += 1
    if cnt != len(num):
        print(',', end = '')
print(']', end = '')