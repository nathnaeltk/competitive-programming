n=input()
times = list(map(int, input().split()))
times.sort()
wait = 0
count = 0
for i in range(len(times)):
    if times[i] >= wait:
        wait += times[i]
        count+=1
print(count)