n = int(input())
powers = list(map(int, input().split()))

scores = [[0] * n for _ in range(n)]

for gap in range(n):
    for i in range(n - gap):
        j = i + gap
        temp1 = 0
        if (i + 2) <= j:
            temp1 = scores[i + 2][j]
        temp2 = 0
        if (i + 1) <= (j - 1):
            temp2 = scores[i + 1][j - 1]
        temp3 = 0
        if i <= (j - 2):
            temp3 = scores[i][j - 2]
        scores[i][j] = max(powers[i] + min(temp1, temp2), powers[j] + min(temp2, temp3))

hermione_score = scores[0][n - 1]
harry_score = sum(powers) - hermione_score

print(hermione_score, harry_score)