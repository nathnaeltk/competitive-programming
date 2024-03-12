
# Input
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []

a_ptr, b_ptr = 0, 0

while a_ptr < n and b_ptr < m:
    if A[a_ptr] < B[b_ptr]:
        print(A[a_ptr], end=' ')
        a_ptr += 1
    else:
        print(B[b_ptr], end=' ')
        b_ptr += 1

while a_ptr < n:
    print(A[a_ptr], end=' ')
    a_ptr += 1
while b_ptr < m:
    print(B[b_ptr], end=' ')
    b_ptr += 1