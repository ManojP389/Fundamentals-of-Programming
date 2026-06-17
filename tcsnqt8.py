arr=[]
freq={}
for i in range(3):
    li =list(map(int,input().split()))
    arr.append(li)
for i in range(len(arr)):
    avg=0
    for j in range(len(arr)):
        avg=avg+arr[j][i]
    freq[i]=avg
for i in range(len(arr)):
    flag=False
    for j in range(len(arr)):
        if arr[i][j]<1 or arr[i][j]>100:
            flag=True
if flag:
    print("Invalid Input")
q=[]
for value in freq.values():
    q.append(value)
a=q[0]
for k in q:
    if k>=a:
        a=k
print("Highest Average:",a)
for i in range(len(q)):
    if a==q[i]:
        print("Trainee Number:",i+1)
