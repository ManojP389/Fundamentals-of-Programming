l = list(map(int,input().split()))
a=0
b=0
c=0
for num in l:
    if num%2 and num>0==0:
        a=a+1
    if num%2!=0 and num>0:
        b=b+1
    if num<0:
        c=c+1
print(str(a)+" "+str(b)+" "+str(c)+" "+str(a+b))

