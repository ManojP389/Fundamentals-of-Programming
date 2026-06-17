# s = input().trim()
# freq1={}
# freq2={}
# for i in s:
#     if ((i in freq1) and (i==")" or "(")) :
#         freq1[i]+=1
#     elif ((i not in freq1) and (i==")" or "(")):
#         freq1[i]=1 
#     elif ((i in freq2) and i.isalpha()): 
#         freq2[i]+=1
#     else:
#         freq2[i]=1
# for ch in s:
#     if ch=="(":
#         freq1[ch]-=1 and freq1[")"]-=1
# if len(freq1)>1:
#     print("Invalid")
# else:
#     print("Valid")
s = input()
count = 0
for i in s:
    if i=="(":
        count+=1
    elif i==")":
        count-=1
    if count <0:
        print("Invalid")
        break
else:    
 if count == 0:
    print("Valid")
    
 else:
    print("Invalid")
    


