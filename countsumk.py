n = int(input())
arr = list(map(int, input().split()))
sum = int(input())
count = 0
for i in range(n):
    for j in range(i,n):
        if arr[i]+arr[j] == sum:
            count+=1
print(count)