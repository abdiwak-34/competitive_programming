# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
ans = True
for i in range(n):
    S = set(map(int, input().split()))
    if len(S.difference(A)) != 0 or len(S) == len(A):
        ans = False
        break
print(ans)