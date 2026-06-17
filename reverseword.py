s=input().split()

for i in s:
    rev=""
    for k in range(len(i)-1,-1,-1):
        rev=rev+i[k]

    print(rev,end=" ")

