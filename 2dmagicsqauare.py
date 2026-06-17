n = int(input())
arr=[]
for i in range(n):
    li = list(map(int,input().split()))
    arr.append(li)
# #summing all values row wise
# sumr=0
# for i in range(n):
#     for j in range(n): 
#         sumr=sumr+arr[i][j]
#         b = sumr-sumd1
# print(sumr)
# #summing all values row column
# sumc=0
# for i in range(n):
#     for j in range(n): 
#         sumc=sumc+arr[j][i]
#         a=sumc-sumd1
# print(sumc)
# summing all values diaginally left to ryt
# sumd=0
# for i in range(n): 
#         sumd=sumd+arr[i][i]

# # print(sumd)
# #summing all values diaginally ryt to left
# sumd1=0
# for i in range(n): 
#         sumd1=sumd1+arr[i][n-1-i]
# # print(sumd1)
# z=sumd+sumd1
# #summing all values row wise
# sumr=0
# for i in range(n):
#     for j in range(n): 
#         sumr=sumr+arr[i][j]
#         b = sumr-sumd1
# # print(sumr)
# #summing all values row column
# sumc=0
# for i in range(n):
#     for j in range(n): 
#         sumc=sumc+arr[j][i]
#         a=sumc-sumd1
# # print(sumc)
# if z==a==b:
#      print("Yes")
# else:
#      print("No")
#these code is to check whether the sum of rows and columns and diagonals are equal or not

