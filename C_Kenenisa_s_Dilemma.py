def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        ans = 0
        if a > b:
            temp = a - b
            if temp % 2:
                ans += 2
            else:
                ans += 1
        elif a == b:
            ans = 0
        else:
            temp = b - a
            if temp % 2:
                ans += 1
            else:
                ans += 2
        print(ans)

if __name__ == "__main__":
    main()
