arr = list(map(int,input().split()))
a = arr[0]

for i in range(1,len(arr)):
    if(arr[i]>a):
        a = arr[i]

print(a)