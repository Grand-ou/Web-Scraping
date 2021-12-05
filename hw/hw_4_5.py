def same_row(i,j): return (i//5 == j//5)
def same_col(i,j): return (i-j) % 5 == 0
def same_block(i,j,area): return (area[i] == area[j])

def solveSudoku(board, area):
    ans = []
    idx = board.index(0) if 0 in board else -1
    if idx == -1: #解完了
        return [board]
    exclude = {board[j] for j in range(25) if same_row(idx,j) or same_col(idx,j) or same_block(idx,j, area)}
    for m in set('12345')-exclude:
        ans += solveSudoku(board[:idx]+[m]+board[idx+1:], area)
    return ans

#接著開始input題目要求的區塊
area = [0 for i in range (25)] #將題目的區塊做成一維的list，same_area(i,j)就可以判斷是否在同個區塊了
cnt = 1
for i in range(5):
    line = input()
    line = line.split(' ')
    # print(line)
    for j in line:
        axis = j.split(',')
        # print(j)
        # print(int(axis[0])*5 + int(axis[1]), len(area))
        area[int(axis[0])*5 + int(axis[1])] = cnt
    
    cnt += 1
# 放入題目
space = [0 for i in range (25)] #即將放入數字
while True:
    try: 
        line = input()
        if line == 'e':
            break
        line = line.split(' ')

        axis = line[0].split(',')
        space[int(axis[0])*5 + int(axis[1])] = line[1]
    except:
        break

# 解題
try:
    Ans = solveSudoku(space, area)
    cnt = 0
    for i in Ans[0]:

        if cnt != 0 and cnt%5 == 0:
            print()
        elif cnt != 0 :
            print(' ', end='')
        print(i, end='')
        cnt += 1
except:
    print('no solution!')
# print(Ans)
