shapes = input("")

count = 0
current_count = 0

for shape in shapes:
    if shape == "O":
        current_count += 1
        count = max(count, current_count)
    else:
        current_count = 0

print(count)
