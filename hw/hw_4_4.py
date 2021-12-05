
def check(coordinate, position, board):

    for x, y in coordinate:
        # 檢查x, y 是否超出邊界
        
        x += position[0]
        y += position[1]
        if x not in range(0, len(board)): return False
        if y not in range(0, len(board[0])): return False
        # 檢查欲放入方塊位置是否已被填滿
        if board[x][y] != 0 : return False
    return True

def clear(board):
    # 從桌面的最後檢查是否全部填滿
    cnt = len(board)
    while cnt > 0:
        cnt -= 1
        if 0 not in board[cnt]:
            # 如果填滿就把最後踢出(pop)並在前面補上(insert)
            board.pop(cnt)
            board.insert(0, [0 for i in range(len(board[0]))])
            cnt += 1

def fall(coordinate, position, board):
    # 依次把選中的形狀往下一格直到觸底或是遇到其他方塊
    move = 1
    while check(coordinate, (position[0]+1, position[1]), board): position = (position[0]+1, position[1])
    for x,y in coordinate:
        # 更新桌面
        x += position[0]
        y += position[1]
        board[x][y] = 1
def print_board(board):
    for brd in board:
        for b in brd:
            print("＊" if b else "Ｏ", end="")
        print()

# step 1 建立桌面以及俄羅斯方塊位置

w = int(input())
h = int(input())
board = [[0 for i in range(w)] for j in range(h)]
chess = {
        "I":[(0,0), (1,0), (2,0), (3,0)],
        "J":[(2,0), (0,1), (1,1), (2,1)],
        'L':[(0,0), (1,0), (2,0), (2,1)],
        'O':[(0,0), (1,0), (1,1), (0,1)],
        'S':[(0,1), (0,2), (1,0), (1,1)],
        'T':[(0,0), (0,1), (0,2), (1,1)],
        'Z':[(0,0), (0,1), (1,1), (1,2)]
        }


while True:
    try:
        line = input()
        if line == 'e':
            break
        line = line.split(' ')
        #step 2 確認擺放位置是否超出範圍
        if not check(chess[line[0]], (0, int(line[1])), board):
            print("Game Over!")
            break

        #step 3 紀錄選中的方塊要向左或右移動幾步
        move = 0
        left_or_right = []
        if len(line) >= 3:
            left_or_right = line[2:]
        for c in left_or_right:
            #step 4 確認往右往左擺放位置是否成功，如果成功就紀錄，如果撞到東西就留在原地
            if c == "right":
                if check(chess[line[0]], (0, int(line[1])+1), board): move+=1
            else:
                if check(chess[line[0]], (0, int(line[1])-1), board): move-=1
        #step 4 把選中的方塊向左或右移動
        
        #step 5 使方塊下降到最下面
        fall(chess[line[0]], (0, int(line[1])+move), board)
        # print_board(board)
        #step 6 清除存在的橫排
        clear(board)
        # print_board(board)
    except EOFError:
        print_board(board)
        break
