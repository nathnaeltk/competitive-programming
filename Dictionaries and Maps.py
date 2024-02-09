# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())

phone_book = {}

for _ in range(n):
    entry = input().split()
    name, phone_number = entry[0], entry[1]
    phone_book[name] = phone_number

while True:
    try:
        query = input().strip()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
