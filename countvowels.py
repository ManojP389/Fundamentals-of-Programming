s = input()
# vowels={"a","e","i","o","u"}
count=0
vowels="aeiou"

for i in s:
    if i in vowels:
        count+=1
print(count)
