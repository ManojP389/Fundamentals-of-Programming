arr = list(map(int,input().split()))
freq={}
for k in arr:
    if k in freq:
        freq[k]+=1
    else:
        freq[k]=1
a=0
for value in freq.values():
    if value>a:
        a=value

for key,value in freq.items():
    if value ==a:
        print(key)
        break







    