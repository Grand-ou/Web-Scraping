
# check list
# 1.將傳入的字串中除了空格外的標點符號刪除
# 2.將字串按照各奇數位字元的ascii值相加,取最後兩位數,再由小到大排序
# 3.若2的情況相同則字串按照各偶數位字元的ascii值相加,取最後兩位數,再由大到小排序
# 4.將上述排序完的串列取倒數第三個字串，按字串內各個字元對應加權值(a:1 -> z:26)相乘
# 5.將4的結果取首4碼輸出，不足4碼則用0補齊

import re

def clean_line(line):
    pro = line[::-1]
    cnt = len(line)
    for i in line:
        cnt -= 1
        if i == ' ':
            continue
        if ord(i.lower()) < 97 or ord(i.lower()) > 122:
            pro = pro[:cnt] + '' + pro[cnt+1:]
        
    line = pro[::-1]
    line = line.split(' ')
    return line

def score_word(word):
    score_odd = 0
    score_even = 0
    cnt = 1
    for j in word:
        if cnt % 2 == 1:
            score_odd += ord(j)
            
        else:
            score_even += ord(j)
        cnt += 1
        # print(score_even)
    score_odd = score_odd%100
    score_even = 100 - (score_even%100)
    
    return(score_odd, score_even)

def get_score(line):
    line = line[::-1]
    pw = 1
    for i in line[2]:
            pw *= ord(i.lower()) - 96
    sum = pw
    sum = str(sum)
    while len(sum) < 4:
        sum = '0' + sum 
    sum = sum[:4]
    return sum

line = input()
line = clean_line(line)

line = sorted(line, key=lambda x: score_word(x))
# for i in line:
#     print(i, score_word(i))
# print(line)
print(get_score(line))