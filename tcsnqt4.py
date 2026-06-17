n=int(input())
m = int(input())
arr=[]
l=[]
for i in range(n):
    li=list(map(int,input().split()))
    arr.append(li)
# target =0
# for i in range(n):
#     for j in range(n):
#         if arr[i][j]==1:
#             target+=1
for i in range(n):
    count=0
    for j in range(n):
        if arr[i][j]==1:
            count+=1     
    l.append(count)
x=l[0]
for i in l:
    if i>x:
        x=i
print(x)
# print(max(arr))

