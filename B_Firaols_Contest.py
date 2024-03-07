max_difficulty, num_problems = map(int, input().split())

frequencies = {}
difficulties = list(map(int, input().split(" ")))
result = ""

problem_set_count = 0
for difficulty in difficulties:
    if not(difficulty in frequencies) or frequencies[difficulty] == 0:
        problem_set_count += 1
        frequencies[difficulty] = 1

        if problem_set_count == max_difficulty:
            result += "1"
        else:
            result += "0"
    else:
        result += "0"
        frequencies[difficulty] += 1

    if problem_set_count == max_difficulty:
        for dif in frequencies.keys():
            frequencies[dif] -= 1

            if frequencies[dif] == 0:
                problem_set_count -= 1

print(result)
