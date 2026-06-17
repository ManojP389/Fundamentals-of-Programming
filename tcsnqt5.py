t=int(input())
entry=list(map(int,input().split()))
exit=list(map(int,input().split()))
g=0
x=[]
for i in range(t):
    g=(g+entry[i])-(exit[i])
    x.append(g)
print(max(x))

    
    

