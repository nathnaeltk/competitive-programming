def generate_unique_name(files, query):
    count = files.get(query, 0) + 1
    files[query] = count
    return query + str(count)

n = int(input())
files = {}

for _ in range(n):
    query = input()
    if query in files:
        new_name = generate_unique_name(files, query)
        print(new_name)
    else:
        files[query] = 0
        print("OK")
