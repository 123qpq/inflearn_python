def dsort(lt, rt):
    if lt < rt:
        mid = (lt+rt) // 2
        dsort(lt, mid)
        dsort(mid+1, rt)
        p1= lt
        p2= mid + 1
        temp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                temp.append(arr[p1])
                p1 += 1
            else:
                temp.append(arr[p2])
                p2 += 1
        if p1 <= mid:
            temp += arr[p1:mid+1]
        if p2 <= rt:
            temp += arr[p2:rt+1]
        print(temp)
        for i in range(len(temp)):
            arr[lt+i] = temp[i]


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("befor :", end = ' ')
    print(arr)
    dsort(0, len(arr)-1)
    print("after :", end = ' ')
    print(arr)