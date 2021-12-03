import sys
purchase = {}
read = True
while(read):
    
    info = input()
    if info == 'end':
        break
    info = info.split(',')
    info[0] = (info[0][len(info[0])-3:]) + ' ' + info[1]
    # print(info[0])
    purchase[info[0]] = info[2]
time = 0

while(read):
    try:
        search = input()
    except:
        break
    
    print(purchase.get(search, 'Check again!'))