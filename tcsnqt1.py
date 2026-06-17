v=int(input())
w=int(input())
# for i in range(1,v+1):
#     for j in range(1,v+1):
#         if 2*i+4*j==w:
#             print("TW:"+str(j)+" "+"FW:"+str(i))
a=4*v
TW=0
i=2
# a=a-i
# if a!=w:
#     TW+=1
while a>=w:
    a=a-i
    if a!=w:
        TW+=1
FW = v-TW
print("TW="+str(TW)+" "+"FW="+str(FW))
