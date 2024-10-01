n = int(input())
t = list(map(int, input().split()))
pr = []
m = []
p = []
for i in range(len(t)):
    if t[i] == 1:
        pr.append(i + 1)
    elif t[i] == 2:
        m.append(i+1)
    elif t[i] == 3:
        p.append(i+1)
w = min(len(pr),len(m), len(p))
if w > 0:
    for i in range(w):
        print(pr[i], m[i], p[i])
else:
    print(0)