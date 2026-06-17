s=input().strip().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in alphabet:
        alphabet= alphabet.replace(i,'')

if alphabet == "":
    print("Panagram")
else:
    print("Not Panagram")

# if new=="":
#     print("Panagram")
# else:
#     print("Not Panagram")

# alphabet = "abc"
# alphabet.replace('a', '')
# print(alphabet)