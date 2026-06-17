n =int(input())
arr =[]
count = 0
for i in range(n):
    num = int(input())
    arr.append(num)
for i in arr:
    if i>0:
        count+=1
print(count)