x = 13 
n = 4
m = 8

A = [4, 6, 8, 10]
B=[1, 3, 6, 8, 9, 10, 11, 12]

rez = x
for i in range(1, n + 1):
    x = x - abs(A[n - i] - B[m - (n - i) - 1]) + abs(A[n - i] - B[i - 1])
    print(f"|A[{n-i}] - B[{m-(n-i)-1}]| + |A[{n-i}] - B [{i-1}]|")
    rez = max(rez, x)
    print(f"result set to {rez} because of")