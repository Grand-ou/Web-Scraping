import math

N = int(input())
D = int(input())
M = int(input())
c = input()
r = input()
B = int(input())
p = input()
c = c.split(' ')
r = r.split(' ')
p = p.split(' ')

c = [int(x) for x in c]
r = [int(x) for x in r]
p = [int(x) for x in p]

date_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
k = date_count[M-1]
car_need = math.ceil(N/5)
room_need = math.ceil(N/4)
# print(car_need, room_need)
start_d = 0
find = False
for i in range(k - D):
    sum = 0
    for j in range(i, i+D):
        if c[j] < car_need:
            break
        if j < i+D-1 and r[j] < room_need:
            break
        if j < i+D-1:
            sum += room_need*p[j]
        if j == i+D-1 and sum <= B:
            find = True
    if find :
        start_d = i + 1
        break
if start_d == 0:
    print('None')
else:
    print(start_d)