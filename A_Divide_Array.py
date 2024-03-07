n=int(input())
a=list(map(int,input().split()))
a1,a2,a3=[],[],[]
for i in a:
    if i<0:a1.append(i)
    elif i>0:a2.append(i)
    else:a3.append(i)
if not len(a1)&1:
    a3.append(a1.pop())
if len(a2)==0:
    a2.append(a1.pop())
    a2.append(a1.pop())
print(len(a1),*a1)
print(len(a2),*a2)
print(len(a3),*a3)