# Input
n, target = map(int, input().split())
values = list(map(int, input().split()))

# Create a list of tuples with values and indices
values = [(value, index + 1) for index, value in enumerate(values)]

# Sort the values based on their actual values
values.sort()

# Iterate through the values
for i in range(n):
    for j in range(i+1, n):
        left = j+1
        right = n-1
        while left < right:
            current_sum = values[i][0] + values[j][0] + values[left][0] + values[right][0]
            if current_sum == target:
                # Print the positions of the values
                positions = [values[i][1], values[j][1], values[left][1], values[right][1]]
                print(" ".join(map(str, sorted(positions))))
                exit()
            elif current_sum < target:
                left += 1
            else:
                right -= 1

print("IMPOSSIBLE")
