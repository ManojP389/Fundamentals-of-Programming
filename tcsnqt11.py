n=int(input())
m=int(input())
arr=[]
for i in range(n):
    a=float(input())
    arr.append(a)
for i in range(m):
    b=float(input())
    arr.append(b)  
cost=0
for i in range(0,n):
    cost=cost+(arr[i]*18)
for i in range(n,len(arr)):
    cost=cost+(arr[i]*12)

print(cost)