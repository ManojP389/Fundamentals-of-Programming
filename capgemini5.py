n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])

for i in range(n):
        a=arr[i][0]
        b=arr[i][1]
        res=(a*4)+(b*2)
        print(res)





    
    