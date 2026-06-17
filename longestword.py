arr = list(map(str, input().split()))
max = len(arr[0])
for i in arr:
    if len(i)>max:
        max = len(i)

for l in arr:
    if len(l)==max:
        print(l)