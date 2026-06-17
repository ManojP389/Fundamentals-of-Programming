s = input()
freq={}
for i in s:
    freq[i] = freq.get(i,0)+1

for key,value in freq.items():
    print(str(key)+str(value),end="")