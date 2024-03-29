t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    for i in range(len(arr)):
        j = i
        while j < len(arr):
            subarr = arr[i:j+1]
            tans = 0
            unique = []
            for l in range(len(subarr)):
                if subarr[l] >= l:
                    tans += 1
            if tans == len(subarr) and subarr not in unique:
                ans += 1
                unique.append(subarr)
            j += 1

    print(ans)


