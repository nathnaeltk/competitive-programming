# Problem: A - Algorithm Test I - https://codeforces.com/gym/544347/problem/A

import math

m = int(input())  
a = list(map(int, input().split()))  

distinct_colors = set(a)

result = math.factorial(len(distinct_colors))

print(result)
