n =int(input())
arr = list(map(int,input().split()))
k = int(input())
li=[]
for i in range(len(arr)-k,n):
    li.append(arr[i])
for j in range(0,len(arr)-k):
    li.append(arr[j])
print(li)

