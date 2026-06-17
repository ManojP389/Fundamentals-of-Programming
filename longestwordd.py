s = input().split()
freq={}
for word in s:
    freq[word]=len(word)
a=0
for value in freq.values():
    if value>a:
        a=value

for key,value in freq.items():
    if value ==a:
        print(key)
        break







    