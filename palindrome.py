s = input().strip()
l = 0
r = len(s)-1
while l<r:
    if(s[l]!=s[r]):
        print("False")
        break
    else:
        print("True")
        break

    l=l+1
    r=r-1