n=int(input())
m=int(input())
arr=[]
for i in range(n):
    row=[]
    for j in range(m):
        num=int(input())
        row.append(num)
    arr.append(row)

for i in range(n):
    for j in range(len(arr[i])):
        print(arr[i][j],end="")
    print()