
def check(table):
    for i in range(9):
        rowcheck = [0] * 10
        colcheck = [0] * 10
        for j in range(9):
            rowcheck[table[i][j]] = 1
            colcheck[table[j][i]] = 1
        if sum(rowcheck) != 9 or sum(colcheck) != 9:
            return False

    for i in range(3):
        for j in range(3):
            boxcheck = [0] * 10
            for k in range(3):
                for s in range(3):
                    boxcheck[table[3*i+k][3*j+s]] = 1
            if sum(boxcheck) != 9:
                return False
    return True

table = [list(map(int, input().split()))for _ in range(9)]
if check(table):
    print("YES")
else:
    print("NO")