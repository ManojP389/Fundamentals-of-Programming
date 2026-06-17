s = input().split()
t = input()
freq= {}
for word in s:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

for key,value in freq.items():
    if key == t:
        # res=freq[key]
    
      print(freq[key])
