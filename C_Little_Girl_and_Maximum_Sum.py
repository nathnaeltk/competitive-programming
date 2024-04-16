# n is the length of the array and q is the number of queries
n, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

coverage_redundency = [0] * n
ls = []
rs = []

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    ls.append(l)
    rs.append(r)

    for i in range(len(a)):
        if a[i] in range(l, r + 1):
            coverage_redundency[i] += 1

# place the biggest element in the array at the index where the coverage_redundency is the highest
r = len(a)-1
while r > 0:
    max_coverage = max(coverage_redundency)
    max_index = coverage_redundency.index(max_coverage)
    a[r] = max_coverage[max_index]
    r -= 1

print(a)
print(coverage_redundency)
# answer = 0

# for i in range(len(rs)):
#     answer += sum(coverage_redundency[ls[i]:rs[i]+1])

# print(answer)