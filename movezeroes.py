n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
    if arr[i] == 0:
        for j in range(n):
            arr[j] = arr[j+1]

print(arr)
