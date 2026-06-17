n = int(input())
arr=[]
flag = True
for i in range(n):
    li = list(map(int,input().split()))
    arr.append(li)
target = sum(arr[0])

for i in range(n):
    sumr = 0
    for j in range(n):
        sumr=sumr+arr[i][j]
    
    if sumr!=target:
        flag = False

for i in range(n):
    sumc = 0
    for j in range(n):
        sumc=sumc+arr[j][i]
    if sumc!=target:
        flag =False
sumd=0
for i in range(n):
    sumd=sumd+arr[i][i]
sumd1=0
for i in range(n):
    sumd1=sumd1+arr[i][n-i-1]

if sumd!=target and sumd1!=target:
    flag=False

if flag ==True:
    print("Yes")
else:
    print("No")