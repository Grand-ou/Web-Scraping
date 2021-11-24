left = ['LF', 'SS', '3B']
right = ['RF', '1B', '2B']
side = input()
time = int(input())
l = 0
r = 0
for i in range(time):
    area = input()
    if area in left:
        l += 1
    if area in right:
        r += 1
# print(l, r)
if l < r :
    if side == 'L':
        print('拉打')
    else :
        print('推打')
elif r < l:
    if side == 'R':
        print('拉打')
    else :
        print('推打')