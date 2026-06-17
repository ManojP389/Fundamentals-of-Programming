s = input()
key = int(input())
alphabets="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res=""
for letter in s:
    if letter in alphabets:
        a=alphabets.index(letter)
        z=(a+key)%26
        res=res+alphabets[z]
    elif letter in b:
        n=b.index(letter)
        y=(n+key)%26
        res=res+b[y]
    else:
        res=res+letter
        

print(res)

