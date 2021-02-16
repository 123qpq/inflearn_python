import sys

def dfs(v):
    if v > 7:
        return
    else:
        #print(v, end = " ") # 전위순회
        dfs(v*2)   # 왼쪽노드
        #print(v, end = " ") # 중위순회
        dfs(v*2+1) # 오른쪽노드
        #print(v, end = " ") # 후위순회

if __name__ == "__main__":
    dfs(1)