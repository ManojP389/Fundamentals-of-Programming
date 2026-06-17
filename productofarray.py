# arr =list(map(int,input().split()))
# res=[]
# p=1
# for i in range(len(arr)):
#     arr.remove(arr[i])
#     for num in arr:
#         p=p*num
#     res.append(p)
#     arr.append(arr[i])
# for z in res:
#     print(z,end=" ")

arr=list(map(int,input().split()))
res=[]
for i in range(len(arr)):
    p=1
    for j in range(len(arr)):
        if j!=i:
            p=p*arr[j]
        
    res.append(p)
for k in res:
    print(k,end=" ")



