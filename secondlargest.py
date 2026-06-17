n =int(input())
arr =[]
for i in range(n):
    num = int(input())
    arr.append(num)
    
for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr[1])