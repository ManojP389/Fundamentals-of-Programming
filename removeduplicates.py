# s = input().strip()
# res = "" 
# for i in s:
#     if i not in res:
#         res+=i
# print(res)
s = input().strip()
res = ""
for i in range(len(s)): 
    for j in range(i):
        if s[i] == s[j]:
            break
    else:
        res += s[i]
print(res)