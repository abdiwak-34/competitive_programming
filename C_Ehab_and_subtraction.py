def ehab_and_subtraction(n, k, arr):
    arr.sort()
    result = []
    last_printed = 0
    
    for i in range(k):
        while i < n and arr[i] == last_printed:
            i += 1
        if i < n:
            result.append(arr[i] - last_printed)
            last_printed = arr[i]
        else:
            result.append(0)
    
    print("\n".join(map(str, result)))
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ehab_and_subtraction(n, k, arr)
