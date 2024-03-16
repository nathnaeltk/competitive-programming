noTests = int(input())

for d in range(noTests):
    string = input()
    codeforces = "codeforces"

    difference = 0
    
    for i in range(10):
        if string[i] != codeforces[i]:
            difference += 1
    
    print(difference)
