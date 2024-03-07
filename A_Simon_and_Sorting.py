def solve():
    s = input()
    p = 0

    if s[0] != 'a':
        p += 1
    if s[1] != 'b':
        p += 1
    if s[2] != 'c':
        p += 1

    if p == 0 or p == 2:
        print("YES")
        return
    print("NO")


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        solve()
