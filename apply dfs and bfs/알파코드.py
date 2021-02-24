def dfs(l):
    global cnt
    if l == nlen:
        for i in wlst:
            print(i, end = "")
        print()
        cnt += 1
    elif int(num[l]) != 0:
        wlst.append(chr(int(num[l])+64))
        dfs(l+1)
        wlst.pop()
        if l+2 <= nlen and int(num[l:l+2]) <= 26:
            wlst.append(chr(int(num[l:l+2])+64))
            dfs(l+2)
            wlst.pop()


if __name__ == "__main__":
    num = input()
    nlen = len(num)
    wlst = []
    cnt = 0
    dfs(0)
    print(cnt)