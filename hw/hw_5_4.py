def ID_gender(city, num):
    first = ['BNZ','AMW','KLY','JVX','HU','GT','FS','ER','DOQ','CIP']
    cert = 0
    cnt = -1
    for i in first:
        cnt += 1
        if city in i:
            cert += cnt
            break
    cnt = 7
    for i in num:
        i = int(i)
        cert += i * cnt
        # print(i*cnt)
        if cnt > 1:
            cnt -= 1
    # print(cert)
    if cert%10 == 2:
        return 'Male'
    elif cert%10 == 4:
        return 'Female'
    
    
line = input()
print(ID_gender(line[0], line[1:]))