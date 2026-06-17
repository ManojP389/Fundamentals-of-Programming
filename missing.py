n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))



for i in range(1,n+1):
    if i not in arr:
        print(i)
        
