# n = input()
# arr = list(n)
# max = arr[0]
# for i in range(0 ,len(arr),1):
#     if(arr[i]>max):
#         max = arr[i]
# print(max)
n = int(input())
max = n%10
while(n>0):
    temp =n%10
    if temp>max:
        max = temp
    n = n//10
print(max)
