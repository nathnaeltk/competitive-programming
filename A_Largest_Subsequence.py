def lexicographically_largest_subsequence_with_indices(s):
    char_stack = []
    index_stack = []
    n = len(s)

    for i in range(n):
        # Pop the stack while the current character is greater than the top of the stack
        while char_stack and s[i] > char_stack[-1]:
            char_stack.pop()
            index_stack.pop()

        # Push the current character onto the stack
        char_stack.append(s[i])
        index_stack.append(i)

    # Build the result subsequence and indices
    result = {'subsequence': [], 'indices': []}
    while char_stack:
        result['subsequence'].append(char_stack.pop())
        result['indices'].append(index_stack.pop())

    return result

def solve():
    n = int(input())
    s = input().strip()
    result = lexicographically_largest_subsequence_with_indices(s)

    ch2 = [0] * 26
    t2 = list(s)
    for char in s:
        ch2[ord(char) - ord('a')] += 1

    t = []
    for i in range(26):
        for j in range(ch2[i]):
            t.append(chr(i + ord('a')))

    vec = []
    count = [0] * 26
    visited = [0] * n
    for idx in result['indices']:
        visited[idx] = 1

    for char in result['subsequence']:
        count[ord(char) - ord('a')] += 1

    rem = 0
    for i in range(25, -1, -1):
        if count[i] != 0:
            rem = count[i]
            break

    for i in range(26):
        for j in range(count[i]):
            vec.append(chr(i + ord('a')))

    op = len(result['subsequence']) - rem
    c = 0
    t2_modified = list(t2)
    for i in range(n):
        if visited[i] == 1:
            t2_modified[i] = vec[c]
            c += 1

    if t == t2_modified:
        print(op)
    else:
        print(-1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
