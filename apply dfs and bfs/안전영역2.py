import sys
#sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
sys.setrecursionlimit(10**6)    # 파이썬은 최대 1000회 재귀가 기본 설정이다. 
                                # 이를 늘리기 위해 다음과 같이 설정해준다.
def DFS(x, y, h):
    board[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==0 and table[xx][yy]>h:
            DFS(xx, yy, h)

if __name__=="__main__":
    n = int(input())
    cnt = 0
    res = 0
    table=[list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        board=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if board[i][j]==0 and table[i][j]>h:
                    cnt+=1
                    DFS(i, j, h)
        res=max(res, cnt)
        if cnt==0:
            break
    print(res)