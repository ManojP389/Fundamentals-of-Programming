# n = int(input())
# count = 0
# s = str(n)
# a = list(s)
# for i in s:
#     if int(i)%2==0:
#         count = count + 1
# print(count)

n =int(input())
count = 0
while(n>0):
    digit = n%10
    if digit%2==0:
        count = count + 1
    n = n//10
print(count)