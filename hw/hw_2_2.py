def find_prefix(word_lst):
    num = input()
    line = num.split(',')
    cnt = 1000000000000000000000
    for i in line:
        # print(len)
        cnt = min(cnt, len(i))
        if len (i) == 0:
            cnt = 0
    for i in range(1, cnt + 1):
        find = False
        for j in range(1, len(line)):
            # print(line[j][0:i], line[0][0:i], line[j][0:i] == line[0][0:i])
            if line[j][0:i] != line[0][0:i]:
                cnt = i - 1
                find = True
                break
        if find == True:
            break

    # print(cnt, line[0])
    if cnt == 0:
        print('No common')
    else:
        print(line[0][0:cnt])