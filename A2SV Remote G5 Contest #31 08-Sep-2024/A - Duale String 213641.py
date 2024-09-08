# Problem: A - Duale String - https://codeforces.com/gym/547609/problem/A

def is_duale(s):
    if len(s) % 2 != 0:
        return "NO"
    else:
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            return "YES"
        else:
            return "NO"

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(is_duale(s))

if __name__ == "__main__":
    main()
