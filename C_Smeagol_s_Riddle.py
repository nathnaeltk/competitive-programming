n = int(input())

words = []

for _ in range(n):
    word = input().strip()
    words.append(word)

for word in words:
    left, right = 0, len(word) - 1
    changes = 0

    while left < right:
        if word[left] != word[right]:
            changes += 1
        left += 1
        right -= 1

    print(changes)