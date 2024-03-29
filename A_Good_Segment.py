n = int(input())
s = input()
left = 0
res = 1
current = 1

for r in range(1, n):
    if ord(s(r-1)+1 == ord(s(r))):
        current+=1
    else:
        current+=1

    if current>res:
        res = current

print(res)