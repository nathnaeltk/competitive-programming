def min_operations(a, b, count=0):
    if a == b:
        return count
    elif a > b:
        return float('inf')
    else:
        return min(min_operations(a * 2, b, count + 1), min_operations(a - 1, b, count + 1))

a, b = map(int, input().split())
result = min_operations(a, b)
print(result if result != float('inf') else -1)
