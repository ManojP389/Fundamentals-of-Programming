n=int(input())
arr=[]
for i in range(n):
    li = list(map(int,input().split()))
    arr.append(li)
#for sum of elements in all rows
# sum = 0
# for i in range(n):
#     for j in range(n):
#         sum=sum+arr[j][i]
# print(sum)
#for sum of elements in all columns
# sum1=0
# for i in range(n):
#     for j in range(n):
#         sum1=sum1+arr[i][j]
# print(sum1)
#for sum of elements in diagonally left to ryt for i n times
# sum2=0
# for i in range(n):
#     for j in range(n):
#         sum2=sum2+arr[j][j]
# print(sum2)
#for sum of elements in diagonally ryt to left for i n times
# sum3=0
# for i in range(n):
#     for j in range(n):
#         sum3=sum3+arr[j][n-1-j]
# print(sum3)
#for sum of elements in each individual rows
# for i in range(n):
#     sum4=0
#     for j in range(n):
#         sum4=sum4+arr[i][j]
#     print(sum4)
#for sum of elements in each individual column
# for i in range(n):
#     sum5=0
#     for j in range(n):
#         sum5=sum5+arr[j][i]
#     print(sum5)
#for sum of elements in each individual diagonal left to ryt
# sum6=0
# for i in range(n):
#     sum6=sum6+arr[i][i]
# print(sum6)
#for sum of elements in each individual diagonal ryt to left
# sum7=0
# for i in range(n):
#     sum7=sum7+arr[n-1-i][n-1-i]
# print(sum7)
for i in range(n-1):
    sum8 = sum(arr[i+1+1])
print(sum8)

    
   


    




