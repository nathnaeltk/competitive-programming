t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    if s[0] == s[-1]:
        print(len(s), end="")
        for i in range(len(s)-1):
            print(i+1, end=" ")
        
    else:
        print(-1)
        continue
    