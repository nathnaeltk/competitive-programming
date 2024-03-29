n, s = map(int, input().split())

arr = list(map(int, input().split()))
freq = {}
left = 0
count = 0

for right in range(n):
    freq[arr[right]] = freq.get(arr[right], 0) + 1

    while len(freq) > s:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            del freq[arr[left]]
        left += 1

    count += right-left+1
print(count)