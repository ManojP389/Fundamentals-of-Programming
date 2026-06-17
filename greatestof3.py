# arr = list(map(int, input().split()))
# max = arr[0]
# for i in arr:
#     if i>max:
#         max = i
# print(max)
a,b,c = map(int, input().split())
max =a
if b>max and b>c:
    max = b
elif c>max and c>b:
    max = c
else:
    max = a
print(max)