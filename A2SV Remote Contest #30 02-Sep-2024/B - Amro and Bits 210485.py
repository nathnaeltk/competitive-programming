# Problem: B - Amro and Bits - https://codeforces.com/gym/545837/problem/B

t = int(input())  
for _ in range(t):
    x = int(input()) 
    binary_x = bin(x) 
    first_one_index = 0

    for i in range(len(binary_x) - 1, 1, -1):
        if binary_x[i] == '1':
            first_one_index = i
            break

    result_bin = '0b' + binary_x[first_one_index:] 
    other_one_found = False

    for i in range(len(binary_x) - 1, 1, -1):
        if binary_x[i] == '1' and i != first_one_index:
            other_one_found = True
            break

    if not other_one_found:
        if len(result_bin) == 3:
            result_bin += '1'
        else:
            result_bin = result_bin[:-1] + '1'

    print(int(result_bin, 2))  