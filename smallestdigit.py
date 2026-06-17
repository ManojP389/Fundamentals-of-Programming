n =int(input())
arr =[]
for i in range(n):
    n = int(input())
    arr.append(n)

min = arr[0]
for i in arr:
    if i>min:
        min = i
print(min)
