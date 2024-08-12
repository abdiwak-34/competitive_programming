def can_reorder(strings):
    strings.sort(key=len)
    for i in range(len(strings) - 1):
        if strings[i] not in strings[i + 1]:
            return False
    
    return True
n = int(input())
strings = [input().strip() for _ in range(n)]
if can_reorder(strings):
    print("YES")
    for string in strings:
        print(string)
else:
    print("NO")
