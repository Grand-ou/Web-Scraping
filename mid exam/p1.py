az = 'AZ'
md = 'moderna'
bnt = 'BNT'
h = '高端'
type = input()
date = input()
time = date.split('/')

time = [int(x) for x in time]
year = time[0]
month = time[1]
day = time[2]
date = day
for i in range(1, month):
    # print(date)
    if i == 2:
        date += 28
    elif i in [4, 6, 9, 11]:
        date += 30
    else:
        date += 31
    # print(i, date)
# print(date, date + 70)
if type == h:
    date = date + 28
else:
    date = date + 70
sec_month = 0
for i in range(1, 13):
    temp = date
    if i == 2:
        date -= 28
    elif i in [4, 6, 9, 11]:
        date -= 30
    else:
        date -= 31
    if date < 0:
        date = temp
        sec_month = i 
        break
if sec_month < 10:
    sec_month = '0' + str(sec_month)
if date < 10:
    date = '0' + str(date)
print(str(year) + '/' + str(sec_month) + '/' + str(date) )