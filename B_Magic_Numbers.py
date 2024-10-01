st = input()
left = 0
while left < len(st):
    if st[left:left+3] == '144':
        left +=3
    elif st[left:left+2] == '14':
        left +=2
    elif st[left:left+1] == '1':
        left +=1
    else:
        print('NO')
        break
if left == len(st):
    print('YES')