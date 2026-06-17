import math
a,b,c = map(int,input().split())

res= math.pow(a,3)+math.pow(a,2)*b+2*math.pow(a,2)*b+2*a*math.pow(b,2)+a*math.pow(b,2)+math.pow(b,3)
print(res)
