n=int(input())
li=list(map(int,input().split()))
a=set()
sum1=0
for x in li:
    a.add(x)

for k in a:
    sum1=sum1+k

print(sum1)