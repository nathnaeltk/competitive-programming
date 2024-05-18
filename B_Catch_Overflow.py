INF = 1 << 32
l = int(input())
cur = [1]  
res = 0
for _ in range(l):
    t = input().strip()
    if t == "for":
        x = int(input())
        cur.append(min(INF, cur[-1] * x))
    elif t == "end":
        if len(cur) > 1:  
            cur.pop()
        else:
            print("OVERFLOW!!!")
    else:
        if cur:  
            res += cur[-1]
        else:
            print("OVERFLOW!!!")
if res >= INF:
    print("OVERFLOW!!!")
else:
    print(res)
