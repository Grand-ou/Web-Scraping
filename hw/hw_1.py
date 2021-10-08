


row1 = input()
depart = input()
score = row1.split(',')
for i in range (5):
    score[i] = int(score[i])

def accounting (s):
    if (s[0] + s[1] + s[2] + s[3]) >= 57 and (s[0] >= 15):
        return True
    else:
        return False

def health (s):
    if (s[1] + s[2] + s[3]) >= 38 :
        return True
    else:
        return False
    
def economic (s):
    if (s[4] + s[3]) >= 26 and (s[2] >= 15):
        return True
    else:
        return False

def programming (s):
    if (s[1] + s[4]) >= 27 and (s[2] >= 15):
        return True
    else:
        return False

def allocate(name, score):
    if name == '會計系':
        if accounting(score):
            print(1)
        else:
            print(0)
    elif name == '公衛系':
        if health(score):
            print(1)
        else:
            print(0)
    elif name == '經濟系':
        if economic(score):
            print(1)
        else:
            print(0)

    elif name == '資工系':
        if programming(score):
            print(1)
        else:
            print(0)
allocate(depart, score)