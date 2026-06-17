# n = int(input())
# sum = 0
# while(n>0):
#     digit = n%10
#     sum = sum + digit
#     n=n//10
# print(sum)
n = input()
sum  =0
for i in n:
    sum = sum + int(i)
print(sum)