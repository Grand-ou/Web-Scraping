# ... 的地方代表自行填寫的地方

#自己定義函數
def same_row(i,j): return ... #看是否為同列
def same_col(i,j): return ... #看是否為同行
def same_area(i,j): return ... #看定義的區域是否有重複的數字
def solveSudoku(board):
    ans = []
    idx = ... # 看看board哪裡有空格存在idx
    if ... #idx沒有空格就結束
        return board

    exclude = ... # 把前三個定義的條件拿來找同行、同列、同區的 set ，可自動找到還可以填哪個數字
    for m in set('12345') - exclude:
        ans += ... #加上m後遞迴
    return ans

#接著開始input題目要求的區塊
area = [] #將題目的區塊做成一維的list，same_area(i,j)就可以判斷是否在同個區塊了
for i in range(5):
    line = input()
    line = line.split(' ')
    row = []
    for j in line[i]:
        axis = j.split(',')
        row.append((axis[0], axis[1]))
    area.append(row)
# 放入題目
space = [[0, False] for i in range (25)] #即將放入數字
while True:
    try: 
        line = input()
        line = line.split(' ')
        space
    except:
        break

# 解題
Ans = solveSudoku(...)

# 列印
if len(Ans) ... :
    ...
        print(...)   
else:
    print(...)