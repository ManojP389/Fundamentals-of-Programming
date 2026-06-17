s=input().strip()
count=0
res=""
for i in s:
    if i=="#":
        count+=1
for i in range(count):
    res=res+"#"
for j in s:
    if j!="#":
        res=res+j

print(res)

