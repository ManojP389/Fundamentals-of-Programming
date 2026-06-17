n =int(input())
x=7000
if n>x:
    print("INVALID INPUT")
if n==0:
    print("Time Estimated: 0 minutes")
if 0<n<=2000:
    print("Time Estimated:25 minutes")
if n>2001 and n<=4000:
    print("Time Estimated:35 minutes")
if n>4000:
    print("Time Estimated:45 minutes")
