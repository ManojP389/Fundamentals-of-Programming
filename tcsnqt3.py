n=int(input())
# li=[]
# for i in range(n):
#     num=int(input())
#     li.append(num)
li=list(map(int,input().split()))
a=li[0]
count=0
for i in li:
    if i>=a:
        count+=1

print(count)

    