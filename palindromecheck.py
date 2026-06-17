s = input()
arr =list(s)
l = 0
r = len(arr)-1
flag = False
while l<r:
    if arr[l] == arr[r]:
        l=l+1
        r=r-1
    else:
        flag = True
        print("False")
        break

if flag == False:
    print("True")