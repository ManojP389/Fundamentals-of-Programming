l = list(map(int,input().split()))
flag = False
for num in l:
    if num!=l[0]:
      flag = True
if flag:
   print("Not all are same")
else:
   print("All are same")
