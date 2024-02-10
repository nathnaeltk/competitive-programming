n = int(input())

current_passengers = 0 
min_capacity = 0  

for _ in range(n):
    a, b = map(int, input().split())

    current_passengers = current_passengers - a + b

    min_capacity = max(min_capacity, current_passengers)

print(min_capacity)
