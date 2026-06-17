s = input().strip()
count=0
count1=0
flag=True
for ch in s:
    if ch=="#":
        count+=1
    if ch=="*":
        count1+=1
if count==count1:
    print("0")
if count1>count:
    print("1")
if count1<count:
    print("0")

     

