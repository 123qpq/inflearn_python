def qsort(lt, rt): #전위 순회 방식
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        
        qsort(lt, pos-1)
        qsort(pos+1, rt)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("Before sort : ", end='')
    print(arr)
    qsort(0, len(arr)-1)
    print(arr)