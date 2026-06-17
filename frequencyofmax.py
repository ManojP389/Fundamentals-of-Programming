n =int(input())
arr=[]
for i in range(n):
    num = int(input())
    arr.append(num)
freq ={}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for i in range(1, n):
    max = arr[0]
    if arr[i]>max:
        max = arr[i]
print(freq[max])