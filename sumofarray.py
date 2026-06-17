n = int(input())
arr=[]
sum = 0
for i in range(n):
    num = int(input())
    arr.append(num)

for i in arr:
    sum+=i
print(sum)
