nums = [-2, 0, 3, -5, 2, -1]
ops = [[0, 2], [2, 5], [0, 5]]

prefix_sum = [nums[0]]
ans = []

for i in range(1, len(nums)):
    prefix_sum.append(prefix_sum[-1] + nums[i])

for i in ops:
    element = prefix_sum[i[1]] - prefix_sum[i[0]] + nums[i[0]]
    ans.append(element)

print(ans)