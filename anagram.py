s = input().strip().lower()
t = input().strip().lower()
freq={}
for i in s:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
flag = False
for i in t:
    if i in freq:
        freq[i]-=1
 
for value in freq.values():
    if value !=0:
        flag = True

if flag or len(s) != len(t):
    print("Not Anagram")

else:
    print("Anagram")
