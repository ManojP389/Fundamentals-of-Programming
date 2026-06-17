t =int(input())

for i in range(t):
    N,K,X=map(int,input().split())
    A=list(map(int,input().split()))
l = 0
r=len(A)-1
# res=[]
while r-l+1>K:
    if abs(A[l]-X)>abs(A[r]-X):
        # res.append(A[l])
        l+=1
    else:
        # res.append(A[r])
        r-=1
print(A[l:r+1])

