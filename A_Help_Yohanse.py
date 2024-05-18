n = int(input())
if n == 1:
    print(1)
else:
    permutation = [n] + list(range(1, n))
    print(" ".join(map(str, permutation))) 