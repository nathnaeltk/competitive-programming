# Problem: A - Distribute - https://codeforces.com/gym/555625/problem/A

n = int(input())
cards = list(map(int, input().split()))
dict = {}

for i, card in enumerate(cards):
    if card in dict:
        dict[card].append(i + 1)
    else:
        dict[card] = [i + 1]
cards.sort()

for i in range(n // 2):
    print(dict[cards[i]].pop(0), dict[cards[n - 1 - i]].pop(0)) 