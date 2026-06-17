n=int(input())
li=list(map(int,input().split()))
freq={}
for i in li:
    freq[i] = freq.get(i,0)+1
for key,value in freq.items():
    print(str(key)+" "+"occurs"+" "+str(value)+" "+"times")