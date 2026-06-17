s=input()
# rev="" 
# a="|"

# for i in range(len(s)-1,-1,-1):
#     if s[i].isalpha():
#         rev=rev+s[i]
#     else:
#         if s[i] in a:
#             rev=rev+s[i]
# print(rev)
arr=[]
for i in range(len(s)-1,-1,-1):
    if s[i].isalpha():
        arr.append(s[i])
q="".join(arr)
res=[]
j=0
for x in s:
    if x.isalpha():
        res.append(q[j])
        j+=1
    else:
        res.append(x)

ans="".join(res)
print(ans)



    