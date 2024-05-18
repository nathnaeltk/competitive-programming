num_tires = int(input())
tire_stack = []
next_removal = 1
reorder_count = 0

for _ in range(2 * num_tires):
    action = list(input().split())

    if action[0] == 'remove':
        if tire_stack and tire_stack[-1] == next_removal:
            tire_stack.pop()
        else:
            if tire_stack:
                reorder_count += 1
            tire_stack = []
        next_removal += 1

    elif action[0] == 'add':
        tire_stack.append(int(action[1]))

print(reorder_count)
