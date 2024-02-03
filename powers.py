# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_powers(a, b, m):
    result1 = pow(a, b)
    result2 = pow(a, b, m)
    print(result1)
    print(result2)

a = int(input())
b = int(input())
m = int(input())

calculate_powers(a, b, m)
