test_cases = int(input())

for _ in range(test_cases):
    contest_duration = int(input())
    contest_log = input().strip()
    problem_count = [0] * 26

    for problem in contest_log:
        problem_count[ord(problem) - ord('A')] += 1

    solved_problems = 0
    for i in range(26):
        if problem_count[i] >= i + 1:
            solved_problems += 1

    print(solved_problems)
