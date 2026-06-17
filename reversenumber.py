# n =int(input())
# rev = ""
# while n>0:
#     digit = n%10
#     rev = rev +str(digit)
#     n = n//10
# print(rev)
s = input()
rev = ""

for i in range(len(s)-1,-1,-1):
    rev = rev +s[i]
print(rev)
    
      