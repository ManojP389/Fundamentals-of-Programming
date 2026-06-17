n=int(input())
balls=list(map(str,input().split()))
freq={}
flag=False
for i in balls:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
for value in freq.values():
    if value%2!=0:
        flag=True
        break
if flag:
    for key,value in freq.items():
            if value%2!=0:
                print(key)
                break
else:
        print("All are Even")