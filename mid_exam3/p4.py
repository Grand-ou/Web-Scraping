def check_row_available(region, row, column, cube, height):
    """
    確認方塊可不可以放在這個 row
    """
    for i in range(len(cube)):
        r, c = cube[i]
        cc = column + c
        rr = row + r
        if rr >= height:
            return False
        if region[rr][cc]:
            return False
    return True

def get_button_row(region, cube, column, height):
    """
    找到方塊最低可以放在哪個 row
    """
    button_row = -1
    for row in range(height):
        if check_row_available(region, row, column, cube, height):
            button_row += 1
        else:
            break
    return button_row

def put_cube_in_region(region, cube, column, height):
    """
    把方塊放在找到的特定 row
    """
    row = get_button_row(region, cube, column, height)
    if row == -1:
        return "Game Over!"
    for i in cube:
        cube_r, cube_c = i
        region[row+cube_r][column+cube_c] = 1
    return region

def remove_full_row(region):
    ans_region = []
    cnt = 0
    for i in range(len(region)):
        mark = True
        for j in range(len(region[0])):
            if not region[i][j]:
                mark = False
        if mark:
            cnt += 1
            ans_region.insert(0, [0 for i in range(len(region[0]))])
        else:
            ans_region.append(region[i])
    return ans_region, cnt 

cube_shape = {
    "I":[(0,0), (1,0), (2,0), (3,0)],
    "J": [(2,0), (0,1), (1,1), (2,1)],
    "L": [(0,0), (1,0), (2,0), (2,1)],
    "O": [(0,0), (0,1), (1,0), (1,1)], 
    "S": [(0,1), (1,0), (1,1), (0,2)],
    "T": [(0,0), (0,1), (0,2), (1,1)],
    "Z": [(0,0), (0,1), (1,1), (1,2)]
}
def find_cube_table(cube_mark):
    """
    把特定方塊的想對位置回傳
    """
    global cube_shape
    return cube_shape[cube_mark]

def check_column_available(cube, width, x, region):
    """
    確認 column 是否合法
    """
    if x < 0 or x >= width:
        return False
    for i in cube:
        cube_row, cube_column = i
        if x + cube_column >= width:
            return False
        if region[cube_row][cube_column+x]:
            return False   
    return True

width = int(input())
height = int(input())
N = int(input())
score = 0
region = [[0 for i in range(width)] for i in range(height)]
con = 0
while 1:
    try:
        s = input().split()
        cube_mark = s[0]
        x = int(s[1])
        cube = find_cube_table(cube_mark)
        if len(s) > 2:
            for i in s[2:]:
                if i == "left" and check_column_available(cube, width, x-1, region):
                    x -= 1
                elif i == "right" and check_column_available(cube, width, x+1, region):
                    x += 1
        region = put_cube_in_region(region, cube, x, height)
        if region ==  "Game Over!": break
        region = remove_full_row(region)
        score
    except: break

if region == "Game Over!":
    print(region)
else:
    for i in range(height):
        for j in range(width):
            if not region[i][j]:
                print("Ｏ", end='')
            else:
                print("＊", end='')
        print()
