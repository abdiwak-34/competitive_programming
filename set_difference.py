# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
li1 = set(map(int, input().split()))
m = int(input())
li2 = set(map(int, input().split()))
print(len(li1.difference(li2)))
